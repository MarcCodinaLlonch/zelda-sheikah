import './Card.css';

function Card({ element, onSelect }) {
  // Número oficial de la carta a la col·lecció (001 a 729)
  const compendiumNumber = String(element.card_number || element.compendium_number || element.id).padStart(3, '0');

  return (
    <article className="contenidorCard">
      {/* .cosCard porta el retall bisellat; el resplendor del hover viu a l'<article> perquè no es talli */}
      <div className="cosCard">
        {/* Barra superior HUD: número de registre i categoria */}
        <div className="capcaleraCard">
          <span className="codiRegistre">
            <span className="nodeRegistre" aria-hidden="true"></span>
            Nº {compendiumNumber}
          </span>
          <span className="badgeCategoria">{element.category}</span>
        </div>

        {/* Visor d'escàner amb les 4 cantoneres d'enfocament */}
        <div className="visorSheikah">
          <span className="marcVisor visorTL" aria-hidden="true"></span>
          <span className="marcVisor visorTR" aria-hidden="true"></span>
          <span className="marcVisor visorBL" aria-hidden="true"></span>
          <span className="marcVisor visorBR" aria-hidden="true"></span>

          <img
            src={element.image}
            title={element.name}
            alt={element.name}
            className="imatgeCard"
            loading="lazy"
          />
        </div>

        <h2 className="titolCard">{element.name}</h2>

        {/* La descripció es retalla a 3 línies; el text complet es veu al detall */}
        <div className="descripcioCard">
          <p>{element.description}</p>
        </div>

        {/* Botó que obre la finestra de detall: avisa al pare amb l'element d'aquesta targeta */}
        <button
          type="button"
          className="botoDetall"
          onClick={() => onSelect(element)}
        >
          Veure detall
        </button>
      </div>
    </article>
  );
}

export default Card;