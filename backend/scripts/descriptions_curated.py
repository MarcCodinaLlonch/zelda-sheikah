"""Descripcions detallades i fidels en català per a personatges, races, llocs, jocs i caps.
Aquestes descripcions han estat redactades expressament per al projecte de classe.
"""

CURATED_DESCRIPTIONS = {
    # ------------------------------------------------------------- PERSONATGES
    "link": (
        "El cavaller escollit per la Master Sword i l'heroi llegendari d'Hyrule. "
        "Després de despertar del Santuari de la Resurrecció a Breath of the Wild sense records, "
        "va derrotar Calamity Ganon per alliberar el regne. A Tears of the Kingdom, després de "
        "perdre el braç dret sota el Castell d'Hyrule, rep el braç màgic de Rauru i viatja pel cel, "
        "la superfície i el subsòl per rescatar la Princesa Zelda i derrotar el Rei Dimoni Ganondorf."
    ),
    "princess-zelda": (
        "La princesa d'Hyrule i portadora del poder sagrat que segella la foscor. A Breath of the Wild, "
        "va lluitar durant anys per despertar el seu poder ancestral, aconseguint contenir Calamity Ganon "
        "durant un segle. A Tears of the Kingdom, cau a través del temps fins a l'època de la fundació d'Hyrule, "
        "on es sacrifica sotmetent-se a la draconificació per restaurar la Master Sword durant mil·lennis."
    ),
    "ganondorf": (
        "El Rei Dimoni i líder original dels Gerudo en l'època fundacional d'Hyrule. Portador d'una Pedra Secreta, "
        "va jurar fidelitat falsa al rei Rauru abans de rebel·lar-se i assassinar la reina Sonia. Va ser segellat sota "
        "el Castell de Hyrule pel sacrifici de Rauru fins que el seu segell es trenca mil·lennis després, desfermant "
        "el Cataclisme a Tears of the Kingdom."
    ),
    "rhoam-bosphoramus-hyrule": (
        "L'últim rei d'Hyrule abans de la Gran Calamitat. Va morir defensant el castell fa cent anys. Apareix davant "
        "de Link a l'inici de Breath of the Wild disfressat com un ancià solitari al Gran Altiplà per guiar l'heroi "
        "i encomanar-li la missió de salvar la seva filla Zelda i el regne."
    ),
    "rauru": (
        "El primer Rei d'Hyrule i líder de la civilització ancestral Zonai. Posseeix un poder immens sobre la llum. "
        "Juntament amb la seva esposa Sonia, va fundar el regne d'Hyrule. Durant la Guerra de l'Empresonament, va "
        "sacrificar la seva vida utilitzant el seu propi braç dret per mantenir segellat Ganondorf."
    ),
    "sonia": (
        "La primera Reina d'Hyrule, d'origen hylià, sacerdotessa amb el poder de controlar el temps i avantpassada "
        "de la Princesa Zelda. Va rebre Zelda amb calidesa quan aquesta va viatjar al passat i la va entrenar "
        "en el control temporal abans de ser traïda i assassinada per Ganondorf."
    ),
    "mineru": (
        "La Savi de l'Esperit dels Zonai i germana gran del rei Rauru. Erudita brillant que va investigar les Pedres "
        "Secretes i la tecnologia Zonai. Després de ser greument ferida a la Guerra de l'Empresonament, va transferir "
        "el seu esperit a la Purah Pad i més tard ajuda en Link controlant un golem gegant al Subsòl."
    ),
    "impa": (
        "L'anciana líder de la tribu Sheikah al poble de Kakariko. Va viure la caiguda d'Hyrule fa cent anys i ha "
        "conservat els records i la voluntat de la família reial. A Tears of the Kingdom, tot i la seva avançada edat, "
        "viatja per tot el regne en globus aerostàtic investigant els misteriosos geoglifs."
    ),
    "purah": (
        "La genial científica en cap de la tribu Sheikah i directora del Laboratori d'Hateno. Famosa pel seu "
        "experiment d'anti-envelliment que la va convertir temporalment en una nena a Breath of the Wild. A Tears "
        "of the Kingdom lidera el Fuerte Vigia (Lookout Landing) com a jove adulta i inventa la Purah Pad."
    ),
    "robbie": (
        "El veterà investigador Sheikah expert en armament ancestral i tecnologia de Guardians. Antic líder del "
        "Laboratori d'Akkala, a Tears of the Kingdom col·labora amb Purah a Lookout Landing i millora la Purah Pad "
        "d'en Link amb el sensor de santuaris i el teletransportador de viatge."
    ),
    "paya": (
        "La neta d'Impa, inicialment tímida i devota cuidadora de la relíquia sagrada de Kakariko a Breath of the Wild. "
        "A Tears of the Kingdom ha madurat i ha assumit el càrrec de cap de la tribu Sheikah, liderant les investigacions "
        "sobre les ruïnes anellades caigudes del cel."
    ),
    "josha": (
        "Jove i entusiasta investigadora Sheikah protegida de Purah a Lookout Landing. És la responsable de coordinar "
        "les expedicions al perillós Subsòl (Depths), enviant en Link a cartografiar les arrels de llum i descobrir "
        "els misteris del món subterrani."
    ),
    "mipha": (
        "La princesa dels Zora, pilot de la Bèstia Divina Vah Ruta i campiona d'Hyrule dotada del poder de sanar ferides. "
        "Estava profundament enamorada d'en Link i li va forjar l'Armadura Zora abans de caure en combat fa cent anys "
        "contra l'Ira de l'Aigua de Ganon."
    ),
    "daruk": (
        "El valent guerrer Goron, pilot de la Bèstia Divina Vah Rudania i Campió d'Hyrule. Portador de l'Escut de Daruk, "
        "una barrera indestructible. Considerava en Link el seu germà d'armes més proper abans de morir a la Muntanya "
        "de la Mort durant la Gran Calamitat."
    ),
    "revali": (
        "L'arquer d'elit dels Rito, creador de la Fúria de Revali (un corrent d'aire ascendent) i pilot de la Bèstia "
        "Divina Vah Medoh. Orgullós i competitiu amb en Link, va ser un dels quatre Campions que van donar la vida "
        "fa cent anys protegint Hyrule."
    ),
    "urbosa": (
        "La matriarca dels Gerudo, pilot de la Bèstia Divina Vah Naboris i Campiona d'Hyrule. Mestra de la Fúria d'Urbosa, "
        "un poder devastador basat en el llamp. Va ser una figura maternal i protectora per a la Princesa Zelda."
    ),
    "sidon": (
        "El carismàtic príncep Zora, germà petit de Mipha. Amb el seu optimisme inesgotable i el seu gest emblemàtic, "
        "ajuda en Link a calmar Vah Ruta. A Tears of the Kingdom es converteix en el Savi de l'Aigua i nou Rei dels Zora, "
        "dominant l'aigua i purificant el domini del fang corrosiu."
    ),
    "yunobo": (
        "Descendent del Campió Daruk que va heretar el poder protector del seu avantpassat. Tot i ser poruc inicialment, "
        "guanya confiança ajudant en Link a la Muntanya de la Mort. A Tears of the Kingdom funda YunoboCo i, després de "
        "ser alliberat d'una màscara de control mental, esdevé el Savi del Foc."
    ),
    "riju": (
        "La jove matriarca de la tribu Gerudo a la Ciutat Gerudo. Va assumir el lideratge molt jove i va ajudar en Link "
        "a penetrar a Vah Naboris amb el Casc del Tro. A Tears of the Kingdom combat amb dues simitarres i esdevé "
        "la Savi del Llamp, invocant tempestes elèctriques."
    ),
    "teba": (
        "El guerrer arquer més hàbil del Poble Rito. Va ajudar en Link a abordar la Bèstia Divina Vah Medoh disparant "
        "als seus canons protectors. A Tears of the Kingdom succeeix en Kaneli com a cap del Poble Rito i entrena "
        "el seu fill Tulin."
    ),
    "tulin": (
        "El jove i prodigiós arquer Rito, fill de Teba. Posseeix una habilitat innata única per generar ràfegues "
        "de vent que impulsen qualsevol aliat per l'aire. A Tears of the Kingdom és el primer a despertar com a Savi, "
        "convertint-se en el Savi del Vent."
    ),
    "king-dorephan": (
        "El majestuós i immens Rei dels Zora, pare de Mipha i Sidon. Governa el Domini dels Zora des de fa més d'un "
        "segle. Malgrat el dolor per la pèrdua de la seva filla Mipha fa cent anys, confia en Link per salvar novament "
        "el seu poble del fang tòxic a Tears of the Kingdom."
    ),
    "muzu": (
        "El conseller reial ancià i rígid del Rei Dorephan al Domini dels Zora. Inicialment guardava un gran ressentiment "
        "cap a en Link per la mort de Mipha fa cent anys, però canvia d'actitud en veure la devoció de Link portant "
        "l'armadura confeccionada per la princesa."
    ),
    "yona": (
        "Una elegant dama Zora d'un domini exterior, promesa i posterior esposa del Príncep Sidon a Tears of the Kingdom. "
        "Dedica tots els seus esforços a atendre els ferits pel fang caigut del cel i repara l'antiga Armadura Zora "
        "per a en Link."
    ),
    "bludo": (
        "El veterà i contundent cap de la Ciutat Goron a la Muntanya de la Mort. Pateix de forts dolors d'esquena que "
        "li impedeixen pilotar els canons ell mateix, delegant les missions a Yunobo i a en Link."
    ),
    "buliara": (
        "La imponent capitana de la guàrdia reial Gerudo i mà dreta de la matriarca Riju. Implacable i fidel defensora "
        "de la ciutat, vigila que cap home (voe) entri a la ciutat sagrada sense autorització."
    ),
    "kass": (
        "El joglar i trobador Rito que viatja per tot Hyrule tocant el seu acordió. Coneix les antigues balades "
        "compostes pel seu mestre Sheikah que amaguen les claus per resoldre els santuaris ancestrals i les gestes "
        "dels quatre Campions."
    ),
    "hestu": (
        "L'enorme i alegre Korok que balla amb les seves maraques màgiques. Quan en Link li recupera les llavors de "
        "Korok perdudes, Hestu realitza balls festius que amplien la capacitat de la bossa d'armes, arcs i escuts."
    ),
    "beedle": (
        "El comerciant itinerant més fidel i incansable de tot Hyrule. Carrega una motxilla gegant en forma d'escarabat "
        "i ven tota mena de fletxes i queviures a les postes. Té una obsessió incontrolable pels escarabats rinoceront."
    ),
    "kilton": (
        "L'extravagant comerciant nocturn fascinat pels monstres d'Hyrule. Viatja amb la seva botiga Monster Shop "
        "en forma de globus i intercanvia parts de monstre per màscares que permeten camuflar-se entre bokoblins i lizalfos."
    ),
    "bolson": (
        "El carismàtic arquitecte i líder de Bolson Construction a Hateno Village. Cèlebre pel seu estil extravagant, "
        "restaura la casa d'en Link a Hateno i exigeix que tots els seus empleats tinguin noms que acabin en 'son'."
    ),
    "hudson": (
        "Mestre fuster de Bolson Construction que viatja a la regió d'Akkala per fundar Tarrey Town des de zero. "
        "A Tears of the Kingdom és el propietari d'Hudson Construction i ven materials per a la construcció amb Ultrahand."
    ),
    "master-kohga": (
        "L'excèntric i pompós líder suprem del Clan Yiga. Obsessionat amb eliminar Link i revenjar-se de la família reial, "
        "utilitza màquines i encanteris estrambòtics. Després de caure al buit a BotW, reapareix al Subsòl a Tears of the "
        "Kingdom intentant ressuscitar el Rei Dimoni."
    ),
    "great-deku-tree": (
        "El savi esperit guardià del Bosc Korok i de la Master Sword. Ha vigilat Hyrule durant eons, custodiant "
        "l'espasa sagrada mentre en Link es recuperava al Santuari de la Resurrecció, i acollint els Koroks sota la seva copa."
    ),
    "great-fairy": (
        "Fades gegantines de gran bellesa (Cotera, Mija, Shisa i Kaysa) que habiten en brolladors amagats en forma de "
        "poncella. Després de rebre ofrenes de rupies o serenates musicals, milloren la defensa de les armadures d'en Link."
    ),
    "symin": (
        "L'ajudant científic Sheikah del Laboratori d'Hateno sota la tutela de Purah. S'encarrega d'organitzar els "
        "arxius del Compendi de Hyrule i a Tears of the Kingdom exerceix com a mestre de l'escola del poble."
    ),
    "pikango": (
        "Un pintor itinerant que recorre les postes d'Hyrule amb el seu cavallet. Gràcies al seu coneixement del paisatge, "
        "ajuda en Link a localitzar els llocs exactes on la Princesa Zelda va fer fotos fa un segle."
    ),
    "kaneli": (
        "L'ancià i venerat cap comunal del Poble Rito a Breath of the Wild, fàcilment reconeixible pel seu aspecte de "
        "gran mussol savi. Gestiona amb serenor les crisis del poble abans de cedir el lideratge a Teba."
    ),
    "koltin": (
        "El germà petit de Kilton a Tears of the Kingdom. Somia amb convertir-se en un Satori (Senyor de la Muntanya) "
        "i demana a en Link que li porti els emblemes de Bubbul Gems de les coves a canvi d'equips únics de monstres."
    ),
    "penn": (
        "Un entusiasta periodista Rito de la 'Gaceta El Trébol' (Lucky Clover Gazette). A Tears of the Kingdom s'associa "
        "amb en Link per investigar rumors sobre la Princesa Zelda a totes les postes del regne al crit de '¡Kakariko!'."
    ),
    "addison": (
        "El treballador més fidel d'Hudson Construction. A Tears of the Kingdom es troba per tots els camins aguantant "
        "fermesa rètols del president Hudson i necessita que en Link construeixi estructures per evitar que caiguin."
    ),
    "hoz": (
        "El capità dels soldats de la guàrdia d'Hyrule a Lookout Landing. Lidera les batudes defensives contra els "
        "campaments de monstres que assetgen els camins del regne."
    ),
    "tauro": (
        "El líder de l'Equip d'Investigació Zonai a Tears of the Kingdom. Erudita apassionat que desxifra els textos "
        "i relleus antics que revelen la ubicació de les ruïnes anellades de Kakariko."
    ),
    "calip": (
        "Un arqueòleg arrogant i autopromocionat que es fa anomenar 'doctor'. Tot i les seves maneres pedants, "
        "ajuda Tauro i en Link en la traducció d'inscripcions Zonai a Kakariko."
    ),
    "cece": (
        "L'extravagant i aclamada dissenyadora de moda del Poble Hateno. Ha creat un moviment estètic basat en bolets "
        "multicolors que competeix per l'alcaldia del poble contra el tradicionalista Reede."
    ),
    "steward-construct": (
        "Gòlems pacífics construïts per la civilització Zonai mil·lennis enrere. Romanen a les illes celestes i al "
        "subsòl ensenyant en Link a refinar mineral de Zonani o utilitzar càpsules d'artefactes."
    ),

    # ------------------------------------------------------------------- RACES
    "hylian": (
        "La raça més nombrosa d'Hyrule, caracteritzada per les seves orelles punxegudes que, segons la tradició, "
        "els permeten escoltar els missatges dels déus. Són els fundadors de la família reial i posseeixen una gran "
        "versatilitat com a agricultors, comerciants i cavallers."
    ),
    "goron": (
        "Una raça pacífica i robusta d'éssers de pedra que habiten a la Muntanya de la Mort i Ciutat Goron. S'alimenten "
        "de roques riques en minerals, resisteixen temperatures extremes de lava i tenen l'habilitat d'enrotllar-se "
        "sobre ells mateixos per desplaçar-se rodant a gran velocitat."
    ),
    "zora": (
        "Una elegant raça amfíbia que habita al Domini dels Zora, a la regió fluvial de Lanayru. Posseeixen una "
        "esperança de vida de diversos segles, una habilitat innata per nedar contra corrent i remuntar cascades, "
        "i una arquitectura aquàtica magistral."
    ),
    "gerudo": (
        "Una orgullosa raça de guerreres del desert que habiten a la Ciutat Gerudo. La seva societat està composta "
        "exclusivament per dones, amb l'excepció d'un sol home nascut cada cent anys. Són cèlebres pel seu domini "
        "de les simitarres, les llances i el comerç de joies."
    ),
    "rito": (
        "Una noble raça d'homes ocell que habiten a la freda regió de Hebra, al Poble Rito construït en un gran pilar "
        "de roca. Són arquers formidables capaços de disparar mentre planegen i aprofiten els corrents tèrmics del cel."
    ),
    "sheikah": (
        "Un clan ancestral de savis i ninjas lleials a la família reial d'Hyrule. Coneguts pel símbol de l'ull que plora, "
        "van desenvolupar fa 10.000 anys una tecnologia prodigiosa capaç de construir les Bèsties Divines, Guardians "
        "i la Sheikah Slate."
    ),
    "korok": (
        "Petits esperits dels boscos amb màscares de fulles, nascuts sota la protecció del Gran Arbre Deku. S'amaguen "
        "per tots els racons d'Hyrule i recompensen aquells que resolen els seus petits puzles amb llavors de Korok."
    ),
    "zonai": (
        "Una antiga i mística civilització vinguda dels cels, posseïdora d'un poder màgic sobre la llum i d'una avançada "
        "tecnologia d'artefactes verds. Van fundar el regne d'Hyrule juntament amb els Hylians en l'època del Rei Rauru."
    ),
    "yiga-clan": (
        "Una facció rebel de Sheikah que fa deu mil anys va jurar lleialtat eterna a Calamity Ganon i Ganondorf. Operen "
        "en secret des de la seva base al desert de Gerudo, assassinant qualsevol partidari de la família reial i "
        "amb una obsessió pels plàtans de força."
    ),

    # -------------------------------------------------------------------- LLOCS
    "hyrule-castle": (
        "La seu del poder de la monarquia d'Hyrule i el cor geogràfic del regne. A Breath of the Wild estava dominat "
        "per la Calamitat i envoltat de Guardians mortals. A Tears of the Kingdom es trenca i s'eleva pels aires, "
        "amb un abisme directe al Subsòl."
    ),
    "great-plateau": (
        "L'altiplà aïllat on Link desperta després de cent anys de son. Conegut com el bressol del regne d'Hyrule, "
        "allotja les ruïnes del Temple del Temps original i el Santuari de la Resurrecció."
    ),
    "great-sky-island": (
        "La immensa illa flotant sobre Hyrule on Link desperta a Tears of the Kingdom després de la corrupció de la "
        "Master Sword. És el territori d'entrenament dels poders Zonai (Ultrahand, Fuse, Ascend i Recall)."
    ),
    "depths": (
        "El misteriós i perillós món subterrani que s'estén sota tot Hyrule, immers en la foscor absoluta. Només és "
        "il·luminat per les Arrels de Llum i habitat per monstres corruptes pel Fang de les Tenebres."
    ),
    "hyrule-field": (
        "La immensa plana central que connecta totes les regions d'Hyrule. Antigament travessada per camins reials "
        "i pobles pròspers, ara és una plana oberta plena de campaments de monstres, ruïnes i postes."
    ),
    "kakariko-village": (
        "El poble tradicional de la tribu Sheikah, situat en una vall protegida entre muntanyes. Allotja la residència "
        "d'Impa, botigues d'articles tradicionals i, a Tears of the Kingdom, les ruïnes anellades caigudes del cel."
    ),
    "hateno-village": (
        "Un poble agrícola tranquil a la regió de Necluda que va sobreviure gairebé intacte a la Calamitat fa cent anys. "
        "Famosa pels seus molins de vent, la casa d'en Link, la moda de Cece i el Laboratori d'Investigació a dalt del turó."
    ),
    "zora-s-domain": (
        "L'espectacular capital aquàtica dels Zora, esculpida en pedra blava brillant sobre les cascades de Lanayru. "
        "Construïda per fondre's harmoniosament amb l'aigua i protegida pel Rei Dorephan i el Príncep Sidon."
    ),
    "goron-city": (
        "La capital minera dels Goron, construïda sobre la roca viva a les faldilles de la Muntanya de la Mort. "
        "Compta amb tallers de forja, escultures de pedra gegantines dels antics caps i aigües termals relaxants."
    ),
    "gerudo-town": (
        "La ciutat-fortalesa emmurallada al bell mig del Desert Gerudo. Regida per una llei sagrada que prohibeix "
        "l'entrada a qualsevol home (voe), és un centre bulliciós de comerç de joies, artesania i begudes al seu oasi."
    ),
    "rito-village": (
        "Un poble vertical espectacular construït al voltant d'un gran pilar de roca enmig del llac a la regió de Hebra. "
        "Les seves cases de fusta en espiral i ponts penjants permeten als Rito alçar el vol aprofitant els corrents ascendents."
    ),
    "korok-forest": (
        "El santuari vegetal amagat al cor dels Lost Woods on resideixen el Gran Arbre Deku i centenars de Koroks. "
        "És el lloc sagrat on descansa el pedestal de la Master Sword."
    ),
    "lost-woods": (
        "Un bosc boirós i laberíntic ple d'arbres amb cares somrients que engoleix qualsevol viatger que s'allunyi "
        "del camí correcte guiat pel foc o el vent, tornant-lo a l'entrada."
    ),
    "lookout-landing": (
        "El quarter general d'emergència fundat per Purah a les portes del Castell de Hyrule a Tears of the Kingdom. "
        "Reuneix cavallers, investigadors Sheikah i refugiats per coordinar la recerca de la Princesa Zelda."
    ),
    "tarrey-town": (
        "Un poble multicultural construït sobre un pont de roca a Akkala per Hudson. Reuneix habitants de totes les "
        "races d'Hyrule i a TotK compta amb una pista de curses de vehicles Zonai."
    ),
    "lurelin-village": (
        "Un acollidor poble mariner a la costa sud de Faron, amb cases de fulles de palma i vaixells pesquers. "
        "A Tears of the Kingdom és envaït per monstres pirates fins que Link i Bolson el reconstrueixen."
    ),
    "kara-kara-bazaar": (
        "Un oasi vibrant i paradís comercial abans d'endinsar-se al gran Desert Gerudo. Compta amb palmeres, aigua "
        "fresca i botigues on viatgers de totes les races es preparen per travessar les dunes."
    ),
    "death-mountain": (
        "L'imponent volcà actiu d'Eldin que domina el nord-est d'Hyrule. Les seves altes temperatures cremen qualsevol "
        "objecte de fusta i a TotK del seu cràter en brolla Fang Rogenc del Rei Dimoni."
    ),
    "gerudo-desert": (
        "Una vasta i inhòspita extensió de dunes al sud-oest del regne, assotada per tempestes de sorra que desorienten "
        "qualsevol mapa i temperatures extremes: calor abrasadora de dia i fred glacial de nit."
    ),
    "hebra-mountains": (
        "Una serralada alpina congelada que s'estén pel nord-oest d'Hyrule, dominada pel pic d'Hebra i assotada per "
        "viseres de neu constants que exigeixen roba tèrmica."
    ),
    "mount-lanayru": (
        "Una muntanya sagrada coberta de neu permanent a l'est d'Hyrule. A dalt de tot acull la Font de la Saviesa, "
        "on la princesa Zelda pregava i on reposa el drac Naydra."
    ),
    "satori-mountain": (
        "Una muntanya mística a la regió de Ridgeland on floreixen cirerers sagrats i es reuneixen criatures lluminoses "
        "sota la presència del Senyor de la Muntanya (Satori)."
    ),
    "lake-hylia": (
        "El llac natural més extens d'Hyrule, travessat pel colossal Pont d'Hylia. Sota les seves aigües profundes "
        "descansen secrets antics i a la superfície s'hi alça el Drac Farosh."
    ),
    "eventide-island": (
        "Una illa remota a l'extrem sud-est d'Hyrule que posa a prova el valor dels herois despullant-los de tot el "
        "seu equipament i armes per sobreviure només amb els recursos naturals."
    ),
    "temple-of-time": (
        "L'emblemàtic temple consagrat a la Deessa Hylia al Gran Altiplà, ara en ruïnes però conservant l'estàtua de "
        "la Deessa que beneeix en Link a canvi d'orbes de santuari."
    ),
    "shrine-of-resurrection": (
        "La cambra mèdica subterrània Sheikah on Link va dormir durant cent anys per guarir les seves ferides mortals "
        "després de la Gran Calamitat."
    ),
    "hateno-ancient-tech-lab": (
        "L'antic observatori i laboratori Sheikah encapçalat per Purah i Symin, situat en un turó amb vistes al mar a Hateno. "
        "Allotja la Forja Blava ancestral utilitzada per millorar les funcions de la Sheikah Slate."
    ),
    "akkala-ancient-tech-lab": (
        "El laboratori remot de Robbie situat a l'extrem nord-est d'Hyrule. Allotjava el robot de forja Cherry (Cirela), "
        "capaç de crear fletxes ancestrals, escuts i l'Armadura Ancestral."
    ),
    "forgotten-temple": (
        "Un temple colossal amagat al fons del Canó de Tanagar. Allotja l'estàtua més gran de la Deessa Hylia i, a TotK, "
        "un mapa de relleu complet amb la ubicació dels geoglifs del regne."
    ),
    "divine-beast-vah-ruta": (
        "La Bèstia Divina de l'Aigua en forma d'elefant colossal, pilotada originàriament per la Campiona Mipha per "
        "protegir el Domini dels Zora."
    ),
    "divine-beast-vah-rudania": (
        "La Bèstia Divina del Foc en forma de salamandra gegant, pilotada pel Campió Daruk a la Muntanya de la Mort."
    ),
    "divine-beast-vah-medoh": (
        "La Bèstia Divina del Vent en forma d'ocell mecànic gegantí, pilotada pel Campió Revali sobrevolant el cel d'Hebra."
    ),
    "divine-beast-vah-naboris": (
        "La Bèstia Divina del Tro en forma de camell cuirassat gegant, pilotada per la Campiona Urbosa al desert de Gerudo."
    ),
    "wind-temple": (
        "L'arca celestial llegendària que flota enmig de la tempesta de neu d'Hebra a Tears of the Kingdom. És el "
        "temple sagrat on Link i Tulin derroten Colgera per despertar el Savi del Vent."
    ),
    "fire-temple": (
        "L'antiga ciutat subterrània Zonai envoltada de lava al Subsòl sota la Muntanya de la Mort, on Link i Yunobo "
        "activen vagonetes i derroten Marbled Gohma."
    ),
    "water-temple": (
        "Un complex flotant d'estructures de baixa gravetat al cel de Lanayru que purifica les fonts d'aigua dels Zora "
        "després que Link i Sidon derroten Mucktorok."
    ),
    "lightning-temple": (
        "Una piràmide sepulcral massiva que emergeix de les tempestes de sorra del Desert Gerudo, on Link i Riju "
        "projecten llum per vèncer la Reina Gibdo."
    ),
    "spirit-temple": (
        "Un temple amagat a les profunditats del Subsòl on Link i Mineru construeixen i activen el Golem de l'Esperit "
        "per enfrontar-se al Seized Construct corrupte."
    ),
    "typhlo-ruins": (
        "Unes ruïnes misterioses cobertes per una foscor impenetrable al nord del Gran Bosc de Hyrule, plenes de "
        "mecanismes Zonai que responen als poders dels quatre Savis."
    ),
    "sheikah-tower": (
        "Torres ancestrals que emergiren de la terra a Breath of the Wild per cartografiar cadascuna de les regions "
        "i actuar com a punts de teletransport i observació."
    ),
    "skyview-tower": (
        "Torres d'observació llançadores inventades per Purah a Tears of the Kingdom. Propulsen en Link cap a l'estratosfera "
        "per escanejar el mapa terrestre i celestial alhora."
    ),
    "ancient-shrine": (
        "Santuaris de prova dissenyats pels monjos Sheikah fa 10.000 anys. Proposen desafiaments d'enginy i combat "
        "a canvi d'orbes espirituals per millorar cors i resistència."
    ),
    "shrine-of-light": (
        "Santuaris celestials i terrestres creats per la llum sagrada de Rauru i Sonia a Tears of the Kingdom que purifiquen "
        "el mal i atorguen Llums de Benedicció a en Link."
    ),
    "lightroot": (
        "Arrels lluminoses gegantines que connecten amb els santuaris de la superfície. En activar-les al Subsòl, "
        "irradien llum que dissipa la foscor eterna i guareix els cors malmesos pel Fang."
    ),

    # --------------------------------------------------------------------- JOCS
    "the-legend-of-zelda-breath-of-the-wild": (
        "El revolucionari joc de món obert llançat el 2017 per a Nintendo Switch i Wii U. Redefineix la saga amb "
        "física interactiva, escalada lliure, supervivència i l'exploració sense límits d'un regne d'Hyrule en runes "
        "després de la Gran Calamitat."
    ),
    "the-master-trials": (
        "El primer paquet de contingut descarregable (DLC) de Breath of the Wild. Inclou el repte del Santuari de l'Espasa "
        "(Trial of the Sword) per desbloquejar el poder permanent de la Master Sword, el Mode Expert i la Màscara de Korok."
    ),
    "the-champions-ballad": (
        "El segon paquet de contingut descarregable (DLC) de Breath of the Wild. Aprofundeix en la història dels quatre "
        "Campions d'Hyrule amb noves masmorres, el repte del 'One-Hit Obliterator' i el vehicle Màquina Heroica (Master Cycle Zero)."
    ),
    "the-legend-of-zelda-tears-of-the-kingdom": (
        "La monumental seqüela directa de Breath of the Wild estrenada el 2023. Expandeix Hyrule cap a les illes celestes "
        "i les profunditats del Subsòl, introduint habilitats creatives sense precedents com Ultrahand, Fuse, Ascend i Recall."
    ),

    # --------------------------------------------------------------------- CAPS
    "calamity-ganon": (
        "L'encarnació del mal ancestral que va devastar Hyrule fa cent anys. Va prendre el control de les Bèsties Divines "
        "i els Guardians mecànics. Link el combat al Santuari del Castell de Hyrule en una forma monstruosa bio-mecànica."
    ),
    "dark-beast-ganon": (
        "La forma final i col·lossal de Calamity Ganon, manifestada com un senglar gegant d'odi i rancor pur a la plana "
        "d'Hyrule. Només pot ser derrotat disparant fletxes de llum amb l'Arc de la Llum atorgat per Zelda."
    ),
    "demon-king-ganondorf": (
        "La veritable forma de Ganondorf restaurada després de trencar el segell de Rauru. Mestre de les armes i la "
        "màgia fosca, desferma el Cataclisme a Tears of the Kingdom i combat Link amb un duel de simitarres i llances."
    ),
    "demon-dragon": (
        "La darrera transformació desesperada de Ganondorf en empassar-se la seva Pedra Secreta, convertint-se en un "
        "drac colossal negre i vermell d'odi pur que combat el Drac de la Llum i en Link al cel nocturn d'Hyrule."
    ),
    "phantom-ganon": (
        "Una aparició espectral fosca i letal creada pel poder del Fang de Ganondorf. Emergeix quan Link derrota les "
        "Mans de Fang (Gloom Hands) i ataca ràpidament amb armes impregnades de corrupció."
    ),
    "thunderblight-ganon": (
        "L'Ira del Tro de Ganon que va conquerir la Bèstia Divina Vah Naboris i va assassinar la Campiona Urbosa fa cent anys. "
        "És el cap més ràpid i esquiu, armat amb escut i espasa electritzada."
    ),
    "fireblight-ganon": (
        "L'Ira del Foc de Ganon que va infestar la Bèstia Divina Vah Rudania a la Muntanya de la Mort, causant la caiguda "
        "del Campió Daruk amb el seu mandoble gegant i boles de foc."
    ),
    "waterblight-ganon": (
        "L'Ira de l'Aigua de Ganon que va usurpar Vah Ruta i va matar la Campiona Mipha. Ataca Link amb una llança llarga "
        "i llança blocs de gel que han de ser destruïts amb Cryonis."
    ),
    "windblight-ganon": (
        "L'Ira del Vent de Ganon que va prendre Vah Medoh al cel d'Hebra, derrotant el Campió Revali amb canons d'energia "
        "i drons reflectidors guiats per tornados."
    ),
    "monk-maz-koshia": (
        "El mestre monjo Sheikah ancestral i guardià final del repte 'The Champions' Ballad'. Avalua la vàlua de Link "
        "en un combat èpic utilitzant multiplicació corporal, clons i un gegant Sheikah."
    ),
    "colgera": (
        "El colossal monstre volador glaçat que mantenia congelada la regió d'Hebra des del Temple del Vent. Link i Tulin "
        "el derroten planant i disparant fletxes directament a les seves membranes de gel dorsal."
    ),
    "moragia": (
        "Un monstre gegant de roca volcànica que emergeix del cràter de la Muntanya de la Mort a Tears of the Kingdom, "
        "derrotat per Link i Yunobo disparant-se des d'un vehicle aeri Zonai."
    ),
    "marbled-gohma": (
        "La reina monstruosa de roca marbrada al cor del Temple del Foc. Llança bombes de roca gegants que Yunobo ha "
        "de destruir amb la seva càrrega rodant per tombar les seves potes."
    ),
    "sludge-like": (
        "Una variant gegant de Like Like corrompuda pel fang que ataca Link i Sidon al Parc de Mipha abans d'accedir "
        "al Temple de l'Aigua."
    ),
    "mucktorok": (
        "Un petit i burleta monstre pop que neda en un tauró gegant de fang al Temple de l'Aigua. Només pot ser colpejat "
        "quan Sidon neteja el fang amb aigua pura."
    ),
    "queen-gibdo": (
        "La temible reina insectoide blindada que assetjava la Ciutat Gerudo des del Temple del Llamp. Només la llum "
        "solar i els llamps de Riju poden desfer la seva cuirassa blanca impenetrable."
    ),
    "seized-construct": (
        "Un golem ancestral Zonai corromput pel fang fosc al Temple de l'Esperit. Link i Mineru l'enfronten en un ring "
        "electrificat utilitzant els punys i canons del seu propi Golem."
    ),
    "hinox": (
        "Gegants cíclops que dormen plàcidament pels boscos i planes d'Hyrule. Porten un collaret ple d'armes i el seu "
        "únic punt feble és l'ull, que es protegeixen amb les mans en ser atacats."
    ),
    "blue-hinox": (
        "Una variant més forta de Hinox amb proteccions de fusta o metall a les cames per evitar atacs directes i un "
        "collaret amb armes de millor qualitat."
    ),
    "black-hinox": (
        "La variant més poderosa de Hinox abans del mode expert, amb defenses de ferro a les cames i un arsenal de "
        "cavaller o de la guàrdia reial penjat al coll."
    ),
    "stalnox": (
        "La versió esquelètica i no-morta d'un Hinox que només es desperta a la nit. Quan la seva salut cau, el seu ull "
        "es desprèn i Link ha de perseguir-lo abans que torni al cos."
    ),
    "stone-talus": (
        "Monstres gegants de pedra mimetitzats com a munts de roques a terra. S'aixequen en apropar-s'hi i només poden "
        "ser danyats colpejant el jaciment de mineral que tenen al capdamunt."
    ),
    "stone-talus-luminous": (
        "Variant de Talus amb un dipòsit de pedra lluminosa a l'esquena, que brilla intensament a la nit i deixa anar "
        "valuoses gemmes en ser derrotat."
    ),
    "stone-talus-rare": (
        "Variant de Talus que porta un jaciment de gemmes rares (diamants, robins, safirs) i ofereix el botí mineral "
        "més valuós del joc."
    ),
    "igneo-talus": (
        "Gegant de roca magmàtica incandescent que crema Link al contacte. Cal refredar-lo prèviament amb fletxes de gel "
        "o aigua abans de poder grimpar-hi."
    ),
    "frost-talus": (
        "Gegant de gel permanent que congela qualsevol que s'hi acosti. Cal fondre la seva capa exterior amb foc o fletxes "
        "calentes per escalar-lo."
    ),
    "battle-talus": (
        "Un Stone Talus que a Tears of the Kingdom ha estat convertit en una fortalesa mòbil per bokoblins, amb bastides "
        "i plataformes de fusta des d'on disparen fletxes."
    ),
    "molduga": (
        "Colossals balenes de sorra carnívores que neden sota les dunes del desert de Gerudo. Cegues però extremadament "
        "sensibles a les vibracions, ataquen qualsevol que camini sobre la sorra."
    ),
    "molduking": (
        "El rei ancestral dels Molduga introduït al DLC 'The Champions' Ballad'. Més ràpid, resistent i amb una pell "
        "reforçada per ferro."
    ),
    "flame-gleeok": (
        "Un temible drac de tres caps que escup foc i boles de lava a Tears of the Kingdom. Controla els corrents d'aire "
        "calent i cal disparar a cadascun dels tres caps per fer-lo caure."
    ),
    "frost-gleeok": (
        "Variant glaçada de Gleeok que habita a les cimeres d'Hebra i Gerudo. Desferma tempestes de neu i estalactites "
        "gegants de gel que cauen del cel."
    ),
    "thunder-gleeok": (
        "La variant elèctrica de Gleeok, que dispara raigs i llamps continus. És immune al xoc elèctric i exigeix "
        "armadures aïllants."
    ),
    "king-gleeok": (
        "La bèstia més temible d'Hyrule: un Gleeok de tres caps elementals diferents (Foc, Gel i Llamp) que habita "
        "a les illes celestes més remotes i a les profunditats del Subsòl."
    ),
    "frox": (
        "Gegants amfibis de les profunditats del Subsòl amb un sol ull i una boca immensa capaç de devorar mineral "
        "de Zonani. Llançar-los bombes a la boca els atordeix."
    ),
    "flux-construct-i": (
        "Un autòmat gegant modular de cubs Zonai que canvia de forma contínuament (humanoide, cub rodant, plataforma voladora). "
        "Cal localitzar el cub lluminós que actua com a nucli."
    ),
    "flux-construct-ii": (
        "Versió reforçada de Flux Construct amb atacs més ràpids i cubs que s'intercanvien de posició per protegir el nucli."
    ),
    "flux-construct-iii": (
        "La versió més letal de Flux Construct, que llança cubs a gran velocitat i exigeix desmuntar-ne les peces amb Ultrahand."
    ),
    "igneo-talus-titan": (
        "Una subespècie colossal d'Igneo Talus camuflada com a roca fosa incandescent a l'interior d'un llac de lava. "
        "Introduït al DLC 'The Champions' Ballad', cal utilitzar corrents ascendents d'aire per aterrar al seu damunt "
        "i colpejar el seu jaciment de mineral."
    ),
    "obsidian-frox": (
        "Variant fosca de Frox que habita a les profunditats més remotes del Subsòl. Compta amb unes potes encara "
        "més potents que les del Frox comú i dipòsits de mineral d'alta duresa a l'esquena."
    ),
    "blue-white-frox": (
        "La variant més resistent i poderosa de Frox del Subsòl. Utilitza els dipòsits de mineral lluminós del seu "
        "llom com a esquer per atreure preses i té l'habilitat d'espolsar-se qualsevol atacant saltant violentament."
    ),
    "ore-deposit": (
        "Jaciment de mineral comú abundant a les parets rocoses d'Hyrule. Trencar la roca amb armes contundents "
        "o bombes proporciona sal gemma, sílex i pedres d'ambre."
    ),
    "rare-ore-deposit": (
        "Dipòsit de mineral valuós amb vetes daurades. En trencar-lo s'obtenen gemmes precioses d'alta qualitat "
        "com robins, safirs, topacis i diamants."
    ),
    "luminous-stone-deposit": (
        "Jaciment de pedra lluminosa que brilla intensament amb una resplendor blavosa en la foscor de la nit "
        "i a les coves d'Hyrule."
    ),
    "zonaite-deposit": (
        "Jaciment de mineral de Zonani propi de les profunditats del Subsòl i les illes celestes. La seva energia "
        "verda és fonamental per forjar càrregues i millorar la bateria Zonai."
    ),
    "well": (
        "Pous excavats a terra per extreure aigua subterrània, situats a prop de pobles, postes i ruïnes d'Hyrule. "
        "A Tears of the Kingdom amaguen coves secretes, cofres i recursos valuosos."
    ),
    "treasure-chest": (
        "Cofres del tresor distribuïts per tot el regne d'Hyrule, santuaris ancestrals, campaments enemics "
        "i coves subterrànies. Contenen des de rupies i gemmes precioses fins a armes d'alt nivell, "
        "materials de construcció i peces d'equipament úniques."
    ),
}

