# Zelda API · Enciclopèdia d'Hyrule (BotW + TotK)

API REST pròpia en **català** desenvolupada amb **Flask** per a l'assignatura de Desenvolupament d'Aplicacions Web.
Cobreix la totalitat de l'univers de **The Legend of Zelda: Breath of the Wild** i **Tears of the Kingdom** (729 elements verificats).

---

## 🚀 Característiques

1. **Dades 100% pròpies i locals**:
   - Cap dependència externa de proxies o APIs caigudes.
   - 729 elements organitzats en **10 categories clau**.
2. **Imatges homogènies i estables**:
   - Totes les 729 imatges han estat descarregades i normalitzades a **WebP 512×512 píxels**.
   - Fons transparents per a personatges i elements, o adaptats per a fotografies/captures del compendi.
   - Es serveixen directament des de `/static/img/<id>.webp`.
3. **Descripcions en català**:
   - Redactades amb fidelitat al lore i als detalls oficials d'Hyrule.
   - Informació d'ubicació, propietats i materials.
4. **Arquitectura modular (ETL separat del servei)**:
   - `scripts/fetch_sources.py`: Extracció de dades oficials de la wiki.
   - `scripts/build_images.py`: Descàrrega i normalització multithread d'imatges a WebP.
   - `scripts/build_dataset.py`: Generació del dataset en català.
   - `app.py`: Servidor Flask ultra-ràpid, sense càrregues lentes en calent.

---

## 📂 Categories disponibles

| Categoria | Nre. Elements | Descripció |
|---|---|---|
| **Personatges** | 45 | Link, Princesa Zelda, Ganondorf, Savis, Campions, Impa, Purah... |
| **Caps** | 41 | Calamity Ganon, Demon King Ganondorf, Gleeoks, Hinox, Talus, Temples... |
| **Enemics** | 94 | Bokoblins, Moblins, Lizalfos, Guardians, Gòlems Zonai, Lynels... |
| **Criatures** | 95 | Cavalls, fauna salvatge, ocells, peixos, fades... |
| **Materials** | 127 | Bolets, fruites, minerals, ingredients de cuina i banyes... |
| **Equipament** | 264 | Master Sword, armes ancestrals, escuts, arcs, variants impolutes... |
| **Tresors** | 6 | Cofres del tresor, jaciments de mineral... |
| **Llocs** | 44 | Castell d'Hyrule, Temples, Illa Inicial, Subsol, Pobles, Torres... |
| **Races** | 9 | Hylians, Gorons, Zores, Gerudo, Rito, Sheikah, Koroks, Zonai, Clan Yiga |
| **Jocs** | 4 | Breath of the Wild, The Master Trials, The Champions' Ballad, Tears of the Kingdom |

**Total:** 729 elements

---

## 🛠️ Com engegar el servidor

1. Activa l'entorn virtual:
   ```bash
   source venv/bin/activate
   ```

2. Executa l'aplicació Flask:
   ```bash
   python app.py
   ```
   El servidor estarà escoltant a `http://localhost:5000`.

---

## 📡 Endpoints de la API

| Mètode | Ruta | Descripció |
|---|---|---|
| `GET` | `/api/zelda-custom` | **Compatibilitat frontend**: Retorna totes les dades agrupades per categoria |
| `GET` | `/api/categories` | Llista de categories amb recompte d'elements |
| `GET` | `/api/elements` | Llista plana d'elements (suporta `?category=`, `?search=`, `?game=`, `?page=`, `?limit=`) |
| `GET` | `/api/elements/<id>` | Detall complet d'un element per slug (ex: `/api/elements/link`) |
| `GET` | `/static/img/<id>.webp` | Imatge 512×512 WebP de l'element |
