"""PAS 2 · Descarrega i NORMALITZA totes les imatges.

Per a cada entrada de `data/raw/sources.json`:
  1. Descarrega la imatge original de la wiki (es guarda a `data/raw/images/`, memòria cau).
  2. La converteix a un format homogeni: **WebP quadrat de 512x512**.
       - Imatges amb fons transparent (artworks/renders): es retallen les vores buides
         i es centren amb un marge uniforme sobre fons transparent.
       - Fotografies/captures (compendi, llocs): retall quadrat centrat.
       - Imatges molt verticals (caràtules): s'encaixen sobre un fons desenfocat.
  3. La desa a `static/img/<id>.webp`, que és el que serveix Flask.

Ús:  venv/bin/python scripts/build_images.py            (només les que falten)
     venv/bin/python scripts/build_images.py --force    (les regenera totes)
     venv/bin/python scripts/build_images.py --only link,bokoblin
"""
import argparse
import concurrent.futures
import io
import json
import os
import sys

from PIL import Image, ImageFilter, ImageOps

sys.path.insert(0, os.path.dirname(__file__))
from wiki import download  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, "data", "raw", "sources.json")
CACHE_DIR = os.path.join(ROOT, "data", "raw", "images")
OUT_DIR = os.path.join(ROOT, "static", "img")

SIZE = 512          # mida final (px)
INNER = 448         # mida màxima del subjecte en imatges transparents (deixa marge)
QUALITY = 85


def has_transparency(img):
    if img.mode != "RGBA":
        return False
    alpha = img.getchannel("A")
    hist = alpha.histogram()
    transparent = sum(hist[:16])
    return transparent / (img.width * img.height) > 0.05


def normalize(raw_bytes):
    img = Image.open(io.BytesIO(raw_bytes))
    img = ImageOps.exif_transpose(img)
    if getattr(img, "is_animated", False):
        img.seek(0)
    img = img.convert("RGBA")

    if has_transparency(img):
        bbox = img.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
        if bbox:
            img = img.crop(bbox)
        img.thumbnail((INNER, INNER), Image.LANCZOS) if max(img.size) > INNER else None
        if max(img.size) < INNER:  # amplia imatges petites perquè totes tinguin el mateix pes visual
            ratio = INNER / max(img.size)
            img = img.resize((round(img.width * ratio), round(img.height * ratio)), Image.LANCZOS)
        canvas = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
        canvas.paste(img, ((SIZE - img.width) // 2, (SIZE - img.height) // 2), img)
        return canvas, "transparent"

    img = img.convert("RGB")
    w, h = img.size
    if w / h < 0.8:  # molt vertical (p. ex. caràtula): encaixar sobre fons desenfocat
        bg = ImageOps.fit(img, (SIZE, SIZE), Image.LANCZOS).filter(ImageFilter.GaussianBlur(24))
        fg = img.copy()
        fg.thumbnail((SIZE, SIZE), Image.LANCZOS)
        if max(fg.size) < SIZE:
            ratio = SIZE / max(fg.size)
            fg = fg.resize((round(fg.width * ratio), round(fg.height * ratio)), Image.LANCZOS)
        bg.paste(fg, ((SIZE - fg.width) // 2, (SIZE - fg.height) // 2))
        return bg, "fit"
    return ImageOps.fit(img, (SIZE, SIZE), Image.LANCZOS, centering=(0.5, 0.5)), "crop"


def process_entry(entry, force=False):
    out_path = os.path.join(OUT_DIR, f"{entry['id']}.webp")
    if not entry.get("image"):
        return entry["id"], "missing_source"
    if os.path.exists(out_path) and not force:
        return entry["id"], "skipped"

    url = entry["image"]["url"]
    ext = os.path.splitext(url)[1].lower() or ".png"
    cache_path = os.path.join(CACHE_DIR, f"{entry['id']}{ext}")

    try:
        if os.path.exists(cache_path) and not force:
            with open(cache_path, "rb") as f:
                raw = f.read()
        else:
            raw = download(url)
            with open(cache_path, "wb") as f:
                f.write(raw)

        img, mode = normalize(raw)
        img.save(out_path, "WEBP", quality=QUALITY, method=6)
        return entry["id"], mode
    except Exception as ex:  # noqa: BLE001
        return entry["id"], f"error: {ex}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--only", default="")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    only = {x.strip() for x in args.only.split(",") if x.strip()}

    os.makedirs(CACHE_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(SOURCES, encoding="utf-8") as f:
        entries = json.load(f)

    if only:
        entries = [e for e in entries if e["id"] in only]

    total = len(entries)
    done = failed = skipped = 0

    print(f"🚀 Iniciant processament de {total} imatges amb {args.workers} fils...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_entry, e, args.force): e for e in entries}
        for idx, fut in enumerate(concurrent.futures.as_completed(futures), 1):
            e_id, status = fut.result()
            if status == "skipped":
                skipped += 1
            elif status.startswith("error") or status == "missing_source":
                failed += 1
                print(f"  ❌ [{idx}/{total}] {e_id}: {status}")
            else:
                done += 1
                if idx % 25 == 0 or idx == total:
                    print(f"  ✅ [{idx}/{total}] Processades ({done} noves, {skipped} omeses)")

    print(f"\n🎉 Imatges acabades: {done} generades noves · {skipped} omeses · {failed} errors")


if __name__ == "__main__":
    main()
