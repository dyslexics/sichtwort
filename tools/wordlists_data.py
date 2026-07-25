# -*- coding: utf-8 -*-
"""Kuratierte Wortdaten für die Sichtwort-Wortlisten.

Jeder Eintrag ist ein Tupel (wort, typ) mit typ aus {n, v, a, o}:
  n = Nomen, v = Verb, a = Adjektiv, o = sonstiges (Artikel, Pronomen,
  Präpositionen, Konjunktionen, Adverbien, Zahlwörter, Partikeln).
Die Silbentrennung wird in gen_wordlists.py automatisch erzeugt.

DE500 orientiert sich am Grundwortschatz der Grundschule (Häufigkeitslisten
Deutsch, z.B. Bayerischer Grundwortschatz). DE1000 = DE500 + DE1000_EXTRA.
"""

# ---------------------------------------------------------------------------
# DE 500 — Grundwortschatz Grundschule (häufigste Wörter)
# ---------------------------------------------------------------------------

DE500 = [
    # --- Artikel & Pronomen (52) ---
    ("der", "o"), ("die", "o"), ("das", "o"), ("den", "o"), ("dem", "o"), ("des", "o"),
    ("ein", "o"), ("eine", "o"), ("einen", "o"), ("einem", "o"), ("einer", "o"), ("eines", "o"),
    ("ich", "o"), ("du", "o"), ("er", "o"), ("sie", "o"), ("es", "o"), ("wir", "o"),
    ("ihr", "o"), ("man", "o"),
    ("mich", "o"), ("dich", "o"), ("sich", "o"), ("uns", "o"), ("euch", "o"), ("mir", "o"),
    ("dir", "o"), ("ihm", "o"), ("ihn", "o"), ("ihnen", "o"),
    ("mein", "o"), ("meine", "o"), ("dein", "o"), ("deine", "o"), ("seine", "o"), ("ihre", "o"),
    ("unser", "o"), ("euer", "o"),
    ("wer", "o"), ("wen", "o"), ("was", "o"), ("wie", "o"), ("wo", "o"), ("wann", "o"),
    ("warum", "o"),
    ("dieser", "o"), ("diese", "o"), ("dieses", "o"), ("jeder", "o"), ("jede", "o"),
    ("jedes", "o"), ("welche", "o"),
    # --- Verneinung & Menge (10) ---
    ("nicht", "o"), ("kein", "o"), ("keine", "o"), ("nichts", "o"), ("alle", "o"),
    ("alles", "o"), ("etwas", "o"), ("viel", "o"), ("viele", "o"), ("mehr", "o"),
    # --- Konjunktionen & Partikeln (21) ---
    ("und", "o"), ("oder", "o"), ("aber", "o"), ("denn", "o"), ("doch", "o"), ("auch", "o"),
    ("nur", "o"), ("noch", "o"), ("schon", "o"), ("als", "o"), ("wenn", "o"), ("weil", "o"),
    ("dass", "o"), ("damit", "o"), ("ob", "o"), ("also", "o"),
    ("ja", "o"), ("nein", "o"), ("bitte", "o"), ("danke", "o"), ("hallo", "o"),
    # --- Präpositionen (29) ---
    ("in", "o"), ("im", "o"), ("an", "o"), ("am", "o"), ("auf", "o"), ("aus", "o"),
    ("bei", "o"), ("beim", "o"), ("mit", "o"), ("nach", "o"), ("von", "o"), ("vom", "o"),
    ("zu", "o"), ("zum", "o"), ("zur", "o"), ("für", "o"), ("über", "o"), ("unter", "o"),
    ("vor", "o"), ("hinter", "o"), ("neben", "o"), ("zwischen", "o"), ("durch", "o"),
    ("gegen", "o"), ("ohne", "o"), ("um", "o"), ("seit", "o"), ("bis", "o"), ("ab", "o"),
    # --- Adverbien (42) ---
    ("so", "o"), ("dann", "o"), ("da", "o"), ("hier", "o"), ("dort", "o"), ("jetzt", "o"),
    ("heute", "o"), ("morgen", "o"), ("gestern", "o"), ("immer", "o"), ("nie", "o"),
    ("oft", "o"), ("manchmal", "o"), ("wieder", "o"), ("sehr", "o"), ("ganz", "o"),
    ("zusammen", "o"), ("allein", "o"), ("vielleicht", "o"), ("natürlich", "o"),
    ("endlich", "o"), ("plötzlich", "o"), ("gern", "o"), ("oben", "o"), ("unten", "o"),
    ("vorne", "o"), ("hinten", "o"), ("links", "o"), ("rechts", "o"), ("draußen", "o"),
    ("drinnen", "o"), ("weg", "o"), ("hin", "o"), ("her", "o"), ("zurück", "o"),
    ("vorbei", "o"), ("nun", "o"), ("eben", "o"), ("fast", "o"), ("gleich", "o"),
    ("bald", "o"), ("genug", "o"),
    # --- Zahlwörter (15) ---
    ("null", "o"), ("eins", "o"), ("zwei", "o"), ("drei", "o"), ("vier", "o"), ("fünf", "o"),
    ("sechs", "o"), ("sieben", "o"), ("acht", "o"), ("neun", "o"), ("zehn", "o"), ("elf", "o"),
    ("zwölf", "o"), ("hundert", "o"), ("tausend", "o"),

    # --- Hilfs- und Modalverben (27) ---
    ("sein", "v"), ("ist", "v"), ("sind", "v"), ("bin", "v"), ("bist", "v"), ("war", "v"),
    ("waren", "v"),
    ("haben", "v"), ("habe", "v"), ("hat", "v"), ("hatte", "v"), ("hatten", "v"),
    ("werden", "v"), ("wird", "v"), ("wurde", "v"),
    ("können", "v"), ("kann", "v"), ("müssen", "v"), ("muss", "v"), ("wollen", "v"),
    ("will", "v"), ("sollen", "v"), ("soll", "v"), ("dürfen", "v"), ("darf", "v"),
    ("mögen", "v"), ("mag", "v"),
    # --- Vollverben (81) ---
    ("gehen", "v"), ("geht", "v"), ("kommen", "v"), ("kommt", "v"), ("machen", "v"),
    ("macht", "v"), ("sagen", "v"), ("sagt", "v"), ("sehen", "v"), ("sieht", "v"),
    ("geben", "v"), ("gibt", "v"), ("nehmen", "v"), ("nimmt", "v"), ("finden", "v"),
    ("fahren", "v"), ("laufen", "v"), ("stehen", "v"), ("liegen", "v"), ("sitzen", "v"),
    ("bleiben", "v"), ("bringen", "v"), ("denken", "v"), ("glauben", "v"), ("wissen", "v"),
    ("kennen", "v"), ("heißen", "v"), ("heißt", "v"), ("spielen", "v"), ("lernen", "v"),
    ("lesen", "v"), ("schreiben", "v"), ("malen", "v"), ("singen", "v"), ("springen", "v"),
    ("essen", "v"), ("trinken", "v"), ("schlafen", "v"), ("hören", "v"), ("sprechen", "v"),
    ("fragen", "v"), ("antworten", "v"), ("rufen", "v"), ("holen", "v"), ("legen", "v"),
    ("setzen", "v"), ("stellen", "v"), ("halten", "v"), ("helfen", "v"), ("arbeiten", "v"),
    ("wohnen", "v"), ("warten", "v"), ("suchen", "v"), ("zeigen", "v"), ("öffnen", "v"),
    ("tragen", "v"), ("ziehen", "v"), ("werfen", "v"), ("fangen", "v"), ("fallen", "v"),
    ("fliegen", "v"), ("schwimmen", "v"), ("tanzen", "v"), ("lachen", "v"), ("weinen", "v"),
    ("lieben", "v"), ("kaufen", "v"), ("kochen", "v"), ("backen", "v"), ("waschen", "v"),
    ("putzen", "v"), ("bauen", "v"), ("brauchen", "v"), ("gehören", "v"), ("versuchen", "v"),
    ("verstehen", "v"), ("vergessen", "v"), ("erzählen", "v"), ("beginnen", "v"),
    ("aufstehen", "v"), ("bekommen", "v"),

    # --- Nomen: Familie & Menschen (22) ---
    ("Kind", "n"), ("Kinder", "n"), ("Mutter", "n"), ("Mama", "n"), ("Vater", "n"),
    ("Papa", "n"), ("Eltern", "n"), ("Bruder", "n"), ("Schwester", "n"), ("Oma", "n"),
    ("Opa", "n"), ("Familie", "n"), ("Freund", "n"), ("Freundin", "n"), ("Mann", "n"),
    ("Frau", "n"), ("Junge", "n"), ("Mädchen", "n"), ("Baby", "n"), ("Mensch", "n"),
    ("Leute", "n"), ("Name", "n"),
    # --- Nomen: Zeit (11) ---
    ("Tag", "n"), ("Nacht", "n"), ("Abend", "n"), ("Mittag", "n"), ("Woche", "n"),
    ("Monat", "n"), ("Jahr", "n"), ("Zeit", "n"), ("Stunde", "n"), ("Minute", "n"),
    ("Uhr", "n"),
    # --- Nomen: Natur & Wetter (22) ---
    ("Sonne", "n"), ("Mond", "n"), ("Stern", "n"), ("Himmel", "n"), ("Wolke", "n"),
    ("Regen", "n"), ("Schnee", "n"), ("Wind", "n"), ("Wetter", "n"), ("Wasser", "n"),
    ("Feuer", "n"), ("Luft", "n"), ("Erde", "n"), ("Baum", "n"), ("Blume", "n"),
    ("Wald", "n"), ("Wiese", "n"), ("Berg", "n"), ("See", "n"), ("Meer", "n"),
    ("Fluss", "n"), ("Garten", "n"),
    # --- Nomen: Wohnen & Ort (16) ---
    ("Haus", "n"), ("Straße", "n"), ("Weg", "n"), ("Stadt", "n"), ("Land", "n"),
    ("Zimmer", "n"), ("Tür", "n"), ("Fenster", "n"), ("Tisch", "n"), ("Stuhl", "n"),
    ("Bett", "n"), ("Schrank", "n"), ("Lampe", "n"), ("Küche", "n"), ("Bad", "n"),
    ("Hof", "n"),
    # --- Nomen: Schule (21) ---
    ("Schule", "n"), ("Lehrer", "n"), ("Lehrerin", "n"), ("Schüler", "n"), ("Klasse", "n"),
    ("Pause", "n"), ("Ferien", "n"), ("Buch", "n"), ("Heft", "n"), ("Stift", "n"),
    ("Tafel", "n"), ("Tasche", "n"), ("Farbe", "n"), ("Bild", "n"), ("Brief", "n"),
    ("Wort", "n"), ("Satz", "n"), ("Zahl", "n"), ("Frage", "n"), ("Antwort", "n"),
    ("Aufgabe", "n"),
    # --- Nomen: Freizeit (10) ---
    ("Auto", "n"), ("Bus", "n"), ("Zug", "n"), ("Fahrrad", "n"), ("Ball", "n"),
    ("Spiel", "n"), ("Geburtstag", "n"), ("Geschenk", "n"), ("Musik", "n"), ("Lied", "n"),
    # --- Nomen: Tiere (10) ---
    ("Tier", "n"), ("Hund", "n"), ("Katze", "n"), ("Maus", "n"), ("Vogel", "n"),
    ("Pferd", "n"), ("Kuh", "n"), ("Schwein", "n"), ("Fisch", "n"), ("Löwe", "n"),
    # --- Nomen: Essen (10) ---
    ("Essen", "n"), ("Brot", "n"), ("Milch", "n"), ("Ei", "n"), ("Apfel", "n"),
    ("Obst", "n"), ("Gemüse", "n"), ("Kuchen", "n"), ("Eis", "n"), ("Salz", "n"),
    # --- Nomen: Körper (13) ---
    ("Hand", "n"), ("Fuß", "n"), ("Kopf", "n"), ("Auge", "n"), ("Ohr", "n"), ("Nase", "n"),
    ("Mund", "n"), ("Zahn", "n"), ("Haar", "n"), ("Arm", "n"), ("Bein", "n"), ("Herz", "n"),
    ("Finger", "n"),
    # --- Nomen: Sonstiges (15) ---
    ("Kleid", "n"), ("Hose", "n"), ("Schuh", "n"), ("Geld", "n"), ("Arbeit", "n"),
    ("Arzt", "n"), ("Glück", "n"), ("Idee", "n"), ("Sache", "n"), ("Ding", "n"),
    ("Stück", "n"), ("Teil", "n"), ("Seite", "n"), ("Anfang", "n"), ("Ende", "n"),

    # --- Adjektive (73) ---
    ("gut", "a"), ("besser", "a"), ("schlecht", "a"), ("groß", "a"), ("klein", "a"),
    ("lang", "a"), ("kurz", "a"), ("hoch", "a"), ("tief", "a"), ("dick", "a"), ("dünn", "a"),
    ("schnell", "a"), ("langsam", "a"), ("alt", "a"), ("jung", "a"), ("neu", "a"),
    ("weit", "a"), ("nah", "a"), ("warm", "a"), ("kalt", "a"), ("heiß", "a"), ("nass", "a"),
    ("trocken", "a"), ("hell", "a"), ("dunkel", "a"), ("laut", "a"), ("leise", "a"),
    ("schön", "a"), ("lieb", "a"), ("nett", "a"), ("böse", "a"), ("froh", "a"),
    ("traurig", "a"), ("lustig", "a"), ("müde", "a"), ("krank", "a"), ("gesund", "a"),
    ("stark", "a"), ("schwach", "a"), ("hart", "a"), ("weich", "a"), ("sauber", "a"),
    ("schmutzig", "a"), ("voll", "a"), ("leer", "a"), ("richtig", "a"), ("falsch", "a"),
    ("leicht", "a"), ("schwer", "a"), ("einfach", "a"), ("wichtig", "a"), ("rot", "a"),
    ("blau", "a"), ("gelb", "a"), ("grün", "a"), ("schwarz", "a"), ("weiß", "a"),
    ("braun", "a"), ("grau", "a"), ("bunt", "a"), ("süß", "a"), ("sauer", "a"),
    ("satt", "a"), ("hungrig", "a"), ("durstig", "a"), ("fertig", "a"), ("offen", "a"),
    ("frei", "a"), ("erste", "a"), ("zweite", "a"), ("dritte", "a"), ("letzte", "a"),
    ("nächste", "a"),
]

