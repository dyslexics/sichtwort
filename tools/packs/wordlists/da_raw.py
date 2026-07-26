# -*- coding: utf-8 -*-
# Grundwortschatz Dänisch (da) für Sichtwort — Rohliste (Checkpoint), genau 500 Wörter
# (wort, typ)  typ: n=Nomen, v=Verb, a=Adjektiv, o=Sonstiges

WORDS = [
    # === o: Pronomen / Begleiter (35) ===
    ("jeg", "o"), ("du", "o"), ("han", "o"), ("hun", "o"), ("den", "o"),
    ("det", "o"), ("vi", "o"), ("de", "o"), ("mig", "o"), ("dig", "o"),
    ("ham", "o"), ("hende", "o"), ("os", "o"), ("jer", "o"), ("dem", "o"),
    ("min", "o"), ("mit", "o"), ("mine", "o"), ("din", "o"), ("dit", "o"),
    ("dine", "o"), ("hans", "o"), ("hendes", "o"), ("vores", "o"), ("jeres", "o"),
    ("deres", "o"), ("sin", "o"), ("sit", "o"), ("sine", "o"), ("en", "o"),
    ("et", "o"), ("denne", "o"), ("dette", "o"), ("disse", "o"), ("selv", "o"),

    # === o: Frage- und Bindewörter (23) ===
    ("hvor", "o"), ("hvornår", "o"), ("hvordan", "o"), ("hvorfor", "o"),
    ("hvem", "o"), ("hvad", "o"), ("hvilken", "o"), ("når", "o"), ("da", "o"),
    ("hvis", "o"), ("fordi", "o"), ("men", "o"), ("og", "o"), ("eller", "o"),
    ("at", "o"), ("som", "o"), ("så", "o"), ("end", "o"), ("både", "o"),
    ("enten", "o"), ("dog", "o"), ("mens", "o"), ("siden", "o"),

    # === o: Adverbien / Partikeln (41) ===
    ("her", "o"), ("der", "o"), ("ja", "o"), ("nej", "o"), ("ikke", "o"),
    ("også", "o"), ("kun", "o"), ("meget", "o"), ("mere", "o"), ("mest", "o"),
    ("lidt", "o"), ("mange", "o"), ("alle", "o"), ("alt", "o"), ("ingen", "o"),
    ("intet", "o"), ("noget", "o"), ("nogen", "o"), ("nogle", "o"), ("hver", "o"),
    ("hele", "o"), ("sammen", "o"), ("igen", "o"), ("altid", "o"), ("aldrig", "o"),
    ("ofte", "o"), ("nu", "o"), ("snart", "o"), ("sent", "o"), ("måske", "o"),
    ("næsten", "o"), ("helt", "o"), ("lige", "o"), ("bare", "o"), ("nok", "o"),
    ("endnu", "o"), ("allerede", "o"), ("sådan", "o"), ("jo", "o"), ("vel", "o"),
    ("gerne", "o"),

    # === o: Präpositionen / Richtungen (30) ===
    ("i", "o"), ("på", "o"), ("til", "o"), ("fra", "o"), ("med", "o"),
    ("uden", "o"), ("om", "o"), ("over", "o"), ("under", "o"), ("ved", "o"),
    ("af", "o"), ("for", "o"), ("mod", "o"), ("efter", "o"), ("før", "o"),
    ("mellem", "o"), ("bag", "o"), ("foran", "o"), ("ind", "o"), ("ud", "o"),
    ("op", "o"), ("ned", "o"), ("hjem", "o"), ("ude", "o"), ("inde", "o"),
    ("oppe", "o"), ("nede", "o"), ("hen", "o"), ("frem", "o"), ("tilbage", "o"),

    # === o: Zahlen (12) ===
    ("to", "o"), ("tre", "o"), ("fire", "o"), ("fem", "o"), ("seks", "o"),
    ("syv", "o"), ("otte", "o"), ("ni", "o"), ("ti", "o"), ("første", "o"),
    ("anden", "o"), ("tredje", "o"),

    # === o: Höflichkeit (4) ===
    ("hej", "o"), ("farvel", "o"), ("tak", "o"), ("undskyld", "o"),

    # === v: Verben (115) ===
    ("være", "v"), ("have", "v"), ("gøre", "v"), ("sige", "v"), ("se", "v"),
    ("gå", "v"), ("komme", "v"), ("få", "v"), ("give", "v"), ("tage", "v"),
    ("vide", "v"), ("kunne", "v"), ("ville", "v"), ("skulle", "v"), ("måtte", "v"),
    ("blive", "v"), ("stå", "v"), ("ligge", "v"), ("sidde", "v"), ("løbe", "v"),
    ("springe", "v"), ("hoppe", "v"), ("danse", "v"), ("synge", "v"), ("spille", "v"),
    ("lege", "v"), ("læse", "v"), ("skrive", "v"), ("tegne", "v"), ("male", "v"),
    ("tælle", "v"), ("regne", "v"), ("lære", "v"), ("tænke", "v"), ("huske", "v"),
    ("glemme", "v"), ("forstå", "v"), ("høre", "v"), ("lytte", "v"), ("tale", "v"),
    ("snakke", "v"), ("spørge", "v"), ("svare", "v"), ("råbe", "v"), ("grine", "v"),
    ("græde", "v"), ("smile", "v"), ("sove", "v"), ("vågne", "v"), ("drømme", "v"),
    ("spise", "v"), ("drikke", "v"), ("bage", "v"), ("koge", "v"), ("lave", "v"),
    ("bygge", "v"), ("hjælpe", "v"), ("arbejde", "v"), ("købe", "v"), ("sælge", "v"),
    ("betale", "v"), ("finde", "v"), ("åbne", "v"), ("lukke", "v"), ("banke", "v"),
    ("ringe", "v"), ("vinke", "v"), ("kysse", "v"), ("kramme", "v"), ("holde", "v"),
    ("kaste", "v"), ("trække", "v"), ("bære", "v"), ("hente", "v"), ("sende", "v"),
    ("lægge", "v"), ("sætte", "v"), ("samle", "v"), ("dele", "v"), ("passe", "v"),
    ("vaske", "v"), ("klippe", "v"), ("pakke", "v"), ("rejse", "v"), ("køre", "v"),
    ("cykle", "v"), ("flyve", "v"), ("svømme", "v"), ("klatre", "v"), ("falde", "v"),
    ("bo", "v"), ("leve", "v"), ("vokse", "v"), ("begynde", "v"), ("starte", "v"),
    ("slutte", "v"), ("stoppe", "v"), ("vente", "v"), ("prøve", "v"), ("vinde", "v"),
    ("slå", "v"), ("kigge", "v"), ("vise", "v"), ("følge", "v"), ("møde", "v"),
    ("ønske", "v"), ("håbe", "v"), ("elske", "v"), ("tro", "v"), ("føle", "v"),
    ("smage", "v"), ("fryse", "v"), ("brænde", "v"), ("tænde", "v"), ("slukke", "v"),

    # === a: Adjektive (75) ===
    ("stor", "a"), ("lille", "a"), ("lang", "a"), ("kort", "a"), ("høj", "a"),
    ("lav", "a"), ("tyk", "a"), ("tynd", "a"), ("bred", "a"), ("smal", "a"),
    ("ny", "a"), ("gammel", "a"), ("ung", "a"), ("god", "a"), ("dårlig", "a"),
    ("glad", "a"), ("ked", "a"), ("sur", "a"), ("vred", "a"), ("bange", "a"),
    ("modig", "a"), ("sjov", "a"), ("kedelig", "a"), ("dejlig", "a"), ("flot", "a"),
    ("pæn", "a"), ("grim", "a"), ("ren", "a"), ("beskidt", "a"), ("våd", "a"),
    ("tør", "a"), ("varm", "a"), ("kold", "a"), ("hurtig", "a"), ("langsom", "a"),
    ("stærk", "a"), ("svag", "a"), ("tung", "a"), ("let", "a"), ("hård", "a"),
    ("blød", "a"), ("sød", "a"), ("tom", "a"), ("fuld", "a"), ("åben", "a"),
    ("lukket", "a"), ("klar", "a"), ("mørk", "a"), ("rigtig", "a"), ("forkert", "a"),
    ("nem", "a"), ("svær", "a"), ("sulten", "a"), ("træt", "a"), ("frisk", "a"),
    ("syg", "a"), ("rask", "a"), ("venlig", "a"), ("dyr", "a"), ("farlig", "a"),
    ("stille", "a"), ("vigtig", "a"), ("rund", "a"), ("skarp", "a"),
    ("rød", "a"), ("blå", "a"), ("grøn", "a"), ("gul", "a"), ("sort", "a"),
    ("hvid", "a"), ("brun", "a"), ("grå", "a"), ("lyserød", "a"), ("orange", "a"),
    ("lilla", "a"),

    # === n: Familie & Menschen (17) ===
    ("mor", "n"), ("far", "n"), ("barn", "n"), ("dreng", "n"), ("pige", "n"),
    ("bror", "n"), ("søster", "n"), ("bedstemor", "n"), ("bedstefar", "n"),
    ("familie", "n"), ("mand", "n"), ("kvinde", "n"), ("ven", "n"), ("navn", "n"),
    ("fødselsdag", "n"), ("onkel", "n"), ("tante", "n"),

    # === n: Schule (18) ===
    ("skole", "n"), ("klasse", "n"), ("lærer", "n"), ("bog", "n"), ("blyant", "n"),
    ("papir", "n"), ("taske", "n"), ("bord", "n"), ("stol", "n"), ("pause", "n"),
    ("time", "n"), ("ord", "n"), ("bogstav", "n"), ("tal", "n"), ("farve", "n"),
    ("spil", "n"), ("leg", "n"), ("billede", "n"),

    # === n: Tiere (19) ===
    ("hund", "n"), ("kat", "n"), ("hest", "n"), ("ko", "n"), ("gris", "n"),
    ("får", "n"), ("høne", "n"), ("and", "n"), ("fugl", "n"), ("fisk", "n"),
    ("mus", "n"), ("kanin", "n"), ("ræv", "n"), ("bjørn", "n"), ("løve", "n"),
    ("slange", "n"), ("frø", "n"), ("bi", "n"), ("sommerfugl", "n"),

    # === n: Essen & Trinken (17) ===
    ("mad", "n"), ("brød", "n"), ("smør", "n"), ("ost", "n"), ("mælk", "n"),
    ("vand", "n"), ("saft", "n"), ("kage", "n"), ("is", "n"), ("slik", "n"),
    ("frugt", "n"), ("æble", "n"), ("banan", "n"), ("kartoffel", "n"),
    ("suppe", "n"), ("kød", "n"), ("æg", "n"),

    # === n: Körper (14) ===
    ("krop", "n"), ("hoved", "n"), ("hår", "n"), ("øje", "n"), ("øre", "n"),
    ("næse", "n"), ("mund", "n"), ("tand", "n"), ("arm", "n"), ("hånd", "n"),
    ("finger", "n"), ("mave", "n"), ("ben", "n"), ("fod", "n"),

    # === n: Natur & Wetter (17) ===
    ("sol", "n"), ("måne", "n"), ("stjerne", "n"), ("himmel", "n"), ("sky", "n"),
    ("regn", "n"), ("sne", "n"), ("vind", "n"), ("luft", "n"), ("ild", "n"),
    ("jord", "n"), ("sø", "n"), ("hav", "n"), ("strand", "n"), ("skov", "n"),
    ("træ", "n"), ("blomst", "n"),

    # === n: Haus & Dinge (20) ===
    ("hus", "n"), ("dør", "n"), ("vindue", "n"), ("væg", "n"), ("gulv", "n"),
    ("tag", "n"), ("køkken", "n"), ("seng", "n"), ("pude", "n"), ("lampe", "n"),
    ("lys", "n"), ("skab", "n"), ("nøgle", "n"), ("ur", "n"), ("telefon", "n"),
    ("kop", "n"), ("glas", "n"), ("kniv", "n"), ("ske", "n"), ("bold", "n"),

    # === n: Kleidung (8) ===
    ("tøj", "n"), ("trøje", "n"), ("bukser", "n"), ("kjole", "n"), ("strømpe", "n"),
    ("sko", "n"), ("jakke", "n"), ("hat", "n"),

    # === n: Stadt & Verkehr (18) ===
    ("by", "n"), ("gade", "n"), ("vej", "n"), ("bro", "n"), ("park", "n"),
    ("butik", "n"), ("kirke", "n"), ("hospital", "n"), ("læge", "n"),
    ("politi", "n"), ("bil", "n"), ("bus", "n"), ("tog", "n"), ("cykel", "n"),
    ("båd", "n"), ("fly", "n"), ("penge", "n"), ("gave", "n"),

    # === n: Zeit (17) ===
    ("dag", "n"), ("nat", "n"), ("morgen", "n"), ("aften", "n"), ("uge", "n"),
    ("år", "n"), ("sommer", "n"), ("vinter", "n"), ("jul", "n"), ("ferie", "n"),
    ("mandag", "n"), ("tirsdag", "n"), ("onsdag", "n"), ("torsdag", "n"),
    ("fredag", "n"), ("lørdag", "n"), ("søndag", "n"),
]
