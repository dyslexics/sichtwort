# -*- coding: utf-8 -*-
"""Grundwortschatz Afrikaans (af) fuer Sichtwort - Rohliste.

Reihenfolge = Wichtigkeit fuer den Lese-Erstunterricht:
Funktionswoerter zuerst, dann haeufige Verben, dann Alltagsnomen, dann Adjektive.
Typen: n=Nomen, v=Verb, a=Adjektiv, o=Sonstiges (Funktionswoerter, Zahlen, Adverbien).
"""

WORDS = [
    # --- Artikel, Pronomen, Determinative ---
    ("die", "o"), ("ek", "o"), ("jy", "o"), ("hy", "o"), ("sy", "o"),
    ("ons", "o"), ("julle", "o"), ("hulle", "o"), ("dit", "o"), ("u", "o"),
    ("my", "o"), ("jou", "o"), ("hom", "o"), ("haar", "o"), ("myne", "o"),
    ("joune", "o"), ("syne", "o"), ("hare", "o"), ("onse", "o"), ("self", "o"),
    ("hierdie", "o"), ("daardie", "o"), ("elke", "o"), ("alle", "o"), ("al", "o"),
    ("sommige", "o"), ("ander", "o"), ("selfde", "o"), ("geen", "o"), ("niks", "o"),
    ("iets", "o"), ("alles", "o"), ("iemand", "o"), ("niemand", "o"), ("mekaar", "o"),

    # --- Fragewoerter ---
    ("wie", "o"), ("wat", "o"), ("waar", "o"), ("wanneer", "o"), ("hoekom", "o"),
    ("hoe", "o"), ("watter", "o"), ("hoeveel", "o"), ("waarom", "o"), ("waarheen", "o"),

    # --- Konjunktionen, Praepositionen ---
    ("en", "o"), ("of", "o"), ("maar", "o"), ("want", "o"), ("omdat", "o"),
    ("as", "o"), ("dan", "o"), ("toe", "o"), ("terwyl", "o"), ("sodat", "o"),
    ("hoewel", "o"), ("dat", "o"), ("in", "o"), ("op", "o"), ("by", "o"),
    ("met", "o"), ("van", "o"), ("na", "o"), ("uit", "o"), ("oor", "o"),
    ("onder", "o"), ("bo", "o"), ("langs", "o"), ("tussen", "o"), ("voor", "o"),
    ("agter", "o"), ("om", "o"), ("tot", "o"), ("teen", "o"), ("sonder", "o"),
    ("deur", "o"), ("vir", "o"), ("aan", "o"), ("af", "o"), ("binne", "o"),
    ("buite", "o"), ("naby", "o"), ("verby", "o"), ("rondom", "o"), ("saam", "o"),

    # --- Adverbien, kleine Woerter ---
    ("nie", "o"), ("ja", "o"), ("nee", "o"), ("ook", "o"), ("nog", "o"),
    ("altyd", "o"), ("nooit", "o"), ("dikwels", "o"), ("soms", "o"), ("weer", "o"),
    ("hier", "o"), ("daar", "o"), ("nou", "o"), ("gister", "o"), ("vandag", "o"),
    ("môre", "o"), ("gou", "o"), ("alleen", "o"), ("net", "o"), ("amper", "o"),
    ("dalk", "o"), ("seker", "o"), ("miskien", "o"), ("so", "o"), ("baie", "o"),
    ("min", "o"), ("meer", "o"), ("genoeg", "o"), ("byna", "o"), ("skielik", "o"),
    ("asseblief", "o"), ("dankie", "o"), ("hallo", "o"), ("totsiens", "o"), ("weg", "o"),
    ("terug", "o"), ("verder", "o"), ("saggies", "o"), ("hardop", "o"), ("regtig", "o"),

    # --- Zahlen ---
    ("nul", "o"), ("een", "o"), ("twee", "o"), ("drie", "o"), ("vier", "o"),
    ("vyf", "o"), ("ses", "o"), ("sewe", "o"), ("agt", "o"), ("nege", "o"),
    ("tien", "o"), ("elf", "o"), ("twaalf", "o"), ("dertien", "o"), ("twintig", "o"),
    ("dertig", "o"), ("honderd", "o"), ("duisend", "o"), ("eerste", "o"), ("laaste", "o"),

    # --- Hilfsverben und haeufigste Verben ---
    ("is", "v"), ("was", "v"), ("wees", "v"), ("het", "v"), ("kan", "v"),
    ("wil", "v"), ("moet", "v"), ("mag", "v"), ("sal", "v"), ("sou", "v"),
    ("word", "v"), ("gaan", "v"), ("kom", "v"), ("doen", "v"), ("maak", "v"),
    ("sien", "v"), ("kyk", "v"), ("hoor", "v"), ("luister", "v"), ("praat", "v"),
    ("vra", "v"), ("antwoord", "v"), ("dink", "v"), ("weet", "v"), ("ken", "v"),
    ("leer", "v"), ("lees", "v"), ("skryf", "v"), ("teken", "v"), ("tel", "v"),
    ("speel", "v"), ("loop", "v"), ("hardloop", "v"), ("spring", "v"), ("sit", "v"),
    ("staan", "v"), ("slaap", "v"), ("eet", "v"), ("drink", "v"), ("kook", "v"),
    ("help", "v"), ("gee", "v"), ("neem", "v"), ("vat", "v"), ("bring", "v"),
    ("dra", "v"), ("hou", "v"), ("val", "v"), ("klim", "v"), ("ry", "v"),
    ("vlieg", "v"), ("swem", "v"), ("sing", "v"), ("dans", "v"), ("lag", "v"),
    ("huil", "v"), ("roep", "v"), ("skree", "v"), ("soek", "v"), ("vind", "v"),
    ("kry", "v"), ("verloor", "v"), ("koop", "v"), ("verkoop", "v"), ("betaal", "v"),
    ("werk", "v"), ("rus", "v"), ("wag", "v"), ("begin", "v"), ("eindig", "v"),
    ("oopmaak", "v"), ("toemaak", "v"), ("breek", "v"), ("bou", "v"), ("plant", "v"),
    ("gooi", "v"), ("vang", "v"), ("druk", "v"), ("trek", "v"), ("stoot", "v"),
    ("skop", "v"), ("borsel", "v"), ("kam", "v"), ("aantrek", "v"), ("uittrek", "v"),
    ("waai", "v"), ("skyn", "v"), ("brand", "v"), ("groei", "v"), ("ruik", "v"),
    ("proe", "v"), ("voel", "v"), ("raak", "v"), ("stap", "v"), ("draai", "v"),
    ("bly", "v"), ("verstaan", "v"), ("onthou", "v"), ("vergeet", "v"), ("oefen", "v"),
    ("deel", "v"), ("wys", "v"), ("stuur", "v"), ("kies", "v"), ("kleur", "v"),
    ("verf", "v"), ("knip", "v"), ("plak", "v"), ("vou", "v"), ("pak", "v"),
    ("dek", "v"), ("vee", "v"), ("skoonmaak", "v"), ("herhaal", "v"), ("tik", "v"),
    ("klop", "v"), ("lek", "v"), ("byt", "v"), ("blaas", "v"), ("gaap", "v"),
    ("droom", "v"), ("wakker", "v"), ("opstaan", "v"), ("wegloop", "v"), ("terugkom", "v"),
    ("hardloop", "v"),

    # --- Familie und Menschen ---
    ("ma", "n"), ("pa", "n"), ("mamma", "n"), ("pappa", "n"), ("ouma", "n"),
    ("oupa", "n"), ("broer", "n"), ("suster", "n"), ("baba", "n"), ("kind", "n"),
    ("seun", "n"), ("dogter", "n"), ("man", "n"), ("vrou", "n"), ("mens", "n"),
    ("familie", "n"), ("ouers", "n"), ("oom", "n"), ("tannie", "n"), ("neef", "n"),
    ("niggie", "n"), ("vriend", "n"), ("vriendin", "n"), ("buurman", "n"), ("maat", "n"),
    ("dokter", "n"), ("boer", "n"), ("bakker", "n"), ("polisie", "n"), ("koning", "n"),

    # --- Schule ---
    ("skool", "n"), ("klas", "n"), ("juffrou", "n"), ("meneer", "n"), ("onderwyser", "n"),
    ("leerling", "n"), ("boek", "n"), ("bladsy", "n"), ("potlood", "n"), ("pen", "n"),
    ("papier", "n"), ("tas", "n"), ("bord", "n"), ("kryt", "n"), ("som", "n"),
    ("woord", "n"), ("letter", "n"), ("sin", "n"), ("storie", "n"), ("prent", "n"),
    ("gom", "n"), ("liniaal", "n"), ("huiswerk", "n"), ("vraag", "n"), ("naam", "n"),
    ("taal", "n"), ("nommer", "n"), ("reël", "n"), ("pouse", "n"), ("toets", "n"),

    # --- Haus und Wohnen ---
    ("huis", "n"), ("kamer", "n"), ("kombuis", "n"), ("badkamer", "n"), ("slaapkamer", "n"),
    ("tafel", "n"), ("stoel", "n"), ("venster", "n"), ("deur", "n"), ("vloer", "n"),
    ("muur", "n"), ("dak", "n"), ("trap", "n"), ("tuin", "n"), ("hek", "n"),
    ("bed", "n"), ("kussing", "n"), ("kombers", "n"), ("mat", "n"), ("kas", "n"),
    ("rak", "n"), ("spieël", "n"), ("lamp", "n"), ("kers", "n"), ("sleutel", "n"),
    ("klok", "n"), ("horlosie", "n"), ("besem", "n"), ("seep", "n"), ("handdoek", "n"),
    ("emmer", "n"), ("mandjie", "n"), ("boks", "n"), ("tou", "n"), ("foto", "n"),

    # --- Ort und Stadt ---
    ("straat", "n"), ("pad", "n"), ("dorp", "n"), ("stad", "n"), ("winkel", "n"),
    ("kerk", "n"), ("hospitaal", "n"), ("biblioteek", "n"), ("park", "n"), ("plaas", "n"),
    ("brug", "n"), ("plek", "n"), ("land", "n"), ("wêreld", "n"), ("mark", "n"),

    # --- Tiere ---
    ("dier", "n"), ("hond", "n"), ("kat", "n"), ("muis", "n"), ("voël", "n"),
    ("vis", "n"), ("koei", "n"), ("perd", "n"), ("skaap", "n"), ("bok", "n"),
    ("vark", "n"), ("hoender", "n"), ("eend", "n"), ("haan", "n"), ("kuiken", "n"),
    ("olifant", "n"), ("leeu", "n"), ("aap", "n"), ("slang", "n"), ("padda", "n"),
    ("by", "n"), ("mier", "n"), ("spinnekop", "n"), ("vlinder", "n"), ("wurm", "n"),
    ("haas", "n"), ("uil", "n"), ("kraai", "n"), ("duif", "n"), ("renoster", "n"),
    ("seekoei", "n"), ("kameelperd", "n"), ("sebra", "n"), ("jakkals", "n"), ("wolf", "n"),
    ("beer", "n"), ("tier", "n"), ("luiperd", "n"), ("dolfyn", "n"), ("haai", "n"),
    ("skilpad", "n"), ("akkedis", "n"), ("krap", "n"), ("nes", "n"), ("veer", "n"),
    ("stert", "n"), ("vlerk", "n"), ("poot", "n"),

    # --- Essen und Trinken ---
    ("kos", "n"), ("brood", "n"), ("melk", "n"), ("water", "n"), ("sap", "n"),
    ("tee", "n"), ("koffie", "n"), ("suiker", "n"), ("sout", "n"), ("peper", "n"),
    ("botter", "n"), ("kaas", "n"), ("eier", "n"), ("vleis", "n"), ("rys", "n"),
    ("pap", "n"), ("sop", "n"), ("slaai", "n"), ("groente", "n"), ("vrugte", "n"),
    ("appel", "n"), ("piesang", "n"), ("druif", "n"), ("lemoen", "n"), ("peer", "n"),
    ("perske", "n"), ("aarbei", "n"), ("tamatie", "n"), ("wortel", "n"), ("aartappel", "n"),
    ("ui", "n"), ("pampoen", "n"), ("ertjie", "n"), ("boontjie", "n"), ("koek", "n"),
    ("koekie", "n"), ("roomys", "n"), ("sjokolade", "n"), ("heuning", "n"), ("ontbyt", "n"),
    ("middagete", "n"), ("aandete", "n"), ("mes", "n"), ("vurk", "n"), ("lepel", "n"),
    ("koppie", "n"), ("glas", "n"), ("pot", "n"), ("pan", "n"), ("ketel", "n"),

    # --- Koerper ---
    ("lyf", "n"), ("kop", "n"), ("gesig", "n"), ("oog", "n"), ("oor", "n"),
    ("neus", "n"), ("mond", "n"), ("tand", "n"), ("tong", "n"), ("lip", "n"),
    ("wang", "n"), ("ken", "n"), ("nek", "n"), ("skouer", "n"), ("arm", "n"),
    ("hand", "n"), ("vinger", "n"), ("duim", "n"), ("maag", "n"), ("rug", "n"),
    ("been", "n"), ("knie", "n"), ("voet", "n"), ("toon", "n"), ("hart", "n"),
    ("vel", "n"), ("bloed", "n"), ("stem", "n"), ("elmboog", "n"),

    # --- Kleidung ---
    ("hemp", "n"), ("broek", "n"), ("rok", "n"), ("romp", "n"), ("jas", "n"),
    ("trui", "n"), ("skoen", "n"), ("sok", "n"), ("hoed", "n"), ("pet", "n"),
    ("das", "n"), ("knoop", "n"), ("sak", "n"), ("handskoen", "n"), ("klere", "n"),

    # --- Natur und Wetter ---
    ("son", "n"), ("maan", "n"), ("ster", "n"), ("lug", "n"), ("wolk", "n"),
    ("reën", "n"), ("sneeu", "n"), ("wind", "n"), ("storm", "n"), ("donder", "n"),
    ("blits", "n"), ("reënboog", "n"), ("boom", "n"), ("blaar", "n"), ("tak", "n"),
    ("blom", "n"), ("gras", "n"), ("bos", "n"), ("veld", "n"), ("berg", "n"),
    ("rivier", "n"), ("see", "n"), ("strand", "n"), ("sand", "n"), ("klip", "n"),
    ("grond", "n"), ("vuur", "n"), ("ys", "n"), ("hout", "n"), ("saad", "n"),
    ("wortels", "n"), ("dou", "n"), ("mis", "n"), ("skaduwee", "n"), ("lig", "n"),

    # --- Spielzeug, Fahrzeuge, Dinge ---
    ("bal", "n"), ("fiets", "n"), ("motor", "n"), ("bus", "n"), ("trein", "n"),
    ("vliegtuig", "n"), ("boot", "n"), ("skip", "n"), ("wa", "n"), ("wiel", "n"),
    ("pop", "n"), ("blok", "n"), ("speelding", "n"), ("kaart", "n"), ("geld", "n"),
    ("sent", "n"), ("rand", "n"), ("brief", "n"), ("koerant", "n"), ("ding", "n"),
    ("spel", "n"), ("liedjie", "n"), ("musiek", "n"), ("fluit", "n"), ("trommel", "n"),
    ("ballon", "n"), ("vlieër", "n"), ("geskenk", "n"), ("kroon", "n"), ("swaard", "n"),

    # --- Zeit ---
    ("tyd", "n"), ("dag", "n"), ("nag", "n"), ("oggend", "n"), ("middag", "n"),
    ("aand", "n"), ("week", "n"), ("maand", "n"), ("jaar", "n"), ("uur", "n"),
    ("minuut", "n"), ("somer", "n"), ("winter", "n"), ("lente", "n"), ("herfs", "n"),
    ("verjaarsdag", "n"), ("vakansie", "n"), ("fees", "n"), ("droom", "n"), ("hulp", "n"),

    # --- Farben ---
    ("rooi", "a"), ("blou", "a"), ("geel", "a"), ("groen", "a"), ("swart", "a"),
    ("wit", "a"), ("bruin", "a"), ("pers", "a"), ("oranje", "a"), ("pienk", "a"),
    ("grys", "a"),

    # --- Adjektive ---
    ("groot", "a"), ("klein", "a"), ("lank", "a"), ("kort", "a"), ("hoog", "a"),
    ("laag", "a"), ("dik", "a"), ("dun", "a"), ("oud", "a"), ("jonk", "a"),
    ("nuut", "a"), ("mooi", "a"), ("lelik", "a"), ("goed", "a"), ("sleg", "a"),
    ("warm", "a"), ("koud", "a"), ("nat", "a"), ("droog", "a"), ("skoon", "a"),
    ("vuil", "a"), ("vol", "a"), ("leeg", "a"), ("swaar", "a"), ("vinnig", "a"),
    ("stadig", "a"), ("sterk", "a"), ("swak", "a"), ("hard", "a"), ("sag", "a"),
    ("soet", "a"), ("suur", "a"), ("bitter", "a"), ("lekker", "a"), ("ryk", "a"),
    ("arm", "a"), ("hartseer", "a"), ("kwaad", "a"), ("bang", "a"), ("moeg", "a"),
    ("honger", "a"), ("dors", "a"), ("siek", "a"), ("gesond", "a"), ("stil", "a"),
    ("maklik", "a"), ("moeilik", "a"), ("reg", "a"), ("verkeerd", "a"), ("vroeg", "a"),
    ("laat", "a"), ("veilig", "a"), ("gelukkig", "a"), ("jammer", "a"), ("slim", "a"),
    ("dom", "a"), ("vriendelik", "a"), ("dapper", "a"), ("stout", "a"), ("ronde", "a"),
    ("wyd", "a"), ("smal", "a"), ("diep", "a"), ("blink", "a"), ("donker", "a"),
    ("helder", "a"), ("sagte", "a"), ("wonderlik", "a"), ("belangrik", "a"), ("ernstig", "a"),
]