# ---------------------------------------------------------------------------
# DE 1000 = DE500 + diese 500 weiteren Wörter
# ---------------------------------------------------------------------------

DE1000_EXTRA = [
    # --- Wochentage, Monate, Jahreszeiten (25) ---
    ("Montag", "n"), ("Dienstag", "n"), ("Mittwoch", "n"), ("Donnerstag", "n"),
    ("Freitag", "n"), ("Samstag", "n"), ("Sonntag", "n"), ("Wochenende", "n"),
    ("Januar", "n"), ("Februar", "n"), ("März", "n"), ("April", "n"), ("Mai", "n"),
    ("Juni", "n"), ("Juli", "n"), ("August", "n"), ("September", "n"), ("Oktober", "n"),
    ("November", "n"), ("Dezember", "n"),
    ("Frühling", "n"), ("Sommer", "n"), ("Herbst", "n"), ("Winter", "n"), ("Weihnachten", "n"),
    # --- Zahlwörter (16) ---
    ("dreizehn", "o"), ("vierzehn", "o"), ("fünfzehn", "o"), ("sechzehn", "o"),
    ("siebzehn", "o"), ("achtzehn", "o"), ("neunzehn", "o"), ("zwanzig", "o"),
    ("dreißig", "o"), ("vierzig", "o"), ("fünfzig", "o"), ("sechzig", "o"), ("siebzig", "o"),
    ("achtzig", "o"), ("neunzig", "o"), ("Million", "n"),
    # --- Funktionswörter & Adverbien (55) ---
    ("wem", "o"), ("wieso", "o"), ("woher", "o"), ("wohin", "o"),
    ("sondern", "o"), ("obwohl", "o"), ("während", "o"), ("bevor", "o"), ("nachdem", "o"),
    ("falls", "o"), ("wegen", "o"), ("trotz", "o"), ("außer", "o"), ("statt", "o"),
    ("manche", "o"), ("wenig", "o"), ("jemand", "o"), ("niemand", "o"), ("selbst", "o"),
    ("beide", "o"), ("andere", "o"), ("anderen", "o"), ("einige", "o"), ("mehrere", "o"),
    ("solche", "o"),
    ("kaum", "o"), ("sogar", "o"), ("wohl", "o"), ("mal", "o"), ("überall", "o"),
    ("eigentlich", "o"), ("besonders", "o"), ("dabei", "o"), ("zuerst", "o"),
    ("trotzdem", "o"), ("deshalb", "o"), ("darum", "o"), ("daher", "o"), ("außerdem", "o"),
    ("sofort", "o"), ("gerade", "o"), ("später", "o"), ("früher", "o"), ("vorher", "o"),
    ("danach", "o"), ("dazu", "o"), ("davon", "o"), ("dafür", "o"), ("darauf", "o"),
    ("meistens", "o"), ("selten", "o"), ("täglich", "o"), ("ziemlich", "o"),
    ("gemeinsam", "o"), ("innen", "o"),
    # --- Verben (110) ---
    ("ging", "v"), ("kam", "v"), ("sah", "v"), ("konnte", "v"),
    ("wollte", "v"), ("möchte", "v"), ("rechnen", "v"), ("basteln", "v"), ("turnen", "v"),
    ("klettern", "v"), ("reiten", "v"), ("wandern", "v"), ("sammeln", "v"), ("passen", "v"),
    ("wachsen", "v"), ("schenken", "v"), ("üben", "v"), ("schauen", "v"),
    ("besuchen", "v"), ("bezahlen", "v"), ("verkaufen", "v"), ("schicken", "v"),
    ("verlieren", "v"), ("gewinnen", "v"), ("verlassen", "v"), ("verstecken", "v"),
    ("erklären", "v"), ("erlauben", "v"), ("entdecken", "v"), ("erkennen", "v"),
    ("erinnern", "v"), ("überlegen", "v"), ("beobachten", "v"), ("aufpassen", "v"),
    ("zuhören", "v"), ("anfangen", "v"), ("aufhören", "v"), ("einkaufen", "v"),
    ("einschlafen", "v"), ("aufwachen", "v"), ("anziehen", "v"), ("ausziehen", "v"),
    ("aufräumen", "v"), ("abholen", "v"), ("mitnehmen", "v"), ("zeichnen", "v"),
    ("kleben", "v"), ("schneiden", "v"), ("gießen", "v"), ("pflanzen", "v"),
    ("füttern", "v"), ("hüpfen", "v"), ("rennen", "v"), ("rutschen", "v"),
    ("schaukeln", "v"), ("stolpern", "v"), ("klopfen", "v"), ("winken", "v"),
    ("atmen", "v"), ("riechen", "v"), ("schmecken", "v"), ("fühlen", "v"), ("frieren", "v"),
    ("baden", "v"), ("duschen", "v"), ("nähen", "v"), ("mischen", "v"), ("decken", "v"),
    ("wischen", "v"), ("sortieren", "v"), ("zählen", "v"), ("messen", "v"), ("teilen", "v"),
    ("tauschen", "v"), ("sparen", "v"), ("wünschen", "v"), ("hoffen", "v"), ("träumen", "v"),
    ("staunen", "v"), ("erschrecken", "v"), ("ärgern", "v"), ("streiten", "v"),
    ("trösten", "v"), ("umarmen", "v"), ("grüßen", "v"), ("einladen", "v"), ("feiern", "v"),
    ("telefonieren", "v"), ("klingeln", "v"), ("flüstern", "v"), ("schreien", "v"),
    ("pfeifen", "v"), ("leuchten", "v"), ("brennen", "v"), ("retten", "v"), ("heilen", "v"),
    ("reparieren", "v"), ("starten", "v"), ("landen", "v"), ("reisen", "v"), ("drehen", "v"),
    ("drücken", "v"), ("schieben", "v"), ("heben", "v"), ("entscheiden", "v"),
    ("planen", "v"), ("überraschen", "v"), ("verschwinden", "v"), ("nennen", "v"),
    ("treffen", "v"),
    # --- Nomen: Schule & Lernen (23) ---
    ("Unterricht", "n"), ("Hausaufgabe", "n"), ("Zeugnis", "n"), ("Note", "n"),
    ("Diktat", "n"), ("Text", "n"), ("Geschichte", "n"), ("Märchen", "n"), ("Gedicht", "n"),
    ("Silbe", "n"), ("Punkt", "n"), ("Linie", "n"), ("Kreis", "n"), ("Lineal", "n"),
    ("Federmappe", "n"), ("Schulhof", "n"), ("Turnhalle", "n"), ("Kindergarten", "n"),
    ("Bleistift", "n"), ("Papier", "n"), ("Schere", "n"), ("Buchstabe", "n"), ("Blatt", "n"),
    # --- Nomen: Natur & Tiere (49) ---
    ("Wurzel", "n"), ("Ast", "n"), ("Gras", "n"), ("Feld", "n"), ("Bauernhof", "n"),
    ("Stall", "n"), ("Traktor", "n"), ("Höhle", "n"), ("Insel", "n"), ("Strand", "n"),
    ("Welle", "n"), ("Bach", "n"), ("Brücke", "n"), ("Nest", "n"), ("Feder", "n"),
    ("Flügel", "n"), ("Schwanz", "n"), ("Fell", "n"), ("Igel", "n"), ("Fuchs", "n"),
    ("Wolf", "n"), ("Reh", "n"), ("Eichhörnchen", "n"), ("Schaf", "n"), ("Ziege", "n"),
    ("Huhn", "n"), ("Hahn", "n"), ("Gans", "n"), ("Esel", "n"), ("Elefant", "n"),
    ("Giraffe", "n"), ("Kamel", "n"), ("Pinguin", "n"), ("Delfin", "n"), ("Schnecke", "n"),
    ("Wurm", "n"), ("Ameise", "n"), ("Spinne", "n"), ("Fliege", "n"), ("Schmetterling", "n"),
    ("Frosch", "n"), ("Schlange", "n"), ("Eule", "n"), ("Papagei", "n"), ("Ente", "n"),
    ("Hase", "n"), ("Bär", "n"), ("Affe", "n"), ("Biene", "n"),
    # --- Nomen: Haus & Alltag (30) ---
    ("Wohnung", "n"), ("Keller", "n"), ("Dach", "n"), ("Treppe", "n"), ("Balkon", "n"),
    ("Zaun", "n"), ("Schlüssel", "n"), ("Sofa", "n"), ("Teppich", "n"), ("Kissen", "n"),
    ("Decke", "n"), ("Spiegel", "n"), ("Handtuch", "n"), ("Seife", "n"), ("Löffel", "n"),
    ("Gabel", "n"), ("Messer", "n"), ("Teller", "n"), ("Tasse", "n"), ("Glas", "n"),
    ("Flasche", "n"), ("Topf", "n"), ("Ofen", "n"), ("Kühlschrank", "n"), ("Eimer", "n"),
    ("Kerze", "n"), ("Zeitung", "n"), ("Kalender", "n"), ("Boden", "n"), ("Wand", "n"),
    # --- Nomen: Essen & Trinken (28) ---
    ("Frühstück", "n"), ("Hunger", "n"), ("Durst", "n"), ("Nudel", "n"), ("Reis", "n"),
    ("Kartoffel", "n"), ("Salat", "n"), ("Tomate", "n"), ("Gurke", "n"), ("Karotte", "n"),
    ("Banane", "n"), ("Erdbeere", "n"), ("Zitrone", "n"), ("Orange", "n"), ("Nuss", "n"),
    ("Marmelade", "n"), ("Schokolade", "n"), ("Keks", "n"), ("Brötchen", "n"),
    ("Fleisch", "n"), ("Tee", "n"), ("Kaffee", "n"), ("Butter", "n"), ("Käse", "n"),
    ("Wurst", "n"), ("Suppe", "n"), ("Zucker", "n"), ("Saft", "n"),
    # --- Nomen: Kleidung & Körper (22) ---
    ("Kleidung", "n"), ("Hemd", "n"), ("Pullover", "n"), ("Mantel", "n"), ("Mütze", "n"),
    ("Hut", "n"), ("Schal", "n"), ("Handschuh", "n"), ("Socke", "n"), ("Stiefel", "n"),
    ("Knopf", "n"), ("Rock", "n"), ("Brille", "n"), ("Schulter", "n"), ("Knie", "n"),
    ("Rücken", "n"), ("Hals", "n"), ("Daumen", "n"), ("Haut", "n"), ("Blut", "n"),
    ("Bauch", "n"), ("Jacke", "n"),
    # --- Nomen: Stadt, Verkehr, Beruf (32) ---
    ("Bahnhof", "n"), ("Schiff", "n"), ("Boot", "n"), ("Flugzeug", "n"), ("Rakete", "n"),
    ("Motorrad", "n"), ("Ampel", "n"), ("Platz", "n"), ("Markt", "n"), ("Laden", "n"),
    ("Bäcker", "n"), ("Post", "n"), ("Bank", "n"), ("Kirche", "n"), ("Museum", "n"),
    ("Kino", "n"), ("Theater", "n"), ("Zoo", "n"), ("Spielplatz", "n"), ("Schwimmbad", "n"),
    ("Krankenhaus", "n"), ("Apotheke", "n"), ("Feuerwehr", "n"), ("Polizei", "n"),
    ("Polizist", "n"), ("Koch", "n"), ("Bauer", "n"), ("Pilot", "n"), ("Beruf", "n"),
    ("Nachbar", "n"), ("Rad", "n"), ("Dorf", "n"),
    # --- Nomen: Spiel, Sport, Musik (22) ---
    ("Sport", "n"), ("Fußball", "n"), ("Tor", "n"), ("Mannschaft", "n"), ("Spieler", "n"),
    ("Puppe", "n"), ("Teddy", "n"), ("Puzzle", "n"), ("Würfel", "n"), ("Karte", "n"),
    ("Schaukel", "n"), ("Rutsche", "n"), ("Luftballon", "n"), ("Trommel", "n"),
    ("Flöte", "n"), ("Gitarre", "n"), ("Klavier", "n"), ("Urlaub", "n"), ("Reise", "n"),
    ("Koffer", "n"), ("Fest", "n"), ("Film", "n"),
    # --- Nomen: Abstrakt & Körperinneres (22) ---
    ("Freude", "n"), ("Traum", "n"), ("Mut", "n"), ("Kraft", "n"), ("Hilfe", "n"),
    ("Ruhe", "n"), ("Ordnung", "n"), ("Regel", "n"), ("Fehler", "n"), ("Grund", "n"),
    ("Beispiel", "n"), ("Wunsch", "n"), ("Gefühl", "n"), ("Liebe", "n"), ("Leben", "n"),
    ("Welt", "n"), ("Angst", "n"), ("Euro", "n"), ("Knochen", "n"), ("Nagel", "n"),
    ("Muskel", "n"), ("Lärm", "n"),
    # --- Adjektive (66) ---
    ("fröhlich", "a"), ("glücklich", "a"), ("mutig", "a"), ("stolz", "a"),
    ("neugierig", "a"), ("freundlich", "a"), ("höflich", "a"), ("frech", "a"),
    ("faul", "a"), ("fleißig", "a"), ("ruhig", "a"), ("wild", "a"), ("wach", "a"),
    ("aufmerksam", "a"), ("geduldig", "a"), ("ehrlich", "a"), ("klug", "a"), ("dumm", "a"),
    ("witzig", "a"), ("langweilig", "a"), ("spannend", "a"), ("gefährlich", "a"),
    ("sicher", "a"), ("möglich", "a"), ("fremd", "a"), ("bekannt", "a"), ("berühmt", "a"),
    ("teuer", "a"), ("billig", "a"), ("reich", "a"), ("arm", "a"), ("breit", "a"),
    ("eng", "a"), ("rund", "a"), ("spitz", "a"), ("flach", "a"), ("steil", "a"),
    ("glatt", "a"), ("scharf", "a"), ("fest", "a"), ("schwierig", "a"), ("deutlich", "a"),
    ("frisch", "a"), ("lecker", "a"), ("salzig", "a"), ("bitter", "a"), ("fein", "a"),
    ("grob", "a"), ("krumm", "a"), ("schief", "a"), ("gemein", "a"), ("streng", "a"),
    ("zufrieden", "a"), ("verrückt", "a"), ("hübsch", "a"), ("hässlich", "a"),
    ("golden", "a"), ("rosa", "a"), ("orange", "a"), ("lila", "a"), ("schmal", "a"),
    ("dringend", "a"), ("nützlich", "a"), ("hellblau", "a"), ("dunkelgrün", "a"),
    ("silbern", "a"),
]

