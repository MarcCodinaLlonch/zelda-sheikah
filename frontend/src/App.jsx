import { useState, useEffect } from 'react';
import './App.css';
import Header from './components/Header.jsx';
import Footer from './components/Footer.jsx';
import List from './components/List.jsx'
import Modal from './components/Modal.jsx';


function getCookie(name) {
  const cookies = document.cookie.split("; ");
  const cookie = cookies.find((item)=>
    item.startsWith(name+"=")
  );

  if (!cookie) return null;

  return decodeURIComponent(
    cookie.substring(name.length +1)
  )
}

function setCookie(name, value){
  document.cookie = `${name}=${encodeURIComponent(value)}; path=/; max-age=10000; SameSite=Lax`;
}

function App() {
  const [elements, setElements] = useState ([]);

  const [activeCategory, setActiveCategories] = useState(() => {
    return getCookie("category") || "Totes";
  })

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Guarda l'element que l'usuari ha obert al detall. Si és null, la finestra està tancada.
  const [selectedElement, setSelectedElement] = useState(null);

  useEffect(() => {
    async function loadelements() {
      try {
        const response = await fetch("http://localhost:5000/api/zelda-custom")

        if (!response.ok) {
          throw new Error("Error carregant les dades de Zelda.")
        }

        const result = await response.json();

        // Com que l'API de Flask ens retorna un objecte on cada clau és una categoria (games, characters, monsters...),
        // fem servir Object.values() per extreure els arrays de cada categoria i .flat() per aplanar-ho tot en una sola llista.
        // Així tenim un únic array pla amb tots els elements per poder fer servir .map() i .filter() com a classe.
        const allElements = Object.values(result.data).flat();
        setElements(allElements);

      } catch (err) {
        setError("No s'han pogut carregar les dades de Zelda");
        console.error(err)

      } finally {
        setLoading(false);
      }

    }

    loadelements();

  }, []);

  useEffect(() => {
    setCookie("category", activeCategory);
  }, [activeCategory])

  const categories = [
    "Totes",
    ...new Set(elements.map((element) => element.category))
  ];

  const visibleelements = elements.filter((element) => {
    if (activeCategory === 'Totes') {
      return true;
    }

    return element.category === activeCategory;
  })

  return (
    <div className='contenidorApp'>
      <main className='principalApp'>
        {/* Només disseny: la capçalera viu dins la pantalla de la tauleta i substitueix el títol duplicat */}
        <Header />

        <section className='panellFiltre'>
          <label htmlFor='filtre-categoria' className='etiquetaFiltre'>
            Filtre per categoria
          </label>
          <div className='embolcallSelect'>
            <select
              id='filtre-categoria'
              className='selectCategoria'
              value={activeCategory}
              onChange={(e) => setActiveCategories(e.target.value)}
            >
              {categories.map((category) => (
                <option key={category} value={category}>
                  {category}
                </option>
              ))}
            </select>
          </div>
        </section>

        {loading && (
          <div className='missatgeEstat carregant'>
            <span className='puntLlum'></span>
            <p>Carregant dades de la Tauleta Sheikah...</p>
          </div>
        )}

        {error && (
          <div className='missatgeEstat error'>
            <p>{error}</p>
          </div>
        )}

        {!loading && !error && (
          <List
            title="Elements d'Hyrule"
            elements={visibleelements}
            onSelect={setSelectedElement}
          />
        )}
      </main>

      <Footer />

      {/* Si hi ha un element seleccionat, mostrem la finestra de detall a sobre de la pantalla */}
      {selectedElement && (
        <Modal element={selectedElement} onClose={() => setSelectedElement(null)} />
      )}
    </div>
  );
}

export default App