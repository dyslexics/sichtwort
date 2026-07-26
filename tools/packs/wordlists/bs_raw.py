# -*- coding: utf-8 -*-
"""Rohliste Grundwortschatz BKS (Bosnisch/Kroatisch/Serbisch), lateinische Schrift.
Auswahl: haeufigste Woerter des Lese-Erstunterrichts, moeglichst in allen drei
Standardvarianten gleich/verstaendlich. Ijekavische Formen (BiH + HR + ME),
bei kruh/hljeb-Divergenzen die breiter verstandene Variante.
Typ: n=Nomen, v=Verb, a=Adjektiv, o=Sonstiges (Funktionswoerter, Zahlen, Adverbien).
"""

WORDS = [
    # --- Pronomen / Determinatoren ---
    ("ja", "o"), ("ti", "o"), ("on", "o"), ("ona", "o"), ("ono", "o"),
    ("mi", "o"), ("vi", "o"), ("oni", "o"), ("one", "o"), ("se", "o"),
    ("moj", "o"), ("tvoj", "o"), ("njegov", "o"), ("njen", "o"), ("naš", "o"),
    ("vaš", "o"), ("njihov", "o"), ("svoj", "o"), ("ovaj", "o"), ("taj", "o"),
    ("onaj", "o"), ("ova", "o"), ("ovo", "o"), ("ta", "o"), ("to", "o"),
    ("sve", "o"), ("svi", "o"), ("svaki", "o"), ("neki", "o"), ("nešto", "o"),
    ("ništa", "o"), ("niko", "o"), ("neko", "o"), ("ko", "o"), ("šta", "o"),
    ("koji", "o"), ("kakav", "o"), ("mene", "o"), ("tebe", "o"), ("nama", "o"),

    # --- Frageadverbien / Adverbien ---
    ("gdje", "o"), ("kada", "o"), ("kako", "o"), ("zašto", "o"), ("koliko", "o"),
    ("ovdje", "o"), ("tamo", "o"), ("ovamo", "o"), ("sada", "o"), ("tada", "o"),
    ("danas", "o"), ("sutra", "o"), ("juče", "o"), ("uvijek", "o"), ("nikada", "o"),
    ("ponekad", "o"), ("već", "o"), ("još", "o"), ("opet", "o"), ("odmah", "o"),
    ("brzo", "o"), ("polako", "o"), ("jako", "o"), ("malo", "o"), ("mnogo", "o"),
    ("više", "o"), ("manje", "o"), ("dobro", "o"), ("loše", "o"), ("gore", "o"),
    ("dolje", "o"), ("naprijed", "o"), ("nazad", "o"), ("blizu", "o"), ("daleko", "o"),
    ("unutra", "o"), ("vani", "o"), ("zajedno", "o"), ("možda", "o"), ("sigurno", "o"),
    ("samo", "o"), ("isto", "o"), ("tako", "o"), ("skoro", "o"), ("uskoro", "o"),
    ("rano", "o"), ("kasno", "o"), ("noćas", "o"), ("jutros", "o"), ("uvečer", "o"),

    # --- Praepositionen ---
    ("na", "o"), ("iz", "o"), ("od", "o"), ("do", "o"), ("za", "o"),
    ("po", "o"), ("pri", "o"), ("pred", "o"), ("iza", "o"), ("ispod", "o"),
    ("iznad", "o"), ("između", "o"), ("kroz", "o"), ("preko", "o"), ("prema", "o"),
    ("bez", "o"), ("uz", "o"), ("kod", "o"), ("nakon", "o"), ("protiv", "o"),
    ("sa", "o"), ("ispred", "o"), ("pored", "o"),

    # --- Konjunktionen / Partikeln ---
    ("ali", "o"), ("ili", "o"), ("pa", "o"), ("da", "o"), ("jer", "o"),
    ("ako", "o"), ("kad", "o"), ("dok", "o"), ("nego", "o"), ("iako", "o"),
    ("ne", "o"), ("li", "o"), ("evo", "o"), ("eto", "o"), ("hvala", "o"),
    ("molim", "o"), ("zdravo", "o"), ("ćao", "o"), ("nema", "o"), ("ima", "o"),

    # --- Zahlen ---
    ("jedan", "o"), ("dva", "o"), ("tri", "o"), ("četiri", "o"), ("pet", "o"),
    ("šest", "o"), ("sedam", "o"), ("osam", "o"), ("devet", "o"), ("deset", "o"),
    ("jedanaest", "o"), ("dvanaest", "o"), ("dvadeset", "o"), ("trideset", "o"),
    ("stotina", "o"), ("hiljada", "o"), ("nula", "o"),

    # --- Familie / Menschen ---
    ("mama", "n"), ("tata", "n"), ("majka", "n"), ("otac", "n"), ("brat", "n"),
    ("sestra", "n"), ("baka", "n"), ("djed", "n"), ("dijete", "n"), ("djeca", "n"),
    ("sin", "n"), ("kćerka", "n"), ("dječak", "n"), ("djevojčica", "n"), ("čovjek", "n"),
    ("žena", "n"), ("muž", "n"), ("prijatelj", "n"), ("prijateljica", "n"), ("porodica", "n"),
    ("tetka", "n"), ("ujak", "n"), ("stric", "n"), ("unuk", "n"), ("beba", "n"),
    ("drug", "n"), ("momak", "n"), ("djevojka", "n"), ("ljudi", "n"), ("komšija", "n"),
    ("gost", "n"), ("doktor", "n"), ("policajac", "n"), ("vozač", "n"), ("pekar", "n"),

    # --- Schule ---
    ("škola", "n"), ("učitelj", "n"), ("učiteljica", "n"), ("učenik", "n"), ("razred", "n"),
    ("knjiga", "n"), ("olovka", "n"), ("papir", "n"), ("slovo", "n"), ("riječ", "n"),
    ("rečenica", "n"), ("broj", "n"), ("zadatak", "n"), ("pitanje", "n"), ("odgovor", "n"),
    ("ploča", "n"), ("klupa", "n"), ("torba", "n"), ("priča", "n"), ("pjesma", "n"),
    ("crtež", "n"), ("boja", "n"), ("kreda", "n"), ("učionica", "n"), ("odmor", "n"),
    ("ocjena", "n"), ("gumica", "n"), ("bojica", "n"), ("strana", "n"), ("naslov", "n"),
    ("ime", "n"), ("prezime", "n"), ("zvono", "n"), ("ruksak", "n"), ("lektira", "n"),

    # --- Tiere ---
    ("pas", "n"), ("mačka", "n"), ("konj", "n"), ("krava", "n"), ("svinja", "n"),
    ("ovca", "n"), ("koza", "n"), ("kokoš", "n"), ("pijetao", "n"), ("patka", "n"),
    ("guska", "n"), ("riba", "n"), ("ptica", "n"), ("miš", "n"), ("zec", "n"),
    ("lisica", "n"), ("vuk", "n"), ("medvjed", "n"), ("jelen", "n"), ("lav", "n"),
    ("tigar", "n"), ("slon", "n"), ("majmun", "n"), ("žirafa", "n"), ("zmija", "n"),
    ("žaba", "n"), ("puž", "n"), ("pčela", "n"), ("leptir", "n"), ("mrav", "n"),
    ("muha", "n"), ("pauk", "n"), ("vjeverica", "n"), ("jež", "n"), ("magarac", "n"),
    ("mače", "n"), ("štene", "n"), ("gnijezdo", "n"), ("krilo", "n"), ("rep", "n"),

    # --- Koerper ---
    ("glava", "n"), ("kosa", "n"), ("oko", "n"), ("uho", "n"), ("nos", "n"),
    ("usta", "n"), ("zub", "n"), ("jezik", "n"), ("vrat", "n"), ("rame", "n"),
    ("ruka", "n"), ("prst", "n"), ("noga", "n"), ("koljeno", "n"), ("stopalo", "n"),
    ("leđa", "n"), ("trbuh", "n"), ("srce", "n"), ("lice", "n"), ("obraz", "n"),
    ("brada", "n"), ("čelo", "n"), ("koža", "n"), ("krv", "n"), ("kost", "n"),
    ("suza", "n"), ("glas", "n"), ("tijelo", "n"),

    # --- Essen / Trinken ---
    ("hljeb", "n"), ("mlijeko", "n"), ("voda", "n"), ("sok", "n"), ("čaj", "n"),
    ("kafa", "n"), ("sir", "n"), ("maslac", "n"), ("jaje", "n"), ("meso", "n"),
    ("supa", "n"), ("krompir", "n"), ("povrće", "n"), ("voće", "n"), ("jabuka", "n"),
    ("kruška", "n"), ("banana", "n"), ("grožđe", "n"), ("jagoda", "n"), ("trešnja", "n"),
    ("šljiva", "n"), ("breskva", "n"), ("limun", "n"), ("lubenica", "n"), ("orah", "n"),
    ("med", "n"), ("šećer", "n"), ("brašno", "n"), ("kolač", "n"), ("torta", "n"),
    ("sladoled", "n"), ("čokolada", "n"), ("bombon", "n"), ("keks", "n"), ("pita", "n"),
    ("ručak", "n"), ("doručak", "n"), ("večera", "n"), ("hrana", "n"), ("salata", "n"),

    # --- Haus / Dinge ---
    ("kuća", "n"), ("stan", "n"), ("soba", "n"), ("kuhinja", "n"), ("kupatilo", "n"),
    ("vrata", "n"), ("prozor", "n"), ("pod", "n"), ("zid", "n"), ("krov", "n"),
    ("krevet", "n"), ("stolica", "n"), ("ormar", "n"), ("polica", "n"), ("lampa", "n"),
    ("ogledalo", "n"), ("tepih", "n"), ("jastuk", "n"), ("ključ", "n"), ("sat", "n"),
    ("telefon", "n"), ("televizor", "n"), ("nož", "n"), ("tanjir", "n"), ("čaša", "n"),
    ("boca", "n"), ("sapun", "n"), ("ručnik", "n"), ("četkica", "n"), ("peć", "n"),
    ("sto", "n"), ("kanta", "n"), ("stepenice", "n"), ("dvorište", "n"), ("garaža", "n"),
    ("bašta", "n"), ("ograda", "n"), ("svjetlo", "n"), ("sjena", "n"), ("slika", "n"),

    # --- Natur ---
    ("sunce", "n"), ("mjesec", "n"), ("zvijezda", "n"), ("nebo", "n"), ("oblak", "n"),
    ("kiša", "n"), ("snijeg", "n"), ("vjetar", "n"), ("led", "n"), ("more", "n"),
    ("rijeka", "n"), ("jezero", "n"), ("potok", "n"), ("planina", "n"), ("brdo", "n"),
    ("šuma", "n"), ("drvo", "n"), ("list", "n"), ("cvijet", "n"), ("trava", "n"),
    ("grana", "n"), ("korijen", "n"), ("sjeme", "n"), ("kamen", "n"), ("pijesak", "n"),
    ("zemlja", "n"), ("polje", "n"), ("put", "n"), ("most", "n"), ("staza", "n"),
    ("vatra", "n"), ("dim", "n"), ("zrak", "n"), ("duga", "n"), ("mrak", "n"),

    # --- Zeit ---
    ("proljeće", "n"), ("ljeto", "n"), ("jesen", "n"), ("zima", "n"), ("dan", "n"),
    ("noć", "n"), ("jutro", "n"), ("veče", "n"), ("godina", "n"), ("minuta", "n"),
    ("vrijeme", "n"), ("praznik", "n"), ("rođendan", "n"), ("sedmica", "n"),

    # --- Stadt / Verkehr / Spiel ---
    ("grad", "n"), ("selo", "n"), ("ulica", "n"), ("trgovina", "n"), ("bolnica", "n"),
    ("crkva", "n"), ("park", "n"), ("igralište", "n"), ("auto", "n"), ("autobus", "n"),
    ("voz", "n"), ("avion", "n"), ("brod", "n"), ("bicikl", "n"), ("lopta", "n"),
    ("igra", "n"), ("igračka", "n"), ("lutka", "n"), ("zmaj", "n"), ("balon", "n"),
    ("poklon", "n"), ("novac", "n"), ("pismo", "n"), ("film", "n"), ("muzika", "n"),
    ("ples", "n"), ("sport", "n"), ("kino", "n"), ("pijaca", "n"), ("zoo", "n"),

    # --- Kleidung ---
    ("odjeća", "n"), ("majica", "n"), ("haljina", "n"), ("cipela", "n"), ("čarapa", "n"),
    ("kapa", "n"), ("jakna", "n"), ("šal", "n"), ("rukavica", "n"), ("dugme", "n"),
    ("hlače", "n"), ("suknja", "n"), ("kaput", "n"), ("papuča", "n"),

    # --- Verben ---
    ("biti", "v"), ("imati", "v"), ("htjeti", "v"), ("moći", "v"), ("morati", "v"),
    ("raditi", "v"), ("ići", "v"), ("doći", "v"), ("otići", "v"), ("gledati", "v"),
    ("vidjeti", "v"), ("čuti", "v"), ("slušati", "v"), ("govoriti", "v"), ("reći", "v"),
    ("pričati", "v"), ("pitati", "v"), ("odgovoriti", "v"), ("znati", "v"), ("misliti", "v"),
    ("učiti", "v"), ("čitati", "v"), ("pisati", "v"), ("crtati", "v"), ("brojati", "v"),
    ("igrati", "v"), ("trčati", "v"), ("skakati", "v"), ("hodati", "v"), ("sjediti", "v"),
    ("stajati", "v"), ("ležati", "v"), ("spavati", "v"), ("ustati", "v"), ("jesti", "v"),
    ("piti", "v"), ("kuhati", "v"), ("praviti", "v"), ("dati", "v"), ("uzeti", "v"),
    ("nositi", "v"), ("donijeti", "v"), ("staviti", "v"), ("otvoriti", "v"), ("zatvoriti", "v"),
    ("tražiti", "v"), ("naći", "v"), ("izgubiti", "v"), ("kupiti", "v"), ("prodati", "v"),
    ("platiti", "v"), ("pomoći", "v"), ("voljeti", "v"), ("smijati", "v"), ("plakati", "v"),
    ("vikati", "v"), ("pjevati", "v"), ("plesati", "v"), ("svirati", "v"), ("letjeti", "v"),
    ("plivati", "v"), ("voziti", "v"), ("putovati", "v"), ("čekati", "v"), ("žuriti", "v"),
    ("početi", "v"), ("završiti", "v"), ("čistiti", "v"), ("prati", "v"), ("obući", "v"),
    ("sanjati", "v"), ("željeti", "v"), ("trebati", "v"), ("dobiti", "v"), ("poslati", "v"),
    ("zvati", "v"), ("razumjeti", "v"), ("zaboraviti", "v"), ("zapamtiti", "v"), ("mjeriti", "v"),
    ("rasti", "v"), ("padati", "v"), ("penjati", "v"), ("gurati", "v"), ("vući", "v"),
    ("baciti", "v"), ("uhvatiti", "v"), ("držati", "v"), ("pustiti", "v"), ("paziti", "v"),
    ("brinuti", "v"), ("graditi", "v"), ("kopati", "v"), ("saditi", "v"), ("brati", "v"),
    ("hraniti", "v"), ("kupati", "v"), ("šetati", "v"), ("vratiti", "v"), ("ostati", "v"),
    ("ući", "v"), ("izaći", "v"), ("sjesti", "v"), ("javiti", "v"), ("pokazati", "v"),
    ("zaspati", "v"), ("probuditi", "v"), ("sakriti", "v"), ("bojati", "v"), ("bježati", "v"),

    # --- Adjektive ---
    ("velik", "a"), ("mali", "a"), ("dobar", "a"), ("loš", "a"), ("lijep", "a"),
    ("ružan", "a"), ("nov", "a"), ("star", "a"), ("mlad", "a"), ("dug", "a"),
    ("kratak", "a"), ("visok", "a"), ("nizak", "a"), ("širok", "a"), ("uzak", "a"),
    ("debeo", "a"), ("mršav", "a"), ("jak", "a"), ("slab", "a"), ("brz", "a"),
    ("spor", "a"), ("topao", "a"), ("hladan", "a"), ("vruć", "a"), ("mokar", "a"),
    ("suh", "a"), ("čist", "a"), ("prljav", "a"), ("pun", "a"), ("prazan", "a"),
    ("težak", "a"), ("lak", "a"), ("tvrd", "a"), ("mekan", "a"), ("sladak", "a"),
    ("kiseo", "a"), ("slan", "a"), ("gorak", "a"), ("svijetao", "a"), ("taman", "a"),
    ("bijel", "a"), ("crn", "a"), ("crven", "a"), ("plav", "a"), ("zelen", "a"),
    ("žut", "a"), ("smeđ", "a"), ("siv", "a"), ("ljubičast", "a"), ("veseo", "a"),
    ("tužan", "a"), ("ljut", "a"), ("umoran", "a"), ("gladan", "a"), ("žedan", "a"),
    ("bolestan", "a"), ("zdrav", "a"), ("pametan", "a"), ("hrabar", "a"), ("tih", "a"),
    ("glasan", "a"), ("bogat", "a"), ("prvi", "a"), ("drugi", "a"), ("treći", "a"),
    ("zadnji", "a"), ("isti", "a"), ("različit", "a"), ("okrugao", "a"), ("ravan", "a"),
    ("oštar", "a"), ("dubok", "a"), ("plitak", "a"), ("važan", "a"), ("smiješan", "a"),
    ("strašan", "a"), ("drag", "a"), ("ljubazan", "a"), ("vrijedan", "a"), ("lijen", "a"),
    ("sam", "a"), ("cijeli", "a"), ("pravi", "a"), ("desni", "a"), ("lijevi", "a"),
    ("gornji", "a"), ("donji", "a"), ("srednji", "a"), ("mlak", "a"), ("nježan", "a"),
    ("divlji", "a"), ("pitom", "a"), ("mudar", "a"), ("sretan", "a"), ("blizak", "a"),
]

# Reserve, falls nach Dedupe aufgefuellt werden muss
EXTRA = [
    ("gitara", "n"), ("bubanj", "n"), ("klavir", "n"), ("truba", "n"), ("harmonika", "n"),
    ("kruna", "n"), ("vitez", "n"), ("princeza", "n"), ("čarolija", "n"), ("vila", "n"),
    ("ljestve", "n"), ("čekić", "n"), ("ekser", "n"), ("pila", "n"), ("lopata", "n"),
    ("kofer", "n"), ("karta", "n"), ("stanica", "n"), ("aerodrom", "n"), ("luka", "n"),
    ("mrkva", "n"), ("luk", "n"), ("kupus", "n"), ("grašak", "n"), ("pasulj", "n"),
    ("tigrić", "n"), ("ribica", "n"), ("ptičica", "n"), ("kućica", "n"), ("cvjetić", "n"),
    ("smijeh", "n"), ("radost", "n"), ("strah", "n"), ("ljubav", "n"), ("nada", "n"),
    ("misao", "n"), ("san", "n"), ("posao", "n"), ("pomoć", "n"), ("pravilo", "n"),
]