# ---------------------------------------------------------------------------
# Englisch: Dolch Sight Words (220 service words + 95 nouns) — gemeinfrei
# ---------------------------------------------------------------------------

DOLCH_SERVICE = [
    # Pre-Primer (40)
    ("a", "o"), ("and", "o"), ("away", "o"), ("big", "a"), ("blue", "a"), ("can", "o"),
    ("come", "v"), ("down", "o"), ("find", "v"), ("for", "o"), ("funny", "a"), ("go", "v"),
    ("help", "v"), ("here", "o"), ("I", "o"), ("in", "o"), ("is", "v"), ("it", "o"),
    ("jump", "v"), ("little", "a"), ("look", "v"), ("make", "v"), ("me", "o"), ("my", "o"),
    ("not", "o"), ("one", "o"), ("play", "v"), ("red", "a"), ("run", "v"), ("said", "v"),
    ("see", "v"), ("the", "o"), ("three", "o"), ("to", "o"), ("two", "o"), ("up", "o"),
    ("we", "o"), ("where", "o"), ("yellow", "a"), ("you", "o"),
    # Primer (52)
    ("all", "o"), ("am", "v"), ("are", "v"), ("at", "o"), ("ate", "v"), ("be", "v"),
    ("black", "a"), ("brown", "a"), ("but", "o"), ("came", "v"), ("did", "v"), ("do", "v"),
    ("eat", "v"), ("four", "o"), ("get", "v"), ("good", "a"), ("have", "v"), ("he", "o"),
    ("into", "o"), ("like", "v"), ("must", "o"), ("new", "a"), ("no", "o"), ("now", "o"),
    ("on", "o"), ("our", "o"), ("out", "o"), ("please", "o"), ("pretty", "a"), ("ran", "v"),
    ("ride", "v"), ("saw", "v"), ("say", "v"), ("she", "o"), ("so", "o"), ("soon", "o"),
    ("that", "o"), ("there", "o"), ("they", "o"), ("this", "o"), ("too", "o"), ("under", "o"),
    ("want", "v"), ("was", "v"), ("well", "o"), ("went", "v"), ("what", "o"), ("white", "a"),
    ("who", "o"), ("will", "o"), ("with", "o"), ("yes", "o"),
    # First Grade (41)
    ("after", "o"), ("again", "o"), ("an", "o"), ("any", "o"), ("as", "o"), ("ask", "v"),
    ("by", "o"), ("could", "o"), ("every", "o"), ("fly", "v"), ("from", "o"), ("give", "v"),
    ("going", "v"), ("had", "v"), ("has", "v"), ("her", "o"), ("him", "o"), ("his", "o"),
    ("how", "o"), ("just", "o"), ("know", "v"), ("let", "v"), ("live", "v"), ("may", "o"),
    ("of", "o"), ("old", "a"), ("once", "o"), ("open", "v"), ("over", "o"), ("put", "v"),
    ("round", "a"), ("some", "o"), ("stop", "v"), ("take", "v"), ("thank", "v"), ("them", "o"),
    ("then", "o"), ("think", "v"), ("walk", "v"), ("were", "v"), ("when", "o"),
    # Second Grade (46)
    ("always", "o"), ("around", "o"), ("because", "o"), ("been", "v"), ("before", "o"),
    ("best", "a"), ("both", "o"), ("buy", "v"), ("call", "v"), ("cold", "a"), ("does", "v"),
    ("don't", "v"), ("fast", "a"), ("first", "a"), ("five", "o"), ("found", "v"), ("gave", "v"),
    ("goes", "v"), ("green", "a"), ("its", "o"), ("made", "v"), ("many", "o"), ("off", "o"),
    ("or", "o"), ("pull", "v"), ("read", "v"), ("right", "a"), ("sing", "v"), ("sit", "v"),
    ("sleep", "v"), ("tell", "v"), ("their", "o"), ("these", "o"), ("those", "o"), ("upon", "o"),
    ("us", "o"), ("use", "v"), ("very", "o"), ("wash", "v"), ("which", "o"), ("why", "o"),
    ("wish", "v"), ("work", "v"), ("would", "o"), ("write", "v"), ("your", "o"),
    # Third Grade (41)
    ("about", "o"), ("better", "a"), ("bring", "v"), ("carry", "v"), ("clean", "a"), ("cut", "v"),
    ("done", "v"), ("draw", "v"), ("drink", "v"), ("eight", "o"), ("fall", "v"), ("far", "o"),
    ("full", "a"), ("got", "v"), ("grow", "v"), ("hold", "v"), ("hot", "a"), ("hurt", "v"),
    ("if", "o"), ("keep", "v"), ("kind", "a"), ("laugh", "v"), ("light", "a"), ("long", "a"),
    ("much", "o"), ("myself", "o"), ("never", "o"), ("only", "o"), ("own", "a"), ("pick", "v"),
    ("seven", "o"), ("shall", "o"), ("show", "v"), ("six", "o"), ("small", "a"), ("start", "v"),
    ("ten", "o"), ("today", "o"), ("together", "o"), ("try", "v"), ("warm", "a"),
]

