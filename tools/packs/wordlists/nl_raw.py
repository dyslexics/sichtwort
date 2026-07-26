# -*- coding: utf-8 -*-
# Checkpoint: Grundwortschatz Niederländisch (Standard-Niederländisch NL)
# 500 häufige Wörter des niederländischen Lese-Erstunterrichts, kindgerecht.
# Typen: n=Nomen, v=Verb, a=Adjektiv, o=Sonstiges (Funktionswörter, Zahlen, Adverbien)
# Verteilung: o=155, v=95, a=80, n=170

WORDS = [
    # === SONSTIGE (o) ===
    # Artikel, Konjunktionen, Frageworter, Pronomen
    ("de", "o"), ("het", "o"), ("een", "o"), ("en", "o"), ("of", "o"),
    ("maar", "o"), ("want", "o"), ("dus", "o"), ("omdat", "o"), ("als", "o"),
    ("ook", "o"), ("niet", "o"), ("wel", "o"), ("ja", "o"), ("nee", "o"),
    ("wat", "o"), ("wie", "o"), ("waar", "o"), ("wanneer", "o"), ("hoe", "o"),
    ("waarom", "o"), ("welke", "o"),
    ("deze", "o"), ("die", "o"), ("dit", "o"), ("dat", "o"),
    ("hier", "o"), ("daar", "o"),
    ("ik", "o"), ("jij", "o"), ("hij", "o"), ("zij", "o"), ("wij", "o"),
    ("jullie", "o"), ("mij", "o"), ("jou", "o"), ("hem", "o"), ("haar", "o"),
    ("ons", "o"), ("hun", "o"), ("mijn", "o"), ("jouw", "o"), ("onze", "o"),
    ("u", "o"), ("me", "o"), ("je", "o"), ("ze", "o"), ("we", "o"), ("er", "o"),
    ("al", "o"), ("alle", "o"), ("allemaal", "o"), ("elke", "o"), ("ieder", "o"),
    ("iets", "o"), ("niets", "o"), ("iemand", "o"), ("niemand", "o"),
    # Zeit / Haufigkeit
    ("altijd", "o"), ("nooit", "o"), ("soms", "o"), ("vaak", "o"), ("steeds", "o"),
    ("nu", "o"), ("dan", "o"), ("toen", "o"), ("straks", "o"), ("daarna", "o"),
    ("eerst", "o"), ("morgen", "o"), ("gisteren", "o"), ("vandaag", "o"),
    ("weer", "o"), ("nog", "o"), ("bijna", "o"), ("meteen", "o"),
    # Grad / Modalpartikeln / Hoflichkeit
    ("meer", "o"), ("minder", "o"), ("veel", "o"), ("weinig", "o"),
    ("zo", "o"), ("heel", "o"), ("erg", "o"), ("even", "o"), ("net", "o"),
    ("pas", "o"), ("toch", "o"), ("misschien", "o"), ("natuurlijk", "o"),
    ("echt", "o"), ("samen", "o"), ("alleen", "o"), ("graag", "o"),
    ("hallo", "o"), ("sorry", "o"),
    # Praepositionen / Ortsangaben
    ("boven", "o"), ("onder", "o"), ("voor", "o"), ("achter", "o"), ("naast", "o"),
    ("tussen", "o"), ("in", "o"), ("uit", "o"), ("op", "o"), ("af", "o"),
    ("aan", "o"), ("bij", "o"), ("met", "o"), ("zonder", "o"), ("van", "o"),
    ("naar", "o"), ("tot", "o"), ("door", "o"), ("over", "o"), ("om", "o"),
    ("langs", "o"), ("tegen", "o"), ("binnen", "o"), ("buiten", "o"),
    ("links", "o"), ("rechts", "o"), ("omhoog", "o"), ("omlaag", "o"),
    ("terug", "o"), ("weg", "o"), ("thuis", "o"), ("overal", "o"),
    # Zahlen
    ("nul", "o"), ("twee", "o"), ("drie", "o"), ("vier", "o"), ("vijf", "o"),
    ("zes", "o"), ("zeven", "o"), ("acht", "o"), ("negen", "o"), ("tien", "o"),
    ("elf", "o"), ("twaalf", "o"), ("dertien", "o"), ("veertien", "o"),
    ("vijftien", "o"), ("zestien", "o"), ("zeventien", "o"), ("achttien", "o"),
    ("negentien", "o"), ("twintig", "o"), ("dertig", "o"), ("veertig", "o"),
    ("vijftig", "o"), ("honderd", "o"), ("duizend", "o"),
    ("eerste", "o"), ("tweede", "o"), ("derde", "o"),

    # === VERBEN (v), Infinitiv ===
    ("zijn", "v"), ("hebben", "v"), ("doen", "v"), ("gaan", "v"), ("komen", "v"),
    ("zien", "v"), ("kijken", "v"), ("horen", "v"), ("luisteren", "v"),
    ("praten", "v"), ("zeggen", "v"), ("vragen", "v"), ("antwoorden", "v"),
    ("roepen", "v"), ("lezen", "v"), ("schrijven", "v"), ("tekenen", "v"),
    ("kleuren", "v"), ("knippen", "v"), ("plakken", "v"), ("tellen", "v"),
    ("rekenen", "v"), ("leren", "v"), ("weten", "v"), ("denken", "v"),
    ("begrijpen", "v"), ("vergeten", "v"), ("willen", "v"), ("kunnen", "v"),
    ("moeten", "v"), ("mogen", "v"), ("zullen", "v"), ("laten", "v"),
    ("maken", "v"), ("bouwen", "v"), ("breken", "v"), ("vallen", "v"),
    ("staan", "v"), ("zitten", "v"), ("liggen", "v"), ("lopen", "v"),
    ("rennen", "v"), ("springen", "v"), ("klimmen", "v"), ("dansen", "v"),
    ("zingen", "v"), ("spelen", "v"), ("lachen", "v"), ("huilen", "v"),
    ("slapen", "v"), ("dromen", "v"), ("worden", "v"), ("eten", "v"),
    ("drinken", "v"), ("koken", "v"), ("bakken", "v"), ("ruiken", "v"),
    ("voelen", "v"), ("pakken", "v"), ("geven", "v"), ("nemen", "v"),
    ("brengen", "v"), ("halen", "v"), ("dragen", "v"), ("duwen", "v"),
    ("trekken", "v"), ("gooien", "v"), ("vangen", "v"), ("houden", "v"),
    ("zoeken", "v"), ("vinden", "v"), ("verliezen", "v"), ("winnen", "v"),
    ("helpen", "v"), ("werken", "v"), ("wachten", "v"), ("wonen", "v"),
    ("rijden", "v"), ("fietsen", "v"), ("zwemmen", "v"), ("vliegen", "v"),
    ("wassen", "v"), ("opruimen", "v"), ("kopen", "v"), ("betalen", "v"),
    ("openen", "v"), ("sluiten", "v"), ("beginnen", "v"), ("stoppen", "v"),
    ("blijven", "v"), ("knuffelen", "v"), ("delen", "v"), ("groeien", "v"),
    ("proberen", "v"), ("hopen", "v"),

    # === ADJEKTIVE (a) ===
    ("groot", "a"), ("klein", "a"), ("lang", "a"), ("kort", "a"), ("hoog", "a"),
    ("laag", "a"), ("dik", "a"), ("dun", "a"), ("breed", "a"), ("smal", "a"),
    ("oud", "a"), ("jong", "a"), ("nieuw", "a"), ("mooi", "a"), ("lelijk", "a"),
    ("lief", "a"), ("stout", "a"), ("blij", "a"), ("boos", "a"), ("bang", "a"),
    ("verdrietig", "a"), ("moe", "a"), ("ziek", "a"), ("gezond", "a"),
    ("sterk", "a"), ("zwak", "a"), ("snel", "a"), ("langzaam", "a"),
    ("warm", "a"), ("koud", "a"), ("heet", "a"), ("nat", "a"), ("droog", "a"),
    ("vies", "a"), ("schoon", "a"), ("donker", "a"), ("zwaar", "a"),
    ("vol", "a"), ("leeg", "a"), ("hard", "a"), ("zacht", "a"), ("scherp", "a"),
    ("rond", "a"), ("recht", "a"), ("zoet", "a"), ("lekker", "a"),
    ("slim", "a"), ("dom", "a"), ("grappig", "a"), ("druk", "a"), ("stil", "a"),
    ("rustig", "a"), ("wild", "a"), ("gek", "a"), ("raar", "a"), ("leuk", "a"),
    ("fijn", "a"), ("goed", "a"), ("slecht", "a"), ("makkelijk", "a"),
    ("moeilijk", "a"), ("knap", "a"), ("vriendelijk", "a"), ("klaar", "a"),
    ("open", "a"), ("dicht", "a"), ("veilig", "a"), ("wakker", "a"), ("stuk", "a"),
    ("rood", "a"), ("blauw", "a"), ("geel", "a"), ("groen", "a"), ("zwart", "a"),
    ("wit", "a"), ("bruin", "a"), ("grijs", "a"), ("roze", "a"), ("paars", "a"),
    ("oranje", "a"),

    # === NOMEN (n) ===
    # Familie und Menschen
    ("moeder", "n"), ("vader", "n"), ("mama", "n"), ("papa", "n"),
    ("oma", "n"), ("opa", "n"), ("broer", "n"), ("zus", "n"), ("kind", "n"),
    ("familie", "n"), ("man", "n"), ("vrouw", "n"), ("jongen", "n"),
    ("meisje", "n"), ("vriend", "n"), ("vriendin", "n"), ("naam", "n"),
    ("dokter", "n"),
    # Schule
    ("school", "n"), ("juf", "n"), ("meester", "n"), ("klas", "n"), ("les", "n"),
    ("boek", "n"), ("pen", "n"), ("potlood", "n"), ("tas", "n"), ("bord", "n"),
    ("stoel", "n"), ("tafel", "n"), ("letter", "n"), ("woord", "n"), ("zin", "n"),
    ("verhaal", "n"), ("vraag", "n"), ("antwoord", "n"),
    # Tiere
    ("dier", "n"), ("hond", "n"), ("kat", "n"), ("poes", "n"), ("muis", "n"),
    ("paard", "n"), ("koe", "n"), ("schaap", "n"), ("kip", "n"), ("eend", "n"),
    ("vogel", "n"), ("vis", "n"), ("konijn", "n"), ("olifant", "n"),
    ("leeuw", "n"), ("aap", "n"), ("beer", "n"), ("vos", "n"), ("kikker", "n"),
    ("ei", "n"),
    # Essen, Trinken, Kueche
    ("brood", "n"), ("boter", "n"), ("kaas", "n"), ("melk", "n"), ("water", "n"),
    ("suiker", "n"), ("appel", "n"), ("peer", "n"), ("banaan", "n"),
    ("tomaat", "n"), ("wortel", "n"), ("aardappel", "n"), ("soep", "n"),
    ("vlees", "n"), ("koek", "n"), ("taart", "n"), ("snoep", "n"), ("ijs", "n"),
    ("boterham", "n"), ("glas", "n"), ("lepel", "n"), ("vork", "n"), ("mes", "n"),
    ("keuken", "n"),
    # Koerper
    ("hoofd", "n"), ("gezicht", "n"), ("oog", "n"), ("oor", "n"), ("neus", "n"),
    ("mond", "n"), ("tand", "n"), ("tong", "n"), ("arm", "n"), ("hand", "n"),
    ("vinger", "n"), ("buik", "n"), ("rug", "n"), ("been", "n"), ("voet", "n"),
    ("knie", "n"), ("hart", "n"), ("lichaam", "n"),
    # Haus und Wohnen
    ("huis", "n"), ("deur", "n"), ("raam", "n"), ("muur", "n"), ("dak", "n"),
    ("trap", "n"), ("kamer", "n"), ("bed", "n"), ("kast", "n"), ("bank", "n"),
    ("lamp", "n"), ("licht", "n"), ("sleutel", "n"), ("klok", "n"),
    ("kussen", "n"), ("tuin", "n"),
    # Natur, Wetter, Zeit
    ("boom", "n"), ("blad", "n"), ("bloem", "n"), ("gras", "n"), ("plant", "n"),
    ("bos", "n"), ("berg", "n"), ("zee", "n"), ("strand", "n"), ("zand", "n"),
    ("steen", "n"), ("lucht", "n"), ("wolk", "n"), ("zon", "n"), ("maan", "n"),
    ("ster", "n"), ("regen", "n"), ("sneeuw", "n"), ("wind", "n"), ("vuur", "n"),
    ("winter", "n"), ("zomer", "n"), ("dag", "n"), ("nacht", "n"), ("avond", "n"),
    ("jaar", "n"),
    # Verkehr, Stadt, Dinge
    ("auto", "n"), ("fiets", "n"), ("bus", "n"), ("trein", "n"), ("boot", "n"),
    ("vliegtuig", "n"), ("straat", "n"), ("stad", "n"), ("dorp", "n"),
    ("winkel", "n"), ("geld", "n"), ("brief", "n"), ("telefoon", "n"),
    ("film", "n"), ("muziek", "n"), ("lied", "n"), ("spel", "n"), ("bal", "n"),
    ("pop", "n"), ("speelgoed", "n"), ("feest", "n"), ("verjaardag", "n"),
    # Kleidung
    ("jas", "n"), ("broek", "n"), ("trui", "n"), ("jurk", "n"), ("rok", "n"),
    ("sok", "n"), ("schoen", "n"), ("muts", "n"),
]
