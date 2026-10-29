"""Diccionari de traducció especialitzat per al Compendi de Hyrule de BotW i TotK.
Tradueix frases completes i estructures recurrents dels textos del compendi a un català natural.
"""
import re


SENTENCE_MAP = {
    # Criatures i monstres
    "This common species is a nuisance all over Hyrule.": "Aquesta espècie comuna és una plaga present per tot Hyrule.",
    "While not very clever, they are at least intelligent enough to hunt beasts and grill the meat for food.": "Tot i no ser especialment astuts, tenen prou intel·ligència per caçar bèsties i rostir la carn al foc.",
    "They are sometimes seen marching in groups.": "Sovint se'ls veu marxant en patrulles organitzades.",
    "If they come at you, watch out for their sharp horns!": "Si t'ataquen, vigila amb les seves banyes esmolades!",
    "These spell-casting monsters can be found all over Hyrule.": "Aquests monstres bruixots llançadors d'encanteris es troben per tot Hyrule.",
    "The weather will normalize once the Wizzrobe is defeated.": "El clima de la zona es normalitzarà un cop derrotat el Wizzrobe.",
    "These quick-witted, lizard-like monsters can be found all over Hyrule.": "Aquests monstres àgils semblants a sargantanes es troben per tot Hyrule.",
    "This low-level, gel-based monster can be found all over Hyrule.": "Aquest monstre gelatinós bàsic es pot trobar per tot el regne d'Hyrule.",
    "It tends to spring its attacks on unsuspecting adventurers from the ground or trees.": "Sol sorgir per sorpresa des de terra o des dels arbres per atacar viatgers desprevinguts.",
    "This low-level gel monster is engulfed in flames.": "Aquest monstre gelatinós bàsic està completament envoltat de flames.",
    "Its strength varies depending on its size.": "La seva força i resistència depenen de la seva mida.",
    "It tends to explode if attacked from close range, so the use of spears, arrows, and other ranged weapons is advised.": "Acostuma a explotar si se l'ataca de prop, per la qual cosa es recomana l'ús de llances, fletxes o armes a distància.",
    "This enormous monster is naturally camouflaged as a rock formation.": "Aquest monstre colossal es camufla de manera natural com una formació rocosa.",
    "Neither sword nor arrow can pierce its stony form, but a cunning adventurer knows to scale its body and attack the ore sprouting from its peak.": "Ni l'espasa ni les fletxes poden perforar el seu cos de pedra, però un aventurer astut sap escalar-lo per colpejar el jaciment de mineral del cim.",
    "Few have seen it in the current age.": "Molt pocs l'han vist en l'època actual.",
    "After the Upheaval, these monsters began appearing in Hyrule's cave systems.": "Després del Cataclisme, aquests monstres van començar a aparèixer a les coves d'Hyrule.",
    "It faithfully obeys commands and tries to root out any being it deems to be an enemy.": "Obeeix cegament les ordres i intenta eliminar qualsevol ésser que consideri una amenaça.",
    "An elite Soldier Construct, hence its \"captain\" title.": "Un golem militar d'elit, d'aquí el seu títol de 'capità'.",
    "Made by the Zonai with advanced techniques and magic.": "Fabricat pels Zonai mitjançant tècniques avançades i màgia ancestral.",
    "These can most often be found on plains.": "Es troben principalment a les planes d'Hyrule.",
    "Their usefulness as transportation has made them valuable since ancient times.": "La seva gran utilitat com a mitjà de transport els ha fet molt valuosos des de temps remots.",
    "This giant horse is the last of its kind.": "Aquest cavall gegantí és l'únic exemplar supervivent de la seva espècie.",
    "Its physical capabilities completely overshadow those of regular horses.": "La seva força i velocitat superen amb escreix les dels cavalls normals.",

    # Materials i cuina
    "A common mushroom found near trees around Hyrule.": "Un bolet comú que creix a la base dels arbres per tot Hyrule.",
    "Eat it to restore half a heart.": "Es pot menjar cru per recuperar mig cor o cuinar en diversos plats nutritius.",
    "Cook it with a critter to make an elixir.": "Cuina'l amb una bestiola o insecte per elaborar un elixir.",
    "Attach it to a weapon to vastly increase its attack power.": "Acobla'l a una arma amb Fuse per augmentar notablement la seva potència d'atac.",
    "Attach it to a weapon to greatly increase its attack power, or cook it with a critter to make an elixir.": "Acobla'l a una arma per incrementar la potència d'atac o combina'l amb bestioles per fer elixirs.",
    "Attach it to a weapon to vastly increase its attack power, or cook it with a critter to make an elixir.": "Acobla'l a una arma per potenciar enormement l'atac o cuina'l en elixirs màgics.",
    "A common fruit eaten by people since ancient times.": "Una fruita molt comuna consumida pels pobladors d'Hyrule des de temps antics.",
    "Eat it fresh, or cook it to increase its effect.": "Menja-la fresca per guarir-te o cuina-la per potenciar-ne els efectes de recuperació.",
    "Fruit from palm trees that grow near the ocean.": "Fruit de les palmeres que creixen a les costes càlides del sud.",
    "It doesn't offer any special effects but will increase your heart recovery when cooked.": "No atorga efectes secundaris especials, però cuinada recupera un gran nombre de cors.",
    "This prized fruit is said to have fallen from the heavens.": "Aquesta fruita cobejada cau de les illes celestes i és summament apreciada.",
    "Eating it restores hearts, and cooking it with other ingredients increases the number of hearts it restores.": "Consumir-la restaura cors, i cuinar-la amb altres ingredients augmenta considerablement la vitalitat recuperada.",
    "This deposit contains a good deal of ore.": "Aquest jaciment conté una bona quantitat de minerals valuosos.",
    "Breaking the rock will yield rock salt, flint, and other ore and minerals.": "Trencar la roca permet extreure sal gemma, sílex i altres gemmes i minerals útils.",
    "Fortunes untold (potentially) await the lucky adventurer who finds one of these.": "Grans tresors i recompenses esperen l'afortunat aventurer que troba un d'aquests cofres.",
    "Chests can often be found within shrines or at enemy encampments.": "Els cofres se solen trobar a l'interior dels santuaris o als campaments enemics.",

    # Armes i equipament
    "The legendary sword that seals the darkness.": "La llegendària espasa sagrada que segella la foscor.",
    "Its corruption was healed by its time with the Light Dragon.": "La seva corrupció i trencament van ser guarits gràcies al poder del Drac de la Llum.",
    "Wooden branches such as this are pretty common, but it's surprisingly well-balanced.": "Branques d'arbre senzilles molt comunes, però sorprenentment ben equilibrades com a arma improvisada.",
    "It doesn't do much damage, but it can be used in a pinch.": "No infligeix gaire dany, però és útil en situacions d'emergència.",
    "A traditional sword prized by Hyrulean travelers for its reliability.": "Una espasa tradicional molt apreciada pels viatgers d'Hyrule per la seva fiabilitat.",
    "A shield favored by travelers for its sturdy construction.": "Un escut molt utilitzat pels viatgers per la seva construcció sòlida i resistent.",
    "Attaching a material greatly enhances the material's power but doesn't add as much durability.": "Acoblar-hi un material en potència enormement el dany, encara que no n'amplia tant la durabilitat.",
    "It can yield powerful attacks when you're down to your last heart.": "Permet desfermar atacs devastadors quan et queda només el teu últim cor de salut.",
    "The Sheikah of ancient Hyrule developed this as a weapon to combat Ganon.": "Els antics Sheikah van desenvolupar aquesta arma ancestral per combatre Ganon.",
    "A sword forged by the Zora using special water-resistant metal.": "Una espasa forjada pels artesans Zora utilitzant un metall especial resistent a l'aigua.",
    "A spear crafted by the Zora for swift underwater thrusts.": "Una llança forjada pels Zora dissenyada per a estocades ràpides sota l'aigua.",
    "A sword crafted by the Goron from heavy volcanic stone and hardened iron.": "Una espasa robusta forjada pels Goron a partir de pedra volcànica pesada i ferro temperat.",
    "A scimitar favored by Gerudo warriors for its elegant curved blade.": "Una simitarra utilitzada per les guerreres Gerudo per la seva fulla corbada elegant i letal.",
    "A bow used by the Rito that allows rapid firing while gliding.": "Un arc lleuger utilitzat pels Rito que permet disparar ràpidament mentre es planeja pel cel.",
}


