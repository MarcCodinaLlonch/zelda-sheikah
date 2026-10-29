"""PAS 3 · Genera la base de dades final en català (zelda.json i zelda_data_ca.json).

- Agrupa les dades en les 10 categories oficials acordades:
  Jocs, Personatges, Caps, Enemics, Criatures, Materials, Equipament, Tresors, Llocs, Races.
- Reclassifica els caps principals i de masmorra a la categoria 'Caps'.
- Assigna descripcions elaborades en català (les seleccionades a mà per a personatges/races/llocs/jocs/caps,
  i una adaptació enriquida de l'extracte oficial del compendi per a la resta).
- Configura les URLs d'imatge locals a 'http://localhost:5000/static/img/<id>.webp'.
- Genera el fitxer 'zelda_data_ca.json' (compatibilitat total amb el frontend actual)
  i 'data/zelda.json' (format pla complet per als nous endpoints).

Ús:  venv/bin/python scripts/build_dataset.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from descriptions_curated import CURATED_DESCRIPTIONS  # noqa: E402
from descriptions_enemies import ENEMY_DESCRIPTIONS  # noqa: E402
from descriptions_creatures import CREATURE_DESCRIPTIONS  # noqa: E402
from descriptions_materials import MATERIAL_DESCRIPTIONS  # noqa: E402
from descriptions_equipment import EQUIPMENT_DESCRIPTIONS  # noqa: E402
from compendium_translations import translate_compendium_text  # noqa: E402
from names_translations import ITEM_NAME_TRANSLATIONS  # noqa: E402
from details_translations import translate_location, translate_drop, translate_property, translate_properties  # noqa: E402


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, "data", "raw", "sources.json")
OUT_JSON = os.path.join(ROOT, "data", "zelda.json")
LEGACY_CACHE = os.path.join(ROOT, "zelda_data_ca.json")

# Ids que s'han de classificar com a 'Caps'
BOSS_IDS = {
    # Grans caps d'història i temples
    "calamity-ganon", "dark-beast-ganon", "demon-king-ganondorf", "demon-dragon",
    "phantom-ganon", "thunderblight-ganon", "fireblight-ganon", "waterblight-ganon",
    "windblight-ganon", "monk-maz-koshia", "colgera", "moragia", "marbled-gohma",
    "sludge-like", "mucktorok", "queen-gibdo", "seized-construct",
    # Caps errants i minicaps
    "hinox", "blue-hinox", "black-hinox", "stalnox",
    "stone-talus", "stone-talus-luminous", "stone-talus-rare", "igneo-talus",
    "frost-talus", "igneo-talus-titan", "battle-talus",
    "molduga", "molduking",
    "flame-gleeok", "frost-gleeok", "thunder-gleeok", "king-gleeok",
    "frox", "obsidian-frox", "blue-white-frox",
    "flux-construct-i", "flux-construct-ii", "flux-construct-iii",
    "master-kohga",
}

CATEGORY_ORDER = [
    "jocs",
    "personatges",
    "races",
    "llocs",
    "caps",
    "enemics",
    "criatures",
    "materials",
    "equipament",
    "tresors",
]

CATEGORY_NAMES_CA = {
    "jocs": "Jocs",
    "personatges": "Personatges",
    "races": "Races",
    "llocs": "Llocs",
    "caps": "Caps",
    "enemics": "Enemics",
    "criatures": "Criatures",
    "materials": "Materials",
    "equipament": "Equipament",
    "tresors": "Tresors",
}

JOCS_ORDER = [
    "breath-of-the-wild", "the-master-trials", "the-champions-ballad", "tears-of-the-kingdom"
]

CHAR_ORDER = [
    "link", "princess-zelda", "ganondorf", "rhoam-bosphoramus-hyrule",
    "rauru", "sonia", "mineru",
    "mipha", "daruk", "urbosa", "revali",
    "sidon", "yunobo", "riju", "tulin",
    "impa", "purah", "robbie", "paya", "josha", "symin",
    "great-deku-tree", "great-fairy", "hestu", "kass", "beedle",
    "kilton", "koltin", "addison", "hudson", "bolson", "cece",
    "penn", "tauro", "calip", "buliara", "muzu", "bludo",
    "kaneli", "teba", "yona", "hoz", "king-dorephan", "pikango",
    "steward-construct"
]

RACE_ORDER = [
    "hylian", "sheikah", "goron", "zora", "gerudo", "rito", "korok", "zonai", "yiga-clan"
]

LLOCS_ORDER = [
    "hyrule-castle", "great-plateau", "great-sky-island", "depths", "hyrule-field",
    "temple-of-time", "forgotten-temple", "wind-temple", "fire-temple", "water-temple", "lightning-temple", "spirit-temple",
    "divine-beast-vah-ruta", "divine-beast-vah-rudania", "divine-beast-vah-medoh", "divine-beast-vah-naboris",
    "lookout-landing", "kakariko-village", "hateno-village", "goron-city", "zora-s-domain", "gerudo-town", "rito-village",
    "korok-forest", "tarrey-town", "lurelin-village", "kara-kara-bazaar",
    "death-mountain", "gerudo-desert", "hebra-mountains", "mount-lanayru", "satori-mountain", "lake-hylia", "eventide-island",
    "lost-woods", "typhlo-ruins",
    "ancient-shrine", "shrine-of-light", "shrine-of-resurrection", "lightroot", "skyview-tower", "sheikah-tower",
    "hateno-ancient-tech-lab", "akkala-ancient-tech-lab"
]

BOSS_ORDER = [
    "calamity-ganon", "dark-beast-ganon", "demon-king-ganondorf", "demon-dragon", "phantom-ganon",
    "windblight-ganon", "fireblight-ganon", "waterblight-ganon", "thunderblight-ganon", "monk-maz-koshia",
    "colgera", "moragia", "marbled-gohma", "mucktorok", "sludge-like", "queen-gibdo", "seized-construct", "master-kohga",
    "king-gleeok", "flame-gleeok", "frost-gleeok", "thunder-gleeok",
    "molduking", "molduga",
    "hinox", "blue-hinox", "black-hinox", "stalnox",
    "stone-talus", "stone-talus-luminous", "stone-talus-rare", "igneo-talus", "frost-talus", "igneo-talus-titan", "battle-talus",
    "frox", "obsidian-frox", "blue-white-frox",
    "flux-construct-i", "flux-construct-ii", "flux-construct-iii"
]

TREASURE_ORDER = [
    "treasure-chest", "ore-deposit", "rare-ore-deposit", "luminous-stone-deposit", "zonaite-deposit", "well"
]

EQUIP_PRIORITY = [
    "master-sword", "sword-of-the-hero", "white-sword-of-the-sky", "fierce-deity-sword",
    "biggoron-s-sword", "dusk-claymore", "one-hit-obliterator",
    # Hylian & Knights
    "traveler-s-sword", "traveler-s-sword-intact", "traveler-s-claymore", "traveler-s-claymore-intact",
    "traveler-s-spear", "traveler-s-spear-intact", "traveler-s-bow", "traveler-s-shield",
    "soldier-s-broadsword", "soldier-s-broadsword-intact", "soldier-s-claymore", "soldier-s-claymore-intact",
    "soldier-s-spear", "soldier-s-spear-intact", "soldier-s-bow", "soldier-s-shield",
    "knight-s-broadsword", "knight-s-broadsword-intact", "knight-s-claymore", "knight-s-claymore-intact",
    "knight-s-halberd", "knight-s-halberd-intact", "knight-s-bow", "knight-s-shield",
    "royal-broadsword", "royal-broadsword-intact", "royal-claymore", "royal-claymore-intact",
    "royal-halberd", "royal-halberd-intact", "royal-bow", "royal-shield",
    "royal-guard-s-sword", "royal-guard-s-sword-intact", "royal-guard-s-claymore", "royal-guard-s-claymore-intact",
    "royal-guard-s-spear", "royal-guard-s-spear-intact", "royal-guard-s-bow", "royal-guard-s-shield",
    # Shields
    "hylian-shield", "bow-of-light"
]

CREATURES_PRIORITY = [
    "lord-of-the-mountain", "patricia", "blupee", "bubbulfrog", "dondon", "cucco",
    "horse", "giant-horse", "white-horse", "giant-white-stallion", "golden-horse", "stalhorse"
]

MATERIALS_PRIORITY = [
    "apple", "golden-apple", "hearty-durian", "hydromelon", "spicy-pepper", "voltfruit",
    "fire-fruit", "ice-fruit", "shock-fruit", "splash-fruit", "dazzlefruit", "bomb-flower",
    "muddle-bud", "puffshroom", "silent-princess", "sundelion"
]


def sort_cat_items(cat, items):
    if cat == "jocs":
        return sorted(items, key=lambda x: JOCS_ORDER.index(x["id"]) if x["id"] in JOCS_ORDER else 999)
    if cat == "personatges":
        return sorted(items, key=lambda x: CHAR_ORDER.index(x["id"]) if x["id"] in CHAR_ORDER else 999)
    if cat == "races":
        return sorted(items, key=lambda x: RACE_ORDER.index(x["id"]) if x["id"] in RACE_ORDER else 999)
    if cat == "llocs":
        return sorted(items, key=lambda x: LLOCS_ORDER.index(x["id"]) if x["id"] in LLOCS_ORDER else 999)
    if cat == "caps":
        return sorted(items, key=lambda x: BOSS_ORDER.index(x["id"]) if x["id"] in BOSS_ORDER else 999)
    if cat == "tresors":
        return sorted(items, key=lambda x: TREASURE_ORDER.index(x["id"]) if x["id"] in TREASURE_ORDER else 999)
    if cat == "equipament":
        return sorted(items, key=lambda x: (0, EQUIP_PRIORITY.index(x["id"])) if x["id"] in EQUIP_PRIORITY else (1, ITEM_NAME_TRANSLATIONS.get(x["name_en"], x["name_en"])))
    if cat == "criatures":
        return sorted(items, key=lambda x: (0, CREATURES_PRIORITY.index(x["id"])) if x["id"] in CREATURES_PRIORITY else (1, ITEM_NAME_TRANSLATIONS.get(x["name_en"], x["name_en"])))
    if cat == "materials":
        return sorted(items, key=lambda x: (0, MATERIALS_PRIORITY.index(x["id"])) if x["id"] in MATERIALS_PRIORITY else (1, ITEM_NAME_TRANSLATIONS.get(x["name_en"], x["name_en"])))
    return sorted(items, key=lambda x: ITEM_NAME_TRANSLATIONS.get(x["name_en"], x["name_en"]))

def format_name(entry):
    base_name = entry["name_en"]
    # Obtenir la traducció al català del diccionari complet
    name = ITEM_NAME_TRANSLATIONS.get(base_name, base_name)

    # Si és una variant intacta de TotK
    if entry.get("variant") == "intact":
        if "✨" not in name:
            name = f"{name} ✨ (Impolut)"
    return name


# Vocabulari freqüent dels extractes oficials per traduir fluidament
TERM_REPLACEMENTS = [
    (r"\bThis common species is a nuisance all over Hyrule\b", "Aquesta espècie comuna és present per tot Hyrule"),
    (r"\bWhile not very clever, they are at least intelligent enough to\b", "Tot i no ser especialment astuts, tenen prou intel·ligència per"),
    (r"\bThey are sometimes seen marching in groups\b", "Sovint se'ls veu patrullant en grup"),
    (r"\bIf they come at you, watch out for their sharp horns!\b", "Si t'ataquen, vigila amb les seves banyes esmolades!"),
    (r"\bA common mushroom found near trees around Hyrule\b", "Un bolet comú que creix a prop dels troncs dels arbres arreu d'Hyrule"),
    (r"\bEat it to restore half a heart\b", "Es pot consumir cru per recuperar mig cor o cuinar en plats nutritius"),
    (r"\bThis prized fruit is said to have fallen from the heavens\b", "Aquesta fruita daurada és molt apreciada per les seves propietats"),
    (r"\bCommon Locations\b", "Localitzacions comunes"),
    (r"\bRecoverable Materials\b", "Materials que s'obtenen"),
    (r"\bCooking Effects\b", "Efectes en la cuina"),
    (r"\bHyrule Field\b", "Plana d'Hyrule"),
    (r"\bCentral Hyrule Depths\b", "Subsòl Central d'Hyrule"),
    (r"\bWest Necluda\b", "Necluda Occidental"),
    (r"\bEast Necluda\b", "Necluda Oriental"),
    (r"\bLanayru Great Spring\b", "Gran Manantial de Lanayru"),
    (r"\bGerudo Desert\b", "Desert Gerudo"),
    (r"\bGerudo Highlands\b", "Serralada Gerudo"),
    (r"\bHebra Mountains\b", "Muntanyes d'Hebra"),
    (r"\bEldin Canyon\b", "Canó d'Eldin"),
    (r"\bDeath Mountain\b", "Muntanya de la Mort"),
    (r"\bFaron Grasslands\b", "Praderies de Faron"),
    (r"\bTabantha Frontier\b", "Confins de Tabantha"),
    (r"\bAkkala Highlands\b", "Terres Altes d'Akkala"),
    (r"\bDeep Akkala\b", "Akkala Profunda"),
    (r"\bGreat Sky Island\b", "Gran Illa Celeste"),
    (r"\bSky Islands\b", "Illes Celestes"),
    (r"\bDepths\b", "El Subsòl"),
]


def adapt_compendium_text(text):
    if not text:
        return ""
    out = text
    for pattern, repl in TERM_REPLACEMENTS:
        out = re.sub(pattern, repl, out, flags=re.IGNORECASE)

    # Traduccions generals de termes de joc
    substitutions = [
        ("restore half a heart", "recuperar mig cor"),
        ("restore hearts", "recuperar cors"),
        ("increases attack power", "augmenta la potència d'atac"),
        ("increases defense", "augmenta la defensa"),
        ("increases stealth", "millora el sigil"),
        ("increases movement speed", "augmenta la velocitat de moviment"),
        ("resists cold", "atorga resistència al fred"),
        ("resists heat", "atorga resistència a la calor"),
        ("resists electricity", "atorga aïllament elèctric"),
        ("gives shock resistance", "atorga resistència a les descàrregues"),
        ("restores stamina", "recupera energia de resistència"),
        ("gives temporary stamina", "atorga resistència addicional temporal"),
        ("glow in the dark", "brillar en la foscor"),
        ("in the Depths", "al Subsòl"),
        ("in caves", "a les coves"),
        ("around trees", "al voltant dels arbres"),
        ("near water", "a prop de l'aigua"),
        ("in high altitudes", "a gran altitud"),
        ("found all over Hyrule", "present a tot el regne d'Hyrule"),
        ("found primarily in", "localitzat principalment a"),
        ("crafted by the ancient", "forjat pels antics"),
        ("wielded by", "empunyat per"),
        ("carried by", "portat per"),
    ]
    for en, ca in substitutions:
        out = re.sub(re.escape(en), ca, out, flags=re.IGNORECASE)
    return out.strip()


def build_description(entry):
    slug = entry["id"]
    clean_slug = slug.replace("-intact", "").replace("-2", "")

    # 1. Si és un enemic i té descripció elaborada a mida
    if slug in ENEMY_DESCRIPTIONS:
        return ENEMY_DESCRIPTIONS[slug]
    if clean_slug in ENEMY_DESCRIPTIONS:
        return ENEMY_DESCRIPTIONS[clean_slug]

    # 2. Si tenim una descripció curada a mida (personatges, races, llocs, jocs, caps, tresors)
    candidates = [
        slug,
        f"the-legend-of-zelda-{slug}",
        clean_slug,
        f"the-legend-of-zelda-{clean_slug}"
    ]
    for c in candidates:
        if c in CURATED_DESCRIPTIONS:
            desc = CURATED_DESCRIPTIONS[c]
            if entry.get("variant") == "intact":
                desc += " Aquesta versió impoluta recuperada del Subsòl conserva la puresa del metall i no ha estat corrompuda pel Fang."
            return desc

    # 3. Criatures
    if slug in CREATURE_DESCRIPTIONS:
        return CREATURE_DESCRIPTIONS[slug]
    if clean_slug in CREATURE_DESCRIPTIONS:
        return CREATURE_DESCRIPTIONS[clean_slug]

    # 4. Materials
    if slug in MATERIAL_DESCRIPTIONS:
        return MATERIAL_DESCRIPTIONS[slug]
    if clean_slug in MATERIAL_DESCRIPTIONS:
        return MATERIAL_DESCRIPTIONS[clean_slug]

    # 5. Equipament
    if slug in EQUIPMENT_DESCRIPTIONS:
        desc = EQUIPMENT_DESCRIPTIONS[slug]
        if entry.get("variant") == "intact":
            desc += " Aquesta versió impoluta recuperada del Subsòl conserva tota la puresa del metall i no ha estat degradada pel Fang."
        return desc
    if clean_slug in EQUIPMENT_DESCRIPTIONS:
        desc = EQUIPMENT_DESCRIPTIONS[clean_slug]
        if entry.get("variant") == "intact":
            desc += " Aquesta versió impoluta recuperada del Subsòl conserva tota la puresa del metall i no ha estat degradada pel Fang."
        return desc

    cat_ca = CATEGORY_NAMES_CA.get(entry.get("category"), "Hyrule")
    return f"Element oficial de la categoria {cat_ca} registrat a l'univers de Zelda."


def main():
    with open(SOURCES, encoding="utf-8") as f:
        sources = json.load(f)

    # Evitem el duplicat de master-kohga-2
    sources = [e for e in sources if e["id"] != "master-kohga-2"]

    # 1. Agrupar fonts per categoria
    by_category_raw = {c: [] for c in CATEGORY_ORDER}
    for entry in sources:
        e_id = entry["id"]
        category_key = entry["category"]
        if e_id in BOSS_IDS or entry["name_en"] in BOSS_IDS:
            category_key = "caps"
        by_category_raw[category_key].append(entry)

    processed = []
    by_category = {CATEGORY_NAMES_CA[cat]: [] for cat in CATEGORY_ORDER}

    card_id = 1
    for cat_key in CATEGORY_ORDER:
        cat_ca = CATEGORY_NAMES_CA[cat_key]
        sorted_entries = sort_cat_items(cat_key, by_category_raw[cat_key])

        for entry in sorted_entries:
            e_id = entry["id"]
            card_number = f"{card_id:03d}"
            name_ca = format_name(entry)
            description_ca = build_description(entry)

            # Imatge local a Flask (WebP quadrat 512x512)
            if e_id == "princess-zelda":
                image_url = f"http://localhost:5000/static/img/{e_id}-v2.webp"
            else:
                image_url = f"http://localhost:5000/static/img/{e_id}.webp"

            # Detalls en català
            raw_locs = entry.get("context", {}).get("totk", {}).get("locations") or entry.get("context", {}).get("botw", {}).get("locations") or []
            raw_drops = entry.get("context", {}).get("totk", {}).get("drops") or entry.get("context", {}).get("botw", {}).get("drops") or []
            raw_props = entry.get("context", {}).get("totk", {}).get("properties") or entry.get("context", {}).get("botw", {}).get("properties") or []

            clean_locs = [translate_location(loc) for loc in raw_locs if loc]
            clean_drops = [translate_drop(d) for d in raw_drops if d]
            clean_props = translate_properties(raw_props)

            item = {
                "id": card_id,
                "card_number": card_number,
                "compendium_number": card_number,
                "slug": e_id,
                "name": name_ca,
                "name_en": entry["name_en"],
                "category": cat_ca,
                "category_key": cat_key,
                "variant": entry.get("variant"),
                "description": description_ca,
                "image": image_url,
                "games": [g.upper() for g in entry.get("games", [])],
                "details": {
                    "locations": clean_locs,
                    "drops": clean_drops,
                    "properties": clean_props,
                }
            }

            # Item per al fitxer de compatibilitat del frontend
            legacy_item = {
                "id": card_id,
                "card_number": card_number,
                "compendium_number": card_number,
                "slug": e_id,
                "name": name_ca,
                "name_en": entry["name_en"],
                "category": cat_ca,
                "description": description_ca,
                "image": image_url,
                "games": [g.upper() for g in entry.get("games", [])],
                "details": {
                    "locations": clean_locs,
                    "drops": clean_drops,
                    "properties": clean_props,
                }
            }

            processed.append(item)
            by_category[cat_ca].append(legacy_item)
            card_id += 1

    # Eliminar categories que hagin quedat buides si n'hi hagués
    by_category = {k: v for k, v in by_category.items() if len(v) > 0}

    # Desar fitxer REST pla (data/zelda.json)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(processed, f, ensure_ascii=False, indent=2)

    # Desar fitxer agrupat (zelda_data_ca.json) per compatibilitat amb el frontend actual
    with open(LEGACY_CACHE, "w", encoding="utf-8") as f:
        json.dump(by_category, f, ensure_ascii=False, indent=2)

    print(f"🎉 Generat data/zelda.json amb {len(processed)} elements numerats (#001 a #{card_id - 1:03d})!")
    print(f"🎉 Generat zelda_data_ca.json amb {len(by_category)} categories:")
    for cat, items in by_category.items():
        start_id = items[0]["card_number"]
        end_id = items[-1]["card_number"]
        print(f"   - {cat} ({len(items)} elements): #{start_id} a #{end_id}")


if __name__ == "__main__":
    main()