# 95 Dolch nouns. "good-bye" wird als "goodbye" geführt, weil der Bindestrich
# im Datenformat die Silbengrenze markiert (Silbenform bleibt "good-bye").
DOLCH_NOUNS = [
    "apple", "baby", "back", "ball", "bear", "bed", "bell", "bird", "birthday", "boat",
    "box", "boy", "bread", "brother", "cake", "car", "cat", "chair", "chicken", "children",
    "Christmas", "coat", "corn", "cow", "day", "dog", "doll", "door", "duck", "egg",
    "eye", "farm", "farmer", "father", "feet", "fire", "fish", "floor", "flower", "game",
    "garden", "girl", "goodbye", "grass", "ground", "hand", "head", "hill", "home", "horse",
    "house", "kitty", "leg", "letter", "man", "men", "milk", "money", "morning", "mother",
    "name", "nest", "night", "paper", "party", "picture", "pig", "rabbit", "rain", "ring",
    "robin", "Santa Claus", "school", "seed", "sheep", "shoe", "sister", "snow", "song",
    "squirrel", "stick", "street", "sun", "table", "thing", "time", "top", "toy", "tree",
    "watch", "water", "way", "wind", "window", "wood",
]

# ---------------------------------------------------------------------------
# Englisch: Fry Sight Words 1–300 — gemeinfrei
# ---------------------------------------------------------------------------

