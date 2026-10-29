"""Client mínim i educat per a l'API MediaWiki de zeldawiki.wiki.

- Reintents automàtics (la xarxa/DNS pot fallar puntualment).
- Petita pausa entre peticions per no sobrecarregar la wiki.
"""
import time

import requests

API_URL = "https://zeldawiki.wiki/w/api.php"
HEADERS = {"User-Agent": "ZeldaClassProject/2.0 (projecte educatiu; Flask API)"}
DELAY = 0.3  # segons entre peticions

_session = requests.Session()
_session.headers.update(HEADERS)


def api(params, retries=6):
    """Fa una petició GET a l'API de la wiki i retorna el JSON."""
    params = {**params, "format": "json", "formatversion": 2}
    last_error = None
    for attempt in range(retries):
        try:
            time.sleep(DELAY)
            r = _session.get(API_URL, params=params, timeout=40)
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa: BLE001
            last_error = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"La wiki no respon després de {retries} intents: {last_error}")


def download(url, retries=6):
    """Descarrega un fitxer binari (imatge) amb reintents."""
    last_error = None
    for attempt in range(retries):
        try:
            time.sleep(DELAY)
            r = _session.get(url, timeout=60)
            r.raise_for_status()
            return r.content
        except Exception as e:  # noqa: BLE001
            last_error = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"No s'ha pogut descarregar {url}: {last_error}")


def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]
