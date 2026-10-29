import './Header.css';

function Header() {
    return (
        <header className="capcalera">
            <div className="filaEmblema">
                {/* Traç de circuit esquerre amb nodes circulars */}
                <svg className="circuitLateral esquerre" viewBox="0 0 160 24" aria-hidden="true">
                    <circle cx="8" cy="12" r="3" fill="none" stroke="currentColor" strokeWidth="1.5" />
                    <path d="M 11 12 L 85 12 L 95 4 L 148 4" fill="none" stroke="currentColor" strokeWidth="1.5" />
                    <circle cx="152" cy="4" r="3" fill="currentColor" />
                    <path d="M 55 12 L 65 20 L 130 20" fill="none" stroke="currentColor" strokeWidth="1.2" opacity="0.6" />
                    <circle cx="134" cy="20" r="2.5" fill="none" stroke="currentColor" strokeWidth="1.2" opacity="0.6" />
                </svg>

                {/* Emblema central: Ull Sheikah amb anells de circuit i nodes (pantalla d'activació) */}
                <div className="simbolSheikah">
                    <svg viewBox="0 0 140 130" className="iconaSheikahEye" aria-hidden="true">
                        <path d="M 32 24 A 54 54 0 0 0 18 78" fill="none" stroke="currentColor" strokeWidth="2" opacity="0.75" />
                        <circle cx="32" cy="24" r="3.5" fill="currentColor" />
                        <circle cx="18" cy="78" r="3.5" fill="currentColor" />

                        <path d="M 108 24 A 54 54 0 0 1 122 78" fill="none" stroke="currentColor" strokeWidth="2" opacity="0.75" />
                        <circle cx="108" cy="24" r="3.5" fill="currentColor" />
                        <circle cx="122" cy="78" r="3.5" fill="currentColor" />

                        <path d="M 28 92 L 40 104 L 54 104" fill="none" stroke="currentColor" strokeWidth="1.8" opacity="0.75" />
                        <circle cx="26" cy="90" r="3" fill="currentColor" />
                        <circle cx="57" cy="104" r="2.5" fill="none" stroke="currentColor" strokeWidth="1.5" />

                        <path d="M 112 92 L 100 104 L 86 104" fill="none" stroke="currentColor" strokeWidth="1.8" opacity="0.75" />
                        <circle cx="114" cy="90" r="3" fill="currentColor" />
                        <circle cx="83" cy="104" r="2.5" fill="none" stroke="currentColor" strokeWidth="1.5" />

                        <line x1="16" y1="60" x2="29" y2="60" stroke="currentColor" strokeWidth="2" />
                        <circle cx="13" cy="60" r="4" fill="currentColor" />
                        <line x1="111" y1="60" x2="124" y2="60" stroke="currentColor" strokeWidth="2" />
                        <circle cx="127" cy="60" r="4" fill="currentColor" />

                        <polygon points="70,25 63,39 77,39" fill="currentColor" />
                        <polygon points="39,33 37,47 49,42" fill="currentColor" />
                        <polygon points="102,32 91,42 102,47" fill="currentColor" />

                        <path d="M 28 60 Q 70 33 112 60 Q 70 87 28 60 Z" fill="none" stroke="currentColor" strokeWidth="4.5" strokeLinejoin="round" />

                        <circle cx="70" cy="60" r="13" fill="none" stroke="currentColor" strokeWidth="3.5" />
                        <circle cx="70" cy="60" r="5.5" fill="currentColor" />

                        <path d="M 67 75 L 73 75 L 75 104 Q 75 113 70 113 Q 65 113 65 104 Z" fill="currentColor" />
                    </svg>
                </div>

                {/* Traç de circuit dret amb nodes circulars */}
                <svg className="circuitLateral dret" viewBox="0 0 160 24" aria-hidden="true">
                    <circle cx="8" cy="4" r="3" fill="currentColor" />
                    <path d="M 12 4 L 65 4 L 75 12 L 149 12" fill="none" stroke="currentColor" strokeWidth="1.5" />
                    <circle cx="152" cy="12" r="3" fill="none" stroke="currentColor" strokeWidth="1.5" />
                    <circle cx="26" cy="20" r="2.5" fill="none" stroke="currentColor" strokeWidth="1.2" opacity="0.6" />
                    <path d="M 30 20 L 95 20 L 105 12" fill="none" stroke="currentColor" strokeWidth="1.2" opacity="0.6" />
                </svg>
            </div>

            <div className="textosCapcalera">
                <h1 className="titolCapcalera">The Legend of Zelda</h1>
                <p className="subtitolCapcalera">Enciclopèdia Sheikah</p>

                {/* Separador de circuit: línia - node - rombe - node - línia */}
                <svg className="separadorCircuit" viewBox="0 0 240 12" aria-hidden="true">
                    <line x1="0" y1="6" x2="98" y2="6" stroke="currentColor" strokeWidth="1" opacity="0.55" />
                    <circle cx="104" cy="6" r="2.5" fill="none" stroke="currentColor" strokeWidth="1.2" />
                    <polygon points="120,1 125,6 120,11 115,6" fill="currentColor" />
                    <circle cx="136" cy="6" r="2.5" fill="none" stroke="currentColor" strokeWidth="1.2" />
                    <line x1="142" y1="6" x2="240" y2="6" stroke="currentColor" strokeWidth="1" opacity="0.55" />
                </svg>
            </div>
        </header>
    );
}

export default Header;