FRY300 = [
    # 1–100
    ("the", "o"), ("of", "o"), ("and", "o"), ("a", "o"), ("to", "o"), ("in", "o"), ("is", "v"),
    ("you", "o"), ("that", "o"), ("it", "o"), ("he", "o"), ("was", "v"), ("for", "o"),
    ("on", "o"), ("are", "v"), ("as", "o"), ("with", "o"), ("his", "o"), ("they", "o"),
    ("I", "o"), ("at", "o"), ("be", "v"), ("this", "o"), ("have", "v"), ("from", "o"),
    ("or", "o"), ("one", "o"), ("had", "v"), ("by", "o"), ("word", "n"), ("but", "o"),
    ("not", "o"), ("what", "o"), ("all", "o"), ("were", "v"), ("we", "o"), ("when", "o"),
    ("your", "o"), ("can", "o"), ("said", "v"), ("there", "o"), ("use", "v"), ("an", "o"),
    ("each", "o"), ("which", "o"), ("she", "o"), ("do", "v"), ("how", "o"), ("their", "o"),
    ("if", "o"), ("will", "o"), ("up", "o"), ("other", "o"), ("about", "o"), ("out", "o"),
    ("many", "o"), ("then", "o"), ("them", "o"), ("these", "o"), ("so", "o"), ("some", "o"),
    ("her", "o"), ("would", "o"), ("make", "v"), ("like", "v"), ("him", "o"), ("into", "o"),
    ("time", "n"), ("has", "v"), ("look", "v"), ("two", "o"), ("more", "o"), ("write", "v"),
    ("go", "v"), ("see", "v"), ("number", "n"), ("no", "o"), ("way", "n"), ("could", "o"),
    ("people", "n"), ("my", "o"), ("than", "o"), ("first", "a"), ("water", "n"), ("been", "v"),
    ("call", "v"), ("who", "o"), ("oil", "n"), ("its", "o"), ("now", "o"), ("find", "v"),
    ("long", "a"), ("down", "o"), ("day", "n"), ("did", "v"), ("get", "v"), ("come", "v"),
    ("made", "v"), ("may", "o"), ("part", "n"),
    # 101–200
    ("over", "o"), ("new", "a"), ("sound", "n"), ("take", "v"), ("only", "o"), ("little", "a"),
    ("work", "v"), ("know", "v"), ("place", "n"), ("year", "n"), ("live", "v"), ("me", "o"),
    ("back", "o"), ("give", "v"), ("most", "o"), ("very", "o"), ("after", "o"), ("thing", "n"),
    ("our", "o"), ("just", "o"), ("name", "n"), ("good", "a"), ("sentence", "n"), ("man", "n"),
    ("think", "v"), ("say", "v"), ("great", "a"), ("where", "o"), ("help", "v"), ("through", "o"),
    ("much", "o"), ("before", "o"), ("line", "n"), ("right", "a"), ("too", "o"), ("mean", "v"),
    ("old", "a"), ("any", "o"), ("same", "a"), ("tell", "v"), ("boy", "n"), ("follow", "v"),
    ("came", "v"), ("want", "v"), ("show", "v"), ("also", "o"), ("around", "o"), ("form", "n"),
    ("three", "o"), ("small", "a"), ("set", "v"), ("put", "v"), ("end", "n"), ("does", "v"),
    ("another", "o"), ("well", "o"), ("large", "a"), ("must", "o"), ("big", "a"), ("even", "o"),
    ("such", "o"), ("because", "o"), ("turn", "v"), ("here", "o"), ("why", "o"), ("ask", "v"),
    ("went", "v"), ("men", "n"), ("read", "v"), ("need", "v"), ("land", "n"), ("different", "a"),
    ("home", "n"), ("us", "o"), ("move", "v"), ("try", "v"), ("kind", "a"), ("hand", "n"),
    ("picture", "n"), ("again", "o"), ("change", "v"), ("off", "o"), ("play", "v"),
    ("spell", "v"), ("air", "n"), ("away", "o"), ("animal", "n"), ("house", "n"), ("point", "n"),
    ("page", "n"), ("letter", "n"), ("mother", "n"), ("answer", "n"), ("found", "v"),
    ("study", "v"), ("still", "o"), ("learn", "v"), ("should", "o"), ("America", "n"),
    ("world", "n"),
    # 201–300
    ("high", "a"), ("every", "o"), ("near", "o"), ("add", "v"), ("food", "n"), ("between", "o"),
    ("own", "a"), ("below", "o"), ("country", "n"), ("plant", "n"), ("last", "a"),
    ("school", "n"), ("father", "n"), ("keep", "v"), ("tree", "n"), ("never", "o"),
    ("start", "v"), ("city", "n"), ("earth", "n"), ("eye", "n"), ("light", "n"),
    ("thought", "n"), ("head", "n"), ("under", "o"), ("story", "n"), ("saw", "v"), ("left", "a"),
    ("don't", "v"), ("few", "o"), ("while", "o"), ("along", "o"), ("might", "o"), ("close", "v"),
    ("something", "o"), ("seem", "v"), ("next", "a"), ("hard", "a"), ("open", "v"),
    ("example", "n"), ("begin", "v"), ("life", "n"), ("always", "o"), ("those", "o"),
    ("both", "o"), ("paper", "n"), ("together", "o"), ("got", "v"), ("group", "n"), ("often", "o"),
    ("run", "v"), ("important", "a"), ("until", "o"), ("children", "n"), ("side", "n"),
    ("feet", "n"), ("car", "n"), ("mile", "n"), ("night", "n"), ("walk", "v"), ("white", "a"),
    ("sea", "n"), ("began", "v"), ("grow", "v"), ("took", "v"), ("river", "n"), ("four", "o"),
    ("carry", "v"), ("state", "n"), ("once", "o"), ("book", "n"), ("hear", "v"), ("stop", "v"),
    ("without", "o"), ("second", "a"), ("later", "o"), ("miss", "v"), ("idea", "n"),
    ("enough", "o"), ("eat", "v"), ("face", "n"), ("watch", "v"), ("far", "o"), ("Indian", "n"),
    ("really", "o"), ("almost", "o"), ("let", "v"), ("above", "o"), ("girl", "n"),
    ("sometimes", "o"), ("mountain", "n"), ("cut", "v"), ("young", "a"), ("talk", "v"),
    ("soon", "o"), ("list", "n"), ("song", "n"), ("being", "v"), ("leave", "v"), ("family", "n"),
    ("it's", "o"),
]