def translate_compendium_text(text):
    if not text:
        return ""
    # 1. Substitució de frases exactes
    result = text
    for en_sent, ca_sent in SENTENCE_MAP.items():
        result = result.replace(en_sent, ca_sent)

    # 2. Substitució de fragments i connectors comuns
    replacements = [
        ("can be found all over Hyrule", "es pot trobar per tot el regne d'Hyrule"),
        ("can be found in the Depths", "es pot trobar a les profunditats del Subsòl"),
        ("can be found on the Sky Islands", "es troba a les illes celestes"),
        ("found in caves", "trobat a l'interior de les coves"),
        ("found near water", "trobat a prop de zones d'aigua"),
        ("found in cold regions", "trobat a regions fredes i nevades"),
        ("found in volcanic regions", "trobat a zones volcàniques d'altes temperatures"),
        ("restores hearts", "restaura cors"),
        ("restores stamina", "recupera resistència"),
        ("increases attack power", "incrementa la potència d'atac"),
        ("increases defense", "incrementa la defensa"),
        ("increases stealth", "millora el sigil"),
        ("increases swim speed", "millora la velocitat de natació"),
        ("grants cold resistance", "atorga protecció contra el fred"),
        ("grants heat resistance", "atorga protecció contra la calor"),
        ("grants shock resistance", "atorga aïllament elèctric"),
        ("resists lightning", "resisteix l'impacte dels llamps"),
        ("flame resistance", "protecció contra flames"),
        ("Attach to an arrow", "Acobla a una fletxa"),
        ("Attach to a weapon", "Acobla a una arma"),
        ("Attach to a shield", "Acobla a un escut"),
        ("bursts into flames", "esclata en flames"),
        ("freezes enemies", "congela els enemics"),
        ("shocks enemies", "electritza els enemics"),
        ("releases a burst of light", "emet un esclat de llum encegadora"),
        ("creates a smoke screen", "crea una cortina de fum per despistar"),
        ("crafted from ancient materials", "fabricat amb materials ancestrals"),
        ("favored by knights", "emprat habitualment pels cavallers de la guàrdia"),
        ("used by Hyrulean soldiers", "utilitzat pels soldats de l'exèrcit d'Hyrule"),
        ("a staple of the Yiga Clan", "una eina distintiva del Clan Yiga"),
    ]
    for en_frag, ca_frag in replacements:
        result = re.sub(re.escape(en_frag), ca_frag, result, flags=re.IGNORECASE)

    return result.strip()
