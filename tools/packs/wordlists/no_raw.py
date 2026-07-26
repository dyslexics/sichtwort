# -*- coding: utf-8 -*-
# Grundwortschatz Norwegisch (Bokmål) für Sichtwort — Rohliste (Checkpoint)
# Feld 1: Wort (ungetrennt), Feld 2: n=Nomen v=Verb a=Adjektiv o=Sonstiges
# Homonyme bewusst nur einmal: "tre" = Zahl 3 (o), "kort" = kurz (a).

FUNC = [
    # Pronomen
    "jeg", "du", "han", "hun", "den", "det", "vi", "dere", "de", "meg",
    "deg", "ham", "henne", "oss", "seg", "min", "mitt", "mine", "din", "ditt",
    "dine", "hans", "hennes", "vårt", "våre", "deres", "sin", "sitt", "sine",
    # Artikel & Demonstrativa
    "en", "ei", "et", "denne", "dette", "disse", "som",
    # Konjunktionen
    "og", "eller", "men", "at", "om", "når", "da", "fordi", "hvis", "så",
    "også", "ikke", "ja", "nei", "jo",
    # Frage- & Ortswörter
    "her", "der", "hvor", "hva", "hvem", "hvorfor", "hvordan", "hvilken", "nå",
    # Präpositionen
    "i", "på", "til", "fra", "med", "uten", "av", "for", "mot", "over",
    "under", "ved", "etter", "før", "mellom", "gjennom", "hos",
    # Richtungs- & Zeitadverbien
    "opp", "ned", "ut", "inn", "ute", "inne", "oppe", "nede", "hjem", "hjemme",
    "borte", "fram", "tilbake", "igjen", "alltid", "aldri", "ofte", "snart",
    # Mengenwörter
    "litt", "mye", "mange", "alle", "noen", "ingen", "hver", "begge", "mer",
    "mest", "mindre", "minst", "veldig", "bare", "enda", "kanskje", "gjerne",
    "sammen", "alene", "selv",
    # Zahlen
    "to", "tre", "fire", "fem", "seks", "sju", "åtte", "ni", "ti", "elleve",
    "tolv", "tjue", "hundre", "tusen", "null",
]

VERBS = [
    "være", "ha", "gjøre", "si", "se", "gå", "komme", "få", "ta", "gi",
    "stå", "ligge", "sitte", "løpe", "hoppe", "danse", "synge", "lese",
    "skrive", "tegne", "male", "telle", "regne", "lære", "kunne", "ville",
    "skulle", "måtte", "tenke", "tro", "vite", "forstå", "huske", "glemme",
    "høre", "snakke", "rope", "spørre", "svare", "fortelle", "spise",
    "drikke", "sove", "våkne", "vaske", "bade", "leke", "spille", "vinne",
    "kaste", "fange", "sparke", "klatre", "svømme", "sykle", "kjøre",
    "reise", "bo", "vente", "hjelpe", "dele", "kjøpe", "selge", "åpne",
    "lukke", "finne", "miste", "holde", "bære", "dra", "trekke", "falle",
    "gråte", "le", "smile", "like", "elske", "ønske", "håpe", "trenge",
    "bruke", "lage", "bygge", "bake", "koke", "klippe", "rydde", "hente",
    "sende", "ringe", "møte", "bli", "begynne", "slutte", "prøve", "lukte",
    "smake", "føle", "kjenne", "vise", "gjemme", "vokse", "brenne", "slå",
    "klemme", "vinke", "følge", "legge", "sette", "fylle",
]

ADJ = [
    "stor", "liten", "lang", "kort", "høy", "lav", "tykk", "tynn", "tung",
    "lett", "sterk", "svak", "rask", "sen", "ny", "gammel", "ung", "fin",
    "pen", "stygg", "snill", "slem", "glad", "trist", "lei", "sint", "redd",
    "rolig", "vill", "våt", "tørr", "varm", "kald", "myk", "hard", "ren",
    "full", "tom", "åpen", "rik", "morsom", "kjedelig", "viktig", "farlig",
    "frisk", "syk", "sulten", "tørst", "trøtt", "våken", "søt", "sur",
    "god", "dårlig", "riktig", "klar", "mørk", "lys", "rund", "skarp",
    "dyp", "nær", "stille", "flink", "dum", "tidlig", "hel", "halv",
    "samme", "annen", "første", "siste", "neste", "ferdig",
    # Farben
    "rød", "blå", "gul", "grønn", "hvit", "svart", "brun", "grå", "rosa",
    "lilla", "oransje",
]

NOUNS = [
    # Familie & Menschen
    "mamma", "pappa", "mor", "far", "bror", "søster", "barn", "gutt",
    "jente", "baby", "bestemor", "bestefar", "tante", "onkel", "familie",
    "venn", "mann", "navn",
    # Körper
    "hode", "hår", "øye", "øre", "nese", "munn", "tann", "arm", "hånd",
    "finger", "ben", "fot", "hjerte", "kropp",
    # Schule
    "skole", "klasse", "lærer", "elev", "bok", "ord", "bokstav", "tall",
    "eventyr", "sang", "bilde", "blyant", "papir", "farge", "stol", "bord",
    # Haus
    "hus", "kjøkken", "stue", "bad", "dør", "vindu", "seng", "lampe",
    "klokke", "nøkkel", "hage",
    # Essen
    "mat", "brød", "ost", "melk", "vann", "kake", "is", "sjokolade", "egg",
    "fisk", "kjøtt", "potet", "eple", "banan", "pizza", "frokost",
    "middag", "glass",
    # Tiere
    "dyr", "hund", "katt", "hest", "ku", "gris", "sau", "geit", "fugl",
    "hval", "frosk", "slange", "sommerfugl", "mus", "rev", "ulv", "bjørn",
    "elefant", "løve", "tiger", "ape", "kanin", "kylling",
    # Natur
    "sol", "måne", "stjerne", "himmel", "sky", "regn", "snø", "vind",
    "vær", "jord", "sand", "stein", "fjell", "skog", "blomst", "sjø",
    "hav", "strand", "vei", "by", "land", "verden", "gård",
    # Zeit
    "dag", "natt", "morgen", "kveld", "uke", "år", "mandag", "tirsdag",
    "onsdag", "torsdag", "fredag", "lørdag", "søndag", "vinter", "vår",
    "sommer", "høst", "jul", "bursdag",
    # Spielzeug & Sachen
    "ball", "dukke", "bil", "buss", "tog", "båt", "fly", "sykkel", "ski",
    "spill", "ballong", "gave", "penger", "butikk", "telefon", "musikk",
    "film",
    # Kleidung
    "klær", "bukse", "genser", "kjole", "sokk", "sko", "jakke", "lue",
    "hatt",
    # Berufe & Figuren
    "lege", "politi", "konge", "dronning", "prinsesse", "troll", "ting",
]

WORDS = (
    [(w, "o") for w in FUNC]
    + [(w, "v") for w in VERBS]
    + [(w, "a") for w in ADJ]
    + [(w, "n") for w in NOUNS]
)

if __name__ == "__main__":
    from collections import Counter
    print("total", len(WORDS))
    print("dups", [w for w, c in Counter(w for w, _ in WORDS).items() if c > 1])
    print("o", len(FUNC), "v", len(VERBS), "a", len(ADJ), "n", len(NOUNS))
