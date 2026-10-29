import "./List.css";
import Card from "./Card.jsx";

function List({ title, elements, onSelect }) {
    return (
        <section className="seccioLlista">
            <div className="capcaleraLlista">
                <div className="titolComptador">
                    <h2>{title}</h2>
                    <span className="comptador">{elements.length} REGISTRES</span>
                </div>
                <div className="circuitCapcaleraLlista" aria-hidden="true">
                    <span className="nodeCircuit"></span>
                    <span className="liniaCircuit"></span>
                    <span className="nodeCircuit buit"></span>
                </div>
            </div>

            {elements.length === 0 ? (
                <div>
                    <div className="estaBuit">
                        <p className="textEstatBuit">No s'ha trobat cap dada al Compendi Sheikah.</p>
                    </div>
                </div>
            ) : (
                <div className="graellaTasques">
                    {elements.map(element => (
                        /* onSelect baixa fins a la targeta perquè el botó pugui obrir el detall */
                        <Card key={element.id} element={element} onSelect={onSelect} />
                    ))}
                </div>
            )}
        </section>
    );
}

export default List;