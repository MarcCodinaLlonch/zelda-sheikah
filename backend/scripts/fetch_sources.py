"""PAS 1 · Obté totes les dades en brut de zeldawiki.wiki.

Genera `data/raw/sources.json` amb:
  - TOTES les entrades del Compendi de Hyrule de Breath of the Wild i Tears of the Kingdom
    (número, nom, categoria, descripció oficial en anglès, llocs, materials, propietats).
  - Els elements de la llista curada `data/curated.json` (personatges, races, llocs, jocs),
    amb el text introductori de la wiki i la millor imatge candidata.

Aquest fitxer en brut NO el serveix l'API: és la base per escriure les descripcions en català
i per descarregar les imatges (pas 2).

Ús:  venv/bin/python scripts/fetch_sources.py
"""
import json
import os
import re
import sys
import unicodedata

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(__file__))
from wiki import api, chunks  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(ROOT, "data", "raw")
OUT_FILE = os.path.join(RAW_DIR, "sources.json")
CURATED_FILE = os.path.join(ROOT, "data", "curated.json")

COMPENDIUM_PAGES = {
    "botw": ("Hyrule Compendium Items in Breath of the Wild", "Compendium/Extract", "BotW_Hyrule_Compendium"),
    "totk": ("Hyrule Compendium Items in Tears of the Kingdom", "Compendium/Extract/TotK", "TotK_Hyrule_Compendium"),
}

SECTION_TO_CATEGORY = {
    "Creatures": "criatures",
    "Monsters": "enemics",  # els caps se separen després (data/bosses.json)
    "Materials": "materials",
    "Equipment": "equipament",
    "Treasure": "tresors",
}


# ---------------------------------------------------------------- utilitats
def slugify(text):
    text = text.replace("✨", " intact").replace("+", " plus").replace("&", " i ")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text


def file_key(name):
    """Normalitza un nom de fitxer de la wiki (espais -> guions baixos, sense 'File:')."""
    name = name.replace("File:", "").strip()
    return name.replace(" ", "_")


def all_images(prefix):
    names, params = set(), {"action": "query", "list": "allimages", "aiprefix": prefix, "ailimit": 500}
    while True:
        r = api(params)
        names.update(file_key(x["name"]) for x in r["query"]["allimages"])
        if "continue" not in r:
            return names
        params.update(r["continue"])


def image_info(file_names):
    """Retorna {file_key: {"url", "width", "height"}} per a una llista de fitxers."""
    info = {}
    for batch in chunks(sorted(set(file_names)), 50):
        r = api({"action": "query", "titles": "|".join("File:" + f for f in batch),
                 "prop": "imageinfo", "iiprop": "url|size"})
        for page in r["query"]["pages"]:
            ii = (page.get("imageinfo") or [None])[0]
            if ii:
                info[file_key(page["title"])] = {"url": ii["url"], "width": ii["width"], "height": ii["height"]}
    return info


def wikitext(page):
    return api({"action": "parse", "page": page, "prop": "wikitext"})["parse"]["wikitext"]


# --------------------------------------------------------- compendi: llista
def parse_gallery(game):
    page, _, _ = COMPENDIUM_PAGES[game]
    text = wikitext(page)
    rows, section = [], None
    for line in text.splitlines():
        m = re.match(r"^={2,4}\s*(.+?)\s*={2,4}$", line)
        if m:
            section = m.group(1)
            continue
        m = re.match(r"^File:(.+?)\|'''\[\[(.+?)\]\]'''(.*)$", line)
        if not m or section not in SECTION_TO_CATEGORY:
            continue
        file_name, link, rest = m.groups()
        target, _, display = link.partition("|")
        number = master = None
        if game == "botw":
            n = re.search(r"Normal:'''\s*<code>(\d+)\s*\((\d+)\)", rest)
            mm = re.search(r"Master:'''\s*<code>(\d+)\s*\((\d+)\)", rest)
            number = int(n.group(2)) if n else None
            master = int(mm.group(2)) if mm else None
        else:
            n = re.search(r"No\.'''\s*<code>(\d+)", rest)
            number = int(n.group(1)) if n else None
        rows.append({
            "game": game,
            "section": section,
            "target": target.strip(),
            "name_en": (display or target).replace("✨", "").strip(),
            "file": file_key(file_name),
            "number": number,
            "master_number": master,
        })
    return rows


