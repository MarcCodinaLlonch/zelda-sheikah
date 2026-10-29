import './Modal.css';

function Modal({ element, onClose }) {
  const compendiumNumber = String(element.card_number || element.compendium_number || element.id).padStart(3, '0');

  // Les llistes de details poden venir buides: només mostrarem les seccions que tinguin dades
  const locations = element.details?.locations || [];
  const drops = element.details?.drops || [];
  const properties = element.details?.properties || [];
  const games = element.games || [];

  return (
    <div className="fonsModal" onClick={onClose}>
      <div 

        className="finestraModal"
        role="dialog" //informa navegador que aquest element html és un element emergent
        aria-modal="true" //contingut darrere queda temporalment bloquejat
        aria-label={`Detall de ${element.name}`}
        onClick={(e) => e.stopPropagation()} // evitem que l'event onClick es propagi cap a l'element pare i es tanqui el modal si fem clic dins del modal
      >
        <button type="button" className="botoTancar" onClick={onClose} aria-label="Tancar">
          ✕
        </button>

        <div className="contingutModal">
          <div className="columnaImatge">
            <div className="visorModal">
              <span className="marcVisorModal modalTL" aria-hidden="true"></span>
              <span className="marcVisorModal modalTR" aria-hidden="true"></span>
              <span className="marcVisorModal modalBL" aria-hidden="true"></span>
              <span className="marcVisorModal modalBR" aria-hidden="true"></span>
              <img src={element.image} alt={element.name} className="imatgeModal" />
            </div>
          </div>

          <div className="columnaInfo">
            <p className="registreModal">
              <span className="nodeRegistreModal" aria-hidden="true"></span>
              Nº {compendiumNumber}
            </p>

            <h2 className="titolModal">{element.name}</h2>
            {/* Si l'API no té el camp 'name_en' (és null o buit), 
                evitem pintar un paràgraf buit i no es renderitza res. */}
            {element.name_en && <p className="titolAnglesModal">{element.name_en}</p>}

            <div className="etiquetesModal">
              <span className="etiquetaModal">{element.category}</span>
              {games.map((game) => (
                <span key={game} className="etiquetaModal etiquetaJoc">{game}</span>
              ))}
            </div>

            <p className="descripcioModal">{element.description}</p>
            {/* Mostra location, drop, propietats del item si n'hi ha */}
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