# ---------------------------------------------------------------------------
# Themenlisten (deutsch, 1.–4. Klasse), je 40–60 Wörter
# ---------------------------------------------------------------------------

THEME_SILBEN = [
    ("Banane", "n"), ("Tomate", "n"), ("Rakete", "n"), ("Kamera", "n"), ("Salami", "n"),
    ("Melone", "n"), ("Zitrone", "n"), ("Schokolade", "n"), ("Marmelade", "n"), ("Limonade", "n"),
    ("Kartoffel", "n"), ("Karotte", "n"), ("Gurke", "n"), ("Blume", "n"), ("Wiese", "n"),
    ("Sonne", "n"), ("Wolke", "n"), ("Katze", "n"), ("Hase", "n"), ("Biene", "n"),
    ("Vogel", "n"), ("Igel", "n"), ("Esel", "n"), ("Kamel", "n"), ("Giraffe", "n"),
    ("Elefant", "n"), ("Papagei", "n"), ("Schnecke", "n"), ("Ameise", "n"), ("Nudel", "n"),
    ("Kuchen", "n"), ("Butter", "n"), ("Zucker", "n"), ("Teller", "n"), ("Löffel", "n"),
    ("Gabel", "n"), ("Tasse", "n"), ("Flasche", "n"), ("Lampe", "n"), ("Leiter", "n"),
    ("Fenster", "n"), ("Treppe", "n"), ("Garten", "n"), ("Wagen", "n"), ("Ampel", "n"),
    ("Puppe", "n"), ("Trommel", "n"), ("Flöte", "n"), ("malen", "v"), ("baden", "v"),
    ("legen", "v"), ("holen", "v"), ("sagen", "v"), ("lachen", "v"), ("winken", "v"),
    ("müde", "a"), ("leise", "a"), ("lustig", "a"),
]