# ------------------------------------------------------- compendi: extractes
HEADING_KEYS = {
    "Description": "description",
    "Common Locations": "locations",
    "Recoverable Materials": "drops",
    "Properties": "properties",
    "Hearts Recovered": "hearts",
    "Cooking Effects": "cooking_effect",
    "Additional Uses": "additional_uses",
}


def parse_compendium_div(div):
    data = {}
    for td in div.find_all("td"):
        heading = td.find(class_="compendium-heading")
        if not heading:
            continue
        key = heading.get_text(" ", strip=True)
        heading.decompose()
        lines = [x.strip() for x in td.get_text("\n", strip=True).split("\n") if x.strip()]
        k = HEADING_KEYS.get(key, slugify(key))
        if k == "description":
            data[k] = " ".join(lines)
        else:
            data[k] = [x for x in lines if x not in ("None", "Unknown", "N/A")]
    return data


def fetch_extracts(game, targets):
    _, template, _ = COMPENDIUM_PAGES[game]
    result = {}
    targets = sorted(set(targets))
    for i, batch in enumerate(chunks(targets, 25)):
        text = "\n\n".join(f'<div id="x{j}">{{{{{template}|{t}}}}}</div>' for j, t in enumerate(batch))
        html = api({"action": "parse", "text": text, "prop": "text", "contentmodel": "wikitext",
                    "disablelimitreport": 1})["parse"]["text"]
        soup = BeautifulSoup(html, "html.parser")
        for st in soup.find_all("style"):
            st.decompose()
        for j, t in enumerate(batch):
            wrapper = soup.find(id=f"x{j}")
            div = wrapper.find(class_="compendium") if wrapper else None
            result[t] = parse_compendium_div(div) if div else {}
        print(f"  [{game}] extractes {min((i + 1) * 25, len(targets))}/{len(targets)}")
    return result


def build_compendium():
    entries = {}
    for game in ("botw", "totk"):
        print(f"📖 Llegint la llista del compendi de {game.upper()}...")
        rows = parse_gallery(game)
        print(f"  {len(rows)} entrades")
        extracts = fetch_extracts(game, [r["target"] for r in rows])
        for r in rows:
            e = entries.setdefault(r["target"], {
                "key": r["target"],
                "name_en": r["name_en"],
                "wiki": r["target"],
                "section": r["section"],
                "games": [],
                "compendium": {},
                "files": {},
                "context": {},
                "variant": "intact" if "✨" in r["target"] else None,
            })
            e["games"].append(game)
            if game == "totk":
                e["section"] = r["section"]  # TotK mana si la categoria difereix
            e["compendium"][game] = r["number"]
            if r["master_number"] and not r["number"]:
                e["compendium"]["botw_master_mode"] = r["master_number"]
            e["files"][game] = r["file"]
            e["context"][game] = extracts.get(r["target"], {})

    # Imatges: prioritat TotK "Picture" (1280x720) > BotW (280x280) > TotK quadrada (168x168)
    print("🖼️  Cercant les imatges del compendi...")
    totk_files = all_images("TotK_Hyrule_Compendium")
    candidates = {}
    for e in entries.values():
        order = []
        if "totk" in e["files"]:
            pic = e["files"]["totk"].rsplit(".", 1)[0] + "_Picture.png"
            if pic in totk_files:
                order.append(pic)
        if "botw" in e["files"]:
            order.append(e["files"]["botw"])
        if "totk" in e["files"]:
            order.append(e["files"]["totk"])
        candidates[e["key"]] = order
    info = image_info([f for order in candidates.values() for f in order])
    for e in entries.values():
        chosen = next((f for f in candidates[e["key"]] if f in info), None)
        e["image_file"] = chosen
        e["image"] = info.get(chosen)
        e["category"] = SECTION_TO_CATEGORY[e["section"]]
        del e["files"]
    return list(entries.values())


# ------------------------------------------------------------ llista curada
SKIP_WORDS = ("Map", "Sprite", "Concept", "Icon", "Silhouette", "Logo", "Sticker", "Stamp", "Symbol", "Emblem")


def name_variants(title):
    variants = [title]
    for prefix in ("Princess ", "King ", "Divine Beast ", "The Legend of Zelda: "):
        if title.startswith(prefix):
            variants.append(title[len(prefix):])
    if title == "Rhoam Bosphoramus Hyrule":
        variants += ["King Rhoam", "Rhoam"]
    return variants


