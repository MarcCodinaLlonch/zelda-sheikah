import './Modal.css';

function Modal({ element, onClose }) {
  const compendiumNumber = String(element.card_number || element.compendium_number || element.id).padStart(3, '0');

  // Les llistes de details poden venir buides: només mostrarem les seccions que tinguin dades
  const locations = element.details?.locations || [];
  const drops = element.details?.drops || [];
  const properties = element.details?.properties || [];
  const games = element.games || [];

  return (
    // Clicar al fons fosc tanca la finestra
    <div className="fonsModal" onClick={onClose}>
      {/* stopPropagation: clicar dins la finestra NO l'ha de tancar */}
      <div
        className="finestraModal"
        role="dialog"
        aria-modal="true"
        aria-label={`Detall de ${element.name}`}
        onClick={(e) => e.stopPropagation()}
      >
        <button type="button" className="botoTancar" onClick={onClose} aria-label="Tancar">
          ✕
        </button>

        <div className="contingutModal">
          {/* Columna esquerra: foto gran amb el visor d'escàner */}
          <div className="columnaImatge">
            <div className="visorModal">
              <span className="marcVisorModal modalTL" aria-hidden="true"></span>
              <span className="marcVisorModal modalTR" aria-hidden="true"></span>
              <span className="marcVisorModal modalBL" aria-hidden="true"></span>
              <span className="marcVisorModal modalBR" aria-hidden="true"></span>
              <img src={element.image} alt={element.name} className="imatgeModal" />
            </div>
          </div>

          {/* Columna dreta: tota la informació */}
          <div className="columnaInfo">
            <p className="registreModal">
              <span className="nodeRegistreModal" aria-hidden="true"></span>
              Nº {compendiumNumber}
            </p>

            <h2 className="titolModal">{element.name}</h2>
            {element.name_en && <p className="titolAnglesModal">{element.name_en}</p>}

            <div className="etiquetesModal">
              <span className="etiquetaModal">{element.category}</span>
              {games.map((game) => (
                <span key={game} className="etiquetaModal etiquetaJoc">{game}</span>
              ))}
            </div>

            <p className="descripcioModal">{element.description}</p>

            {locations.length > 0 && (
              <div className="seccioModal">
                <h3>Llocs</h3>
                <ul>
                  {locations.map((item) => <li key={item}>{item}</li>)}
                </ul>
              </div>
            )}

            {drops.length > 0 && (
              <div className="seccioModal">
                <h3>Botí</h3>
                <ul>
                  {drops.map((item) => <li key={item}>{item}</li>)}
                </ul>
              </div>
            )}

            {properties.length > 0 && (
              <div className="seccioModal">
                <h3>Propietats</h3>
                <ul>
                  {properties.map((item) => <li key={item}>{item}</li>)}
                </ul>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Modal;