THEME_DEHNUNGS_H = [
    ("fahren", "v"), ("gehen", "v"), ("sehen", "v"), ("stehen", "v"), ("nehmen", "v"),
    ("wohnen", "v"), ("zahlen", "v"), ("wählen", "v"), ("fühlen", "v"), ("führen", "v"),
    ("lehren", "v"), ("drehen", "v"), ("nähen", "v"), ("ziehen", "v"), ("erzählen", "v"),
    ("bohren", "v"), ("mahlen", "v"), ("ahnen", "v"), ("Zahl", "n"), ("Zahn", "n"),
    ("Bahn", "n"), ("Hahn", "n"), ("Kahn", "n"), ("Sahne", "n"), ("Wahl", "n"),
    ("Stahl", "n"), ("Stuhl", "n"), ("Kuh", "n"), ("Schuh", "n"), ("Uhr", "n"),
    ("Ohr", "n"), ("Sohn", "n"), ("Wohnung", "n"), ("Mühle", "n"), ("Höhle", "n"),
    ("Söhne", "n"), ("Bühne", "n"), ("Kühe", "n"), ("Reh", "n"), ("Vieh", "n"),
    ("Lehrer", "n"), ("Lehm", "n"), ("Mehl", "n"), ("Zehe", "n"), ("Jahr", "n"),
    ("Fahrrad", "n"), ("Fahne", "n"), ("Höhe", "n"), ("mehr", "o"), ("sehr", "o"),
    ("ihm", "o"), ("ihn", "o"), ("ihr", "o"), ("ohne", "o"), ("zehn", "o"),
    ("kühl", "a"), ("wahr", "a"), ("fröhlich", "a"),
]

THEME_EI_IE = [
    ("Eis", "n"), ("Ei", "n"), ("Eimer", "n"), ("Eiche", "n"), ("Eule", "n"),
    ("Seite", "n"), ("Zeit", "n"), ("Kleid", "n"), ("Bein", "n"), ("Stein", "n"),
    ("Wein", "n"), ("Reise", "n"), ("Kreide", "n"), ("Meister", "n"), ("Teich", "n"),
    ("Seil", "n"), ("Heim", "n"), ("Leiter", "n"), ("Weide", "n"), ("Geige", "n"),
    ("klein", "a"), ("fein", "a"), ("weit", "a"), ("leicht", "a"), ("weich", "a"),
    ("heiß", "a"), ("weiß", "a"), ("breit", "a"), ("drei", "o"), ("zwei", "o"),
    ("bleiben", "v"), ("schreiben", "v"), ("zeigen", "v"), ("steigen", "v"), ("reisen", "v"),
    ("Wiese", "n"), ("Brief", "n"), ("Biene", "n"), ("Riese", "n"), ("Ziege", "n"),
    ("Spiegel", "n"), ("Stiefel", "n"), ("Dieb", "n"), ("Knie", "n"), ("Liebe", "n"),
    ("Lied", "n"), ("Tier", "n"), ("Bier", "n"), ("Papier", "n"), ("Ferien", "n"),
    ("spielen", "v"), ("liegen", "v"), ("fliegen", "v"), ("ziehen", "v"), ("lieben", "v"),
    ("gießen", "v"), ("verlieren", "v"), ("tief", "a"), ("lieb", "a"), ("vier", "o"),
]

THEME_DOPPELKONSONANTEN = [
    ("kommen", "v"), ("rennen", "v"), ("brennen", "v"), ("kennen", "v"), ("nennen", "v"),
    ("wissen", "v"), ("essen", "v"), ("passen", "v"), ("lassen", "v"), ("hoffen", "v"),
    ("treffen", "v"), ("öffnen", "v"), ("packen", "v"), ("hüpfen", "v"), ("klettern", "v"),
    ("füttern", "v"), ("flattern", "v"), ("schwimmen", "v"), ("summen", "v"), ("klopfen", "v"),
    ("Sommer", "n"), ("Hammer", "n"), ("Zimmer", "n"), ("Kamm", "n"), ("Mutter", "n"),
    ("Butter", "n"), ("Futter", "n"), ("Wetter", "n"), ("Blatt", "n"), ("Wasser", "n"),
    ("Messer", "n"), ("Tasse", "n"), ("Klasse", "n"), ("Kasse", "n"), ("Nuss", "n"),
    ("Fluss", "n"), ("Kuss", "n"), ("Schloss", "n"), ("Puppe", "n"), ("Suppe", "n"),
    ("Treppe", "n"), ("Lippe", "n"), ("Affe", "n"), ("Löffel", "n"), ("Koffer", "n"),
    ("Kissen", "n"), ("Kette", "n"), ("Ball", "n"), ("Halle", "n"), ("Rolle", "n"),
    ("alle", "o"), ("immer", "o"), ("dann", "o"), ("wann", "o"), ("schnell", "a"),
    ("still", "a"), ("hell", "a"), ("satt", "a"), ("dumm", "a"), ("kann", "v"),
]

