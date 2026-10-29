# ⚔️ The Legend of Zelda · Compendi d'Hyrule (Tauleta Sheikah)

> **Projecte Full-Stack (Frontend React + Backend Flask)**  
> *Inspirat en la interfície de la Tauleta Sheikah de The Legend of Zelda: Breath of the Wild i Tears of the Kingdom.*

---

## 📖 Descripció del Projecte

Aquesta aplicació web és una reproducció funcional del **Compendi d'Hyrule (Hyrule Compendium)** que en Link consulta a través de la seva **Tauleta Sheikah**. 

El projecte s'ha desenvolupat amb una arquitectura **Full-Stack desacoblada**:
* **Frontend:** Aplicació moderna en **React 19** muntada amb **Vite**, amb una interfície d'usuari (UI/UX) totalment personalitzada que emula el xassís de pedra, les cantoneres de bronze, els circuits luminescents cian i la tipografia antiga d'Hyrule.
* **Backend:** API REST pròpia desenvolupada en **Python (Flask)** que cataloga més de **700 elements en català** (Criatures, Enemics, Caps, Materials, Equipament, etc.) i en serveix les imatges optimitzades en format WebP.

---

## ✨ Característiques Principals

* 📱 **Disseny Tauleta Sheikah (UI/UX Sheikah Slate):**
  * Xassís exterior de pedra tallada amb conductes d'energia i nodes de llum cian.
  * Pantalla de vidre encastada amb quadrícula d'escaneig hologràfica.
  * Tipografia temàtica oficial: **Cinzel** (gravat èpic) i **Rajdhani** (HUD tecnològic).
* 🔍 **Filtre per Categories amb Persistència:**
  * Selector integrat d'estil consola Sheikah per filtrar entre 10 categories (Criatures, Enemics, Caps, Materials, Equipament...).
  * Persistència de l'última categoria seleccionada mitjançant **Cookies**.
* 🎯 **Visor d'Escàner de Càmera Sheikah:**
  * Targetes interactives amb les 4 cantoneres d'enfocament (`⌜ ⌝ ⌞ ⌟`), número de registre oficial del Compendi (`Nº 001`) i fotos en tractament hologràfic.
* 🔎 **Finestra de Detall (Modal interactiu Sheikah):**
  * Permet ampliar qualsevol fitxa amb un sol clic sense canviar de pestanya.
  * Mostra la imatge gran, la descripció sencera, el nom en anglès, les etiquetes del joc (`BOTW` / `TOTK`), i seccions dinàmiques de **Llocs**, **Botí** i **Propietats**.
* ⚡ **Rendiment:** Càrrega mandrosa (*lazy loading*) de les imatges per a una navegació ultra fluida.

---

## 🛠️ Tecnologies Utilitzades

| Àmbit | Tecnologia | Utilitat |
| :--- | :--- | :--- |
| **Frontend** | **React 19** | Llibreria per a la interfície d'usuari per components |
| **Build Tool** | **Vite** | Entorn de desenvolupament ràpid i empaquetador |
| **Estils** | **CSS3 Modern** | Variables CSS (Design Tokens), Flexbox, CSS Grid, `clip-path` |
| **Backend** | **Python 3 & Flask** | Servidor API RESTful |
| **CORS** | **Flask-CORS** | Gestió de capçaleres per a comunicació segura entre Front i Back |
| **Dades** | **JSON & WebP** | Catàleg normalitzat en català i imatges optimitzades |

---

## 📂 Estructura del Repositori

```text
zelda-sheikah/
├── frontend/                     # Aplicació React (Client)
│   ├── public/                   # Icones i assets estàtics
│   ├── src/
│   │   ├── components/           # Components React (Header, List, Card, Modal, Footer)
│   │   ├── App.jsx               # Lògica principal, estats i fetch
│   │   ├── App.css               # Xassís Sheikah i pantalla
│   │   ├── index.css             # Design Tokens i variables de color
│   │   └── main.jsx              # Punt d'entrada de React
│   ├── index.html                # Fonts de Google (Cinzel, Rajdhani)
│   ├── package.json              # Dependències de Node.js
│   └── vite.config.js
│
├── backend/                      # Servidor API Flask (Server)
│   ├── data/
│   │   └── zelda.json            # Base de dades catalogada en català
│   ├── static/
│   │   └── img/                  # Imatges WebP optimitzades de cada element
│   ├── app.py                    # Rutes de l'API Flask (/api/zelda-custom, /api/elements...)
│   └── requirements.txt          # Dependències de Python (Flask, Flask-CORS...)
│
├── .gitignore                    # Ignora node_modules, venv, pycache, etc.
└── README.md                     # Documentació del projecte
```

---

## 🚀 Com Arrencar el Projecte (Quick Start)

### 1. Clonar el repositori
```bash
git clone https://github.com/<el-teu-usuari>/zelda-sheikah.git
cd zelda-sheikah
```

---

### 2. Arrencar el Backend (Python Flask)

Obre una terminal i executa:

```bash
cd backend

# Crear l'entorn virtual
python3 -m venv venv

# Activar l'entorn virtual
# A Linux / macOS:
source venv/bin/activate
# A Windows (PowerShell):
# .\venv\Scripts\Activate.ps1

# Instal·lar les dependències
pip install -r requirements.txt

# Executar el servidor Flask
python app.py
```
> El servidor s'iniciarà a: `http://localhost:5000`

---

### 3. Arrencar el Frontend (React + Vite)

Obre una **segona terminal** i executa:

```bash
cd frontend

# Instal·lar les dependències de Node.js
npm install

# Arrencar el servidor de desenvolupament
npm run dev
```
> Obre el navegador a: `http://localhost:5173`

---

## 👤 Autor

* **Marc Codina Llonch**  
* Cicle Formatiu de Grau Superior en **Desenvolupament d'Aplicacions Multiplataforma (DAM)**  
* Universitat de Vic (UVic-UCC)