def score_file(f, base, category, games):
    stem = f.rsplit(".", 1)[0]
    game_prefix = stem.split("_", 1)[0]
    rest = stem.split("_", 1)[1] if "_" in stem else ""
    base_u = base.replace(" ", "_")
    if not (rest == base_u or rest.startswith(base_u + "_")):
        return None
    if any(w in stem for w in SKIP_WORDS):
        return None
    score = 10 if game_prefix.lower() == games[-1] else 5
    suffix = rest[len(base_u):]
    if category in ("personatges", "races"):
        if "Artwork" in suffix:
            score += 8
        elif "Render" in suffix:
            score += 7
        elif "Model" in suffix:
            score += 6
        else:
            score += 1
    else:  # llocs
        if suffix == "":
            score += 8
        elif re.fullmatch(r"_\d+", suffix) or "Exterior" in suffix or "Overview" in suffix:
            score += 6
        elif "Model" in suffix or "Interior" in suffix:
            score += 2
        else:
            score += 3
    return score


def intro_text(title):
    try:
        html = api({"action": "parse", "page": title, "prop": "text", "section": 0,
                    "disablelimitreport": 1, "redirects": 1})["parse"]["text"]
    except Exception:  # noqa: BLE001
        return ""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.select("style, sup, table, .reference, .mw-references-wrap"):
        tag.decompose()
    paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
    paragraphs = [re.sub(r"\s+", " ", p) for p in paragraphs if len(p) > 40]
    return " ".join(paragraphs)[:1500]


def build_curated():
    with open(CURATED_FILE, encoding="utf-8") as f:
        curated = json.load(f)
    entries = []
    for category, items in curated.items():
        if category.startswith("_"):
            continue
        print(f"📚 Llista curada: {category} ({len(items)})")
        titles = [x["wiki"] for x in items]
        resolved, pageimages = {}, {}
        for batch in chunks(titles, 50):
            r = api({"action": "query", "titles": "|".join(batch), "redirects": 1,
                     "prop": "pageimages", "piprop": "name"})
            redirects = {x["from"]: x["to"] for x in r["query"].get("redirects", [])}
            norm = {x["from"]: x["to"] for x in r["query"].get("normalized", [])}
            pages = {p["title"]: p for p in r["query"]["pages"]}
            for t in batch:
                final = redirects.get(norm.get(t, t), norm.get(t, t))
                p = pages.get(final, {})
                resolved[t] = None if p.get("missing") else final
                if p.get("pageimage"):
                    pageimages[t] = file_key(p["pageimage"])
        for item in items:
            title = resolved.get(item["wiki"])
            if not title:
                print(f"  ⚠️  Pàgina no trobada a la wiki: {item['wiki']}")
            cands = []
            if item.get("image"):
                cands = [(999, file_key(item["image"]))]
            elif category != "jocs":
                for base in name_variants(item["wiki"]):
                    for g in ("TotK", "BotW"):
                        for f in all_images(f"{g}_{base.replace(' ', '_')}"):
                            s = score_file(f, base, category, item["games"])
                            if s is not None:
                                cands.append((s, f))
            if item["wiki"] in pageimages:
                cands.append((0, pageimages[item["wiki"]]))
            cands = sorted(set(cands), key=lambda x: -x[0])
            info = image_info([f for _, f in cands[:6]]) if cands else {}
            chosen = next((f for _, f in cands if f in info), None)
            entries.append({
                "key": item["wiki"],
                "name_en": item["wiki"],
                "wiki": title or item["wiki"],
                "category": category,
                "games": item["games"],
                "compendium": {},
                "variant": None,
                "image_file": chosen,
                "image": info.get(chosen),
                "image_candidates": [f for _, f in cands[:6]],
                "context": {"intro": intro_text(title) if title else ""},
            })
            print(f"  {'✅' if chosen else '❌'} {item['wiki']}: {chosen}")
    return entries


# --------------------------------------------------------------------- main
def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    entries = build_compendium() + build_curated()

    # ids únics i estables
    seen = {}
    for e in entries:
        base = slugify(e["name_en"]) if not e.get("variant") else slugify(e["key"])
        if e["category"] in ("llocs", "jocs", "personatges", "races"):
            base = slugify(e["name_en"].replace("The Legend of Zelda: ", ""))
        slug, n = base, 2
        while slug in seen:
            slug, n = f"{base}-{n}", n + 1
        seen[slug] = True
        e["id"] = slug

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=1)
    missing = [e["id"] for e in entries if not e.get("image")]
    print(f"\n🎉 {len(entries)} entrades desades a {os.path.relpath(OUT_FILE, ROOT)}")
    print(f"   Sense imatge: {len(missing)} {missing[:30]}")


if __name__ == "__main__":
    main()