THEME_SCH = [
    ("Schule", "n"), ("Schuh", "n"), ("Schlitten", "n"), ("Schere", "n"), ("Schrank", "n"),
    ("Schlange", "n"), ("Schnecke", "n"), ("Schaf", "n"), ("Schwein", "n"), ("Schmetterling", "n"),
    ("Schokolade", "n"), ("Schatz", "n"), ("Schnee", "n"), ("Schirm", "n"), ("Schiff", "n"),
    ("Schlüssel", "n"), ("Schublade", "n"), ("Schaukel", "n"), ("Schulter", "n"),
    ("Schwester", "n"),
    ("Fisch", "n"), ("Tisch", "n"), ("Frosch", "n"), ("Busch", "n"), ("Flasche", "n"),
    ("Tasche", "n"), ("Dusche", "n"), ("Kirsche", "n"), ("Muschel", "n"), ("Asche", "n"),
    ("Mensch", "n"), ("Wunsch", "n"), ("Tusche", "n"), ("Masche", "n"), ("Wäsche", "n"),
    ("waschen", "v"), ("wischen", "v"), ("naschen", "v"), ("rauschen", "v"), ("mischen", "v"),
    ("schlafen", "v"), ("schreiben", "v"), ("schwimmen", "v"), ("schauen", "v"), ("schenken", "v"),
    ("schieben", "v"), ("schneiden", "v"), ("schimpfen", "v"), ("schmecken", "v"),
    ("schön", "a"), ("schnell", "a"), ("schwer", "a"), ("scharf", "a"), ("schlau", "a"),
    ("schmal", "a"), ("frisch", "a"), ("falsch", "a"), ("schwarz", "a"),
]

THEME_SP_ST = [
    ("spielen", "v"), ("sparen", "v"), ("spüren", "v"), ("springen", "v"), ("spazieren", "v"),
    ("sprechen", "v"), ("spucken", "v"), ("spinnen", "v"), ("stehen", "v"), ("stellen", "v"),
    ("stören", "v"), ("staunen", "v"), ("stricken", "v"), ("streiten", "v"), ("stolpern", "v"),
    ("basteln", "v"), ("fasten", "v"), ("husten", "v"), ("kosten", "v"), ("flüstern", "v"),
    ("Sport", "n"), ("Spiel", "n"), ("Spinne", "n"), ("Sprache", "n"), ("Spiegel", "n"),
    ("Spitze", "n"), ("Sparschwein", "n"), ("Spielplatz", "n"), ("Spaten", "n"), ("Spatz", "n"),
    ("Stein", "n"), ("Straße", "n"), ("Stuhl", "n"), ("Stern", "n"), ("Stadt", "n"),
    ("Stimme", "n"), ("Stunde", "n"), ("Stiefel", "n"), ("Storch", "n"), ("Strand", "n"),
    ("Strumpf", "n"), ("Stock", "n"), ("Stift", "n"), ("Fenster", "n"), ("Kasten", "n"),
    ("Nest", "n"), ("Wurst", "n"), ("Post", "n"), ("Angst", "n"), ("Obst", "n"),
    ("Wespe", "n"), ("Knospe", "n"), ("Kiste", "n"), ("Pinsel", "n"),
    ("spät", "a"), ("spannend", "a"), ("stark", "a"), ("steil", "a"), ("stolz", "a"),
]

THEME_D_T = [
    ("Hund", "n"), ("Wald", "n"), ("Bild", "n"), ("Kind", "n"), ("Hand", "n"),
    ("Rad", "n"), ("Bad", "n"), ("Pferd", "n"), ("Held", "n"), ("Geld", "n"),
    ("Freund", "n"), ("Mund", "n"), ("Abend", "n"), ("Fahrrad", "n"), ("Hemd", "n"),
    ("Bett", "n"), ("Blatt", "n"), ("Brot", "n"), ("Bart", "n"), ("Boot", "n"),
    ("Hut", "n"), ("Blut", "n"), ("Zelt", "n"), ("Welt", "n"), ("Wort", "n"),
    ("Ort", "n"), ("Sport", "n"), ("Tante", "n"), ("Tasche", "n"), ("Dose", "n"),
    ("Dach", "n"), ("Dorf", "n"), ("Decke", "n"), ("Daumen", "n"), ("Tier", "n"),
    ("Tafel", "n"), ("Tor", "n"), ("Turm", "n"), ("Teller", "n"),
    ("rot", "a"), ("bunt", "a"), ("gesund", "a"), ("blind", "a"), ("wild", "a"),
    ("kalt", "a"), ("alt", "a"), ("laut", "a"), ("gut", "a"), ("hart", "a"),
    ("dunkel", "a"), ("dick", "a"), ("dünn", "a"), ("tief", "a"), ("teuer", "a"),
    ("finden", "v"), ("baden", "v"), ("reden", "v"), ("warten", "v"), ("bitten", "v"),
]

THEME_WELTRAUM = [
    ("Rakete", "n"), ("Planet", "n"), ("Stern", "n"), ("Sternbild", "n"), ("Mond", "n"),
    ("Sonne", "n"), ("Erde", "n"), ("Mars", "n"), ("Venus", "n"), ("Jupiter", "n"),
    ("Saturn", "n"), ("Merkur", "n"), ("Neptun", "n"), ("Uranus", "n"), ("Komet", "n"),
    ("Meteorit", "n"), ("Asteroid", "n"), ("Galaxie", "n"), ("Universum", "n"), ("Weltall", "n"),
    ("Weltraum", "n"), ("Astronaut", "n"), ("Raumschiff", "n"), ("Raumstation", "n"),
    ("Raumanzug", "n"), ("Helm", "n"), ("Sauerstoff", "n"), ("Schwerkraft", "n"),
    ("Teleskop", "n"), ("Fernrohr", "n"), ("Satellit", "n"), ("Umlaufbahn", "n"),
    ("Krater", "n"), ("Staub", "n"), ("Licht", "n"), ("Dunkelheit", "n"), ("Nacht", "n"),
    ("Himmel", "n"), ("Milchstraße", "n"), ("Sonnensystem", "n"), ("Mondlandung", "n"),
    ("Start", "n"), ("Landung", "n"), ("Forscher", "n"), ("Roboter", "n"),
    ("starten", "v"), ("landen", "v"), ("fliegen", "v"), ("schweben", "v"), ("forschen", "v"),
    ("entdecken", "v"), ("beobachten", "v"), ("leuchten", "v"), ("kreisen", "v"),
    ("unendlich", "a"), ("dunkel", "a"), ("hell", "a"), ("riesig", "a"), ("fern", "a"),
]
