"""API REST pròpia de The Legend of Zelda en català (Breath of the Wild + Tears of the Kingdom).

Endpoints disponibles:
  - GET /api/zelda-custom                     -> Format agrupat per categoria (compatibilitat frontend)
  - GET /api/categories                       -> Llista de categories amb recompte d'elements
  - GET /api/elements                         -> Llista completa plana amb filtres (?category=, ?search=, ?game=, ?page=, ?limit=)
  - GET /api/elements/<id>                    -> Detall complet d'un element per slug
  - GET /static/img/<fitxer>.webp             -> Servei d'imatges normalitzades 512x512

Totes les dades i imatges es serveixen localment des del mateix servidor.
"""
import json
import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(ROOT, "data", "zelda.json")
LEGACY_FILE = os.path.join(ROOT, "zelda_data_ca.json")
STATIC_IMG_DIR = os.path.join(ROOT, "static", "img")

app = Flask(__name__, static_folder="static")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
CORS(app)


@app.after_request
def add_no_cache_headers(response):
    if request.path.startswith("/static/"):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response


def load_dataset():
    """Carrega la llista completa d'elements."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def load_legacy_dataset():
    """Carrega el format agrupat per categories per a compatibilitat."""
    if os.path.exists(LEGACY_FILE):
        with open(LEGACY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # Si no existeix el legacy, l'agrupem dinàmicament
    flat = load_dataset()
    grouped = {}
    for item in flat:
        cat = item["category"]
        grouped.setdefault(cat, []).append({
            "id": item["id"],
            "name": item["name"],
            "category": cat,
            "description": item["description"],
            "image": item["image"]
        })
    return grouped


# Cache en memòria amb comprovació de mtime
_dataset_cache = {"mtime": 0, "elements": [], "legacy": {}}


def get_data():
    """Retorna els elements i el format legacy sempre sincronitzats amb el disc."""
    current_mtime = os.path.getmtime(DATA_FILE) if os.path.exists(DATA_FILE) else 0
    if current_mtime != _dataset_cache["mtime"]:
        _dataset_cache["elements"] = load_dataset()
        _dataset_cache["legacy"] = load_legacy_dataset()
        _dataset_cache["mtime"] = current_mtime
    return _dataset_cache["elements"], _dataset_cache["legacy"]



@app.route("/static/img/<path:filename>")
def serve_image(filename):
    """Serveix imatges WebP normalitzades amb capçaleres de memòria cau."""
    response = send_from_directory(STATIC_IMG_DIR, filename)
    response.headers["Cache-Control"] = "public, max-age=86400"
    return response


@app.route("/api/zelda-custom", methods=["GET"])
def get_custom_zelda_api():
    """Endpoint de compatibilitat directa amb el frontend React original.

    Retorna totes les dades agrupades per les 10 categories en català.
    """
    elements, legacy_data = get_data()
    return jsonify({
        "status": "success",
        "message": "API de Zelda en català amb imatges verificades (BotW + TotK)",
        "total_elements": len(elements),
        "data": legacy_data
    })


@app.route("/api/categories", methods=["GET"])
def get_categories():
    """Retorna la llista de categories disponibles amb el nombre d'elements."""
    elements, _ = get_data()
    counts = {}
    for item in elements:
        cat = item["category"]
        counts[cat] = counts.get(cat, 0) + 1

    categories = [
        {"category": cat, "count": count}
        for cat, count in counts.items()
    ]
    return jsonify({
        "status": "success",
        "total_categories": len(categories),
        "data": categories
    })


@app.route("/api/elements", methods=["GET"])
def get_elements():
    """Llista d'elements filtrable i paginable.

    Paràmetres query opcionals:
      - category: nom de categoria (ex: 'Personatges', 'Caps', 'Enemics'...)
      - search: text a cercar en el nom o descripció
      - game: 'BOTW' o 'TOTK'
      - page: número de pàgina (per defecte: 1)
      - limit: elements per pàgina (per defecte: 50; 0 o 'all' per a tots)
    """
    elements, _ = get_data()
    category = request.args.get("category", "").strip().lower()
    search = request.args.get("search", "").strip().lower()
    game = request.args.get("game", "").strip().upper()
    page = request.args.get("page", default=1, type=int)
    limit_arg = request.args.get("limit", default="50").strip().lower()

    filtered = elements

    if category and category != "totes":
        filtered = [
            item for item in filtered
            if item["category"].lower() == category or item.get("category_key", "").lower() == category
        ]

    if search:
        filtered = [
            item for item in filtered
            if search in item["name"].lower()
            or search in item.get("name_en", "").lower()
            or search in item["description"].lower()
            or search == str(item.get("id"))
            or search == item.get("card_number")
            or search in item.get("slug", "").lower()
        ]

    if game:
        filtered = [
            item for item in filtered
            if game in item.get("games", [])
        ]

    total = len(filtered)

    # Paginació
    if limit_arg in ("0", "all", "none"):
        results = filtered
        limit = total
    else:
        try:
            limit = max(1, int(limit_arg))
        except ValueError:
            limit = 50

        start = (max(1, page) - 1) * limit
        end = start + limit
        results = filtered[start:end]

    return jsonify({
        "status": "success",
        "total": total,
        "page": page if limit_arg not in ("0", "all", "none") else 1,
        "limit": limit,
        "data": results
    })


@app.route("/api/elements/<item_id>", methods=["GET"])
def get_element_by_id(item_id):
    """Retorna un element concret a partir del seu número ID, card_number o slug."""
    elements, _ = get_data()
    item_id_str = item_id.strip()
    item_id_lower = item_id_str.lower()

    try:
        item_id_int = int(item_id_str)
    except ValueError:
        item_id_int = None

    for item in elements:
        if item_id_int is not None and item.get("id") == item_id_int:
            return jsonify({
                "status": "success",
                "data": item
            })
        if item.get("card_number") == item_id_str or str(item.get("id")) == item_id_str:
            return jsonify({
                "status": "success",
                "data": item
            })
        if item.get("slug") == item_id_lower:
            return jsonify({
                "status": "success",
                "data": item
            })

    return jsonify({
        "status": "error",
        "message": f"Element '{item_id}' no trobat a l'enciclopèdia d'Hyrule."
    }), 404


@app.route("/", methods=["GET"])
def index():
    """Pàgina d'índex que descriu l'API."""
    elements, _ = get_data()
    return jsonify({
        "name": "Hyrule Codex API",
        "version": "2.0",
        "description": "API pròpia de The Legend of Zelda (Breath of the Wild + Tears of the Kingdom) en català",
        "total_elements": len(elements),
        "endpoints": {
            "legacy": "/api/zelda-custom",
            "categories": "/api/categories",
            "elements": "/api/elements",
            "element_detail": "/api/elements/<id>"
        }
    })


if __name__ == "__main__":
    elements, _ = get_data()
    print("⚔️ Servidor Flask d'Hyrule en marxa a http://localhost:5000")
    print(f"   Carregats {len(elements)} elements verificats en català.")
    app.run(port=5000, debug=True)