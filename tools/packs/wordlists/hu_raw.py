# -*- coding: utf-8 -*-
"""Grundwortschatz Ungarisch (hu) fuer Sichtwort — Rohliste (Checkpoint).

Feld 1: Wort (ungetrennt), Feld 2: Wortart n/v/a/o
Auswahl: haeufigste Woerter des ungarischen Lese-Erstunterrichts,
kindgerecht, Einzelwoerter, keine Duplikate.
"""

WORDS = [
    # --- Funktionswoerter, Pronomen, Adverbien (o) ---
    ("a", "o"), ("az", "o"), ("egy", "o"), ("és", "o"), ("de", "o"),
    ("vagy", "o"), ("hogy", "o"), ("nem", "o"), ("igen", "o"), ("is", "o"),
    ("csak", "o"), ("már", "o"), ("még", "o"), ("itt", "o"), ("ott", "o"),
    ("most", "o"), ("majd", "o"), ("mindig", "o"), ("soha", "o"), ("nagyon", "o"),
    ("ez", "o"), ("én", "o"), ("te", "o"), ("ő", "o"), ("mi", "o"),
    ("ti", "o"), ("ők", "o"), ("ki", "o"), ("hol", "o"), ("hová", "o"),
    ("honnan", "o"), ("mikor", "o"), ("miért", "o"), ("hogyan", "o"), ("mert", "o"),
    ("ha", "o"), ("mint", "o"), ("talán", "o"), ("persze", "o"), ("újra", "o"),
    ("együtt", "o"), ("külön", "o"), ("alatt", "o"), ("fölött", "o"), ("mellett", "o"),
    ("mögött", "o"), ("előtt", "o"), ("között", "o"), ("nélkül", "o"), ("után", "o"),
    ("felé", "o"), ("körül", "o"), ("belül", "o"), ("kívül", "o"), ("fel", "o"),
    ("le", "o"), ("be", "o"), ("el", "o"), ("vissza", "o"), ("ide", "o"),
    ("oda", "o"), ("innen", "o"), ("onnan", "o"), ("mindenhol", "o"), ("sehol", "o"),
    ("valahol", "o"), ("minden", "o"), ("semmi", "o"), ("valami", "o"), ("mindenki", "o"),
    ("senki", "o"), ("valaki", "o"), ("néhány", "o"), ("ma", "o"), ("holnap", "o"),
    ("tegnap", "o"), ("reggel", "o"), ("este", "o"), ("éjjel", "o"), ("nappal", "o"),
    ("gyorsan", "o"), ("lassan", "o"), ("jól", "o"), ("rosszul", "o"), ("szépen", "o"),
    ("hamar", "o"), ("azonnal", "o"), ("tényleg", "o"), ("tessék", "o"), ("köszönöm", "o"),
    ("szia", "o"), ("viszlát", "o"), ("jaj", "o"), ("kérem", "o"), ("bocsánat", "o"),
    ("hurrá", "o"), ("pedig", "o"), ("tehát", "o"), ("aztán", "o"), ("amikor", "o"),
    ("ahol", "o"), ("aki", "o"), ("ami", "o"), ("sem", "o"), ("hány", "o"),
    ("mennyi", "o"), ("melyik", "o"), ("milyen", "o"), ("igazán", "o"), ("alig", "o"),
    ("elég", "o"), ("túl", "o"), ("néha", "o"), ("gyakran", "o"), ("rögtön", "o"),
    ("nekem", "o"), ("neked", "o"), ("neki", "o"), ("velem", "o"), ("vele", "o"),

    # --- Zahlen (o) ---
    ("nulla", "o"), ("kettő", "o"), ("három", "o"), ("négy", "o"), ("öt", "o"),
    ("hat", "o"), ("hét", "o"), ("nyolc", "o"), ("kilenc", "o"), ("tíz", "o"),
    ("tizenegy", "o"), ("húsz", "o"), ("harminc", "o"), ("negyven", "o"), ("ötven", "o"),
    ("hatvan", "o"), ("hetven", "o"), ("nyolcvan", "o"), ("kilencven", "o"), ("száz", "o"),
    ("ezer", "o"),

    # --- Familie & Menschen (n) ---
    ("anya", "n"), ("apa", "n"), ("gyerek", "n"), ("fiú", "n"), ("lány", "n"),
    ("baba", "n"), ("testvér", "n"), ("nagymama", "n"), ("nagypapa", "n"), ("család", "n"),
    ("néni", "n"), ("bácsi", "n"), ("barát", "n"), ("ember", "n"), ("nő", "n"),
    ("férfi", "n"), ("felnőtt", "n"), ("név", "n"),

    # --- Schule (n) ---
    ("iskola", "n"), ("tanár", "n"), ("tanító", "n"), ("osztály", "n"), ("diák", "n"),
    ("tanuló", "n"), ("könyv", "n"), ("füzet", "n"), ("ceruza", "n"), ("toll", "n"),
    ("radír", "n"), ("papír", "n"), ("táska", "n"), ("pad", "n"), ("tábla", "n"),
    ("kréta", "n"), ("olló", "n"), ("ragasztó", "n"), ("szó", "n"), ("betű", "n"),
    ("szám", "n"), ("mondat", "n"), ("mese", "n"), ("vers", "n"), ("rajz", "n"),
    ("kép", "n"), ("óra", "n"), ("szünet", "n"), ("lecke", "n"), ("feladat", "n"),
    ("játék", "n"), ("labda", "n"), ("kérdés", "n"), ("válasz", "n"), ("hiba", "n"),

    # --- Haus & Wohnen (n) ---
    ("ház", "n"), ("lakás", "n"), ("szoba", "n"), ("konyha", "n"), ("fürdőszoba", "n"),
    ("ajtó", "n"), ("ablak", "n"), ("asztal", "n"), ("szék", "n"), ("ágy", "n"),
    ("szekrény", "n"), ("lámpa", "n"), ("kulcs", "n"), ("tükör", "n"), ("szőnyeg", "n"),
    ("fal", "n"), ("tető", "n"), ("kert", "n"), ("udvar", "n"), ("lépcső", "n"),
    ("doboz", "n"), ("kosár", "n"), ("seprű", "n"), ("párna", "n"), ("takaró", "n"),

    # --- Essen & Trinken (n) ---
    ("kenyér", "n"), ("vaj", "n"), ("sajt", "n"), ("tej", "n"), ("víz", "n"),
    ("alma", "n"), ("körte", "n"), ("banán", "n"), ("szőlő", "n"), ("eper", "n"),
    ("dinnye", "n"), ("répa", "n"), ("krumpli", "n"), ("paradicsom", "n"), ("uborka", "n"),
    ("hagyma", "n"), ("leves", "n"), ("hús", "n"), ("hal", "n"), ("tojás", "n"),
    ("cukor", "n"), ("só", "n"), ("méz", "n"), ("tea", "n"), ("kávé", "n"),
    ("sütemény", "n"), ("csoki", "n"), ("fagylalt", "n"), ("gyümölcs", "n"), ("zöldség", "n"),
    ("reggeli", "n"), ("ebéd", "n"), ("vacsora", "n"), ("étel", "n"), ("ital", "n"),
    ("tányér", "n"), ("pohár", "n"), ("kanál", "n"), ("villa", "n"), ("kés", "n"),
    ("bögre", "n"),

    # --- Tiere (n) ---
    ("kutya", "n"), ("macska", "n"), ("ló", "n"), ("tehén", "n"), ("disznó", "n"),
    ("birka", "n"), ("kecske", "n"), ("tyúk", "n"), ("kakas", "n"), ("kacsa", "n"),
    ("liba", "n"), ("nyúl", "n"), ("egér", "n"), ("madár", "n"), ("veréb", "n"),
    ("gólya", "n"), ("bagoly", "n"), ("róka", "n"), ("farkas", "n"), ("medve", "n"),
    ("őz", "n"), ("szarvas", "n"), ("oroszlán", "n"), ("elefánt", "n"), ("majom", "n"),
    ("zsiráf", "n"), ("teknős", "n"), ("béka", "n"), ("kígyó", "n"), ("pók", "n"),
    ("méh", "n"), ("hangya", "n"), ("lepke", "n"), ("katica", "n"), ("légy", "n"),
    ("sün", "n"), ("mókus", "n"), ("hörcsög", "n"), ("papagáj", "n"), ("delfin", "n"),

    # --- Koerper (n) ---
    ("fej", "n"), ("haj", "n"), ("szem", "n"), ("fül", "n"), ("orr", "n"),
    ("száj", "n"), ("fog", "n"), ("nyelv", "n"), ("arc", "n"), ("nyak", "n"),
    ("váll", "n"), ("kar", "n"), ("kéz", "n"), ("ujj", "n"), ("has", "n"),
    ("hát", "n"), ("láb", "n"), ("térd", "n"), ("talp", "n"), ("szív", "n"),
    ("csont", "n"), ("bőr", "n"), ("könny", "n"),

    # --- Natur (n) ---
    ("nap", "n"), ("hold", "n"), ("csillag", "n"), ("ég", "n"), ("felhő", "n"),
    ("eső", "n"), ("hó", "n"), ("szél", "n"), ("vihar", "n"), ("villám", "n"),
    ("tűz", "n"), ("föld", "n"), ("levegő", "n"), ("tenger", "n"), ("folyó", "n"),
    ("patak", "n"), ("tó", "n"), ("hegy", "n"), ("domb", "n"), ("erdő", "n"),
    ("mező", "n"), ("rét", "n"), ("fa", "n"), ("ág", "n"), ("levél", "n"),
    ("virág", "n"), ("fű", "n"), ("mag", "n"), ("gyökér", "n"), ("kő", "n"),
    ("homok", "n"), ("sár", "n"), ("jég", "n"),

    # --- Zeit (n) ---
    ("idő", "n"), ("év", "n"), ("hónap", "n"), ("perc", "n"), ("dél", "n"),
    ("éjszaka", "n"), ("délután", "n"), ("tavasz", "n"), ("nyár", "n"), ("ősz", "n"),
    ("tél", "n"), ("hétfő", "n"), ("kedd", "n"), ("szerda", "n"), ("csütörtök", "n"),
    ("péntek", "n"), ("szombat", "n"), ("vasárnap", "n"), ("születésnap", "n"), ("karácsony", "n"),
    ("húsvét", "n"), ("ünnep", "n"),

    # --- Stadt, Verkehr, Berufe (n) ---
    ("város", "n"), ("falu", "n"), ("utca", "n"), ("út", "n"), ("tér", "n"),
    ("bolt", "n"), ("piac", "n"), ("posta", "n"), ("kórház", "n"), ("orvos", "n"),
    ("gyógyszer", "n"), ("rendőr", "n"), ("tűzoltó", "n"), ("pék", "n"), ("autó", "n"),
    ("busz", "n"), ("vonat", "n"), ("villamos", "n"), ("bicikli", "n"), ("repülő", "n"),
    ("hajó", "n"), ("motor", "n"), ("kerék", "n"), ("híd", "n"), ("park", "n"),
    ("játszótér", "n"), ("pénz", "n"), ("ajándék", "n"),

    # --- Kleidung (n) ---
    ("ruha", "n"), ("nadrág", "n"), ("ing", "n"), ("pulóver", "n"), ("kabát", "n"),
    ("sapka", "n"), ("sál", "n"), ("kesztyű", "n"), ("cipő", "n"), ("zokni", "n"),
    ("gomb", "n"), ("zseb", "n"),

    # --- Sonstige Nomen (n) ---
    ("telefon", "n"), ("számítógép", "n"), ("televízió", "n"), ("rádió", "n"), ("zene", "n"),
    ("dal", "n"), ("hang", "n"), ("szín", "n"), ("forma", "n"), ("kör", "n"),
    ("pont", "n"), ("vonal", "n"), ("álom", "n"), ("mosoly", "n"), ("csók", "n"),
    ("öröm", "n"), ("erő", "n"), ("baj", "n"), ("munka", "n"), ("csoport", "n"),

    # --- Verben (v) ---
    ("van", "v"), ("nincs", "v"), ("lesz", "v"), ("megy", "v"), ("jön", "v"),
    ("fut", "v"), ("szalad", "v"), ("ugrik", "v"), ("mászik", "v"), ("repül", "v"),
    ("úszik", "v"), ("sétál", "v"), ("áll", "v"), ("ül", "v"), ("fekszik", "v"),
    ("alszik", "v"), ("ébred", "v"), ("indul", "v"), ("érkezik", "v"), ("marad", "v"),
    ("lép", "v"), ("esik", "v"), ("csúszik", "v"), ("eszik", "v"), ("iszik", "v"),
    ("főz", "v"), ("süt", "v"), ("mos", "v"), ("fürdik", "v"), ("öltözik", "v"),
    ("néz", "v"), ("lát", "v"), ("hall", "v"), ("hallgat", "v"), ("figyel", "v"),
    ("olvas", "v"), ("ír", "v"), ("rajzol", "v"), ("fest", "v"), ("számol", "v"),
    ("tanul", "v"), ("tanít", "v"), ("kérdez", "v"), ("felel", "v"), ("mond", "v"),
    ("beszél", "v"), ("mesél", "v"), ("kiabál", "v"), ("suttog", "v"), ("énekel", "v"),
    ("táncol", "v"), ("játszik", "v"), ("nevet", "v"), ("sír", "v"), ("mosolyog", "v"),
    ("örül", "v"), ("fél", "v"), ("szeret", "v"), ("gondol", "v"), ("tud", "v"),
    ("akar", "v"), ("kell", "v"), ("lehet", "v"), ("segít", "v"), ("ad", "v"),
    ("kap", "v"), ("vesz", "v"), ("hoz", "v"), ("visz", "v"), ("tart", "v"),
    ("húz", "v"), ("tol", "v"), ("dob", "v"), ("emel", "v"), ("tesz", "v"),
    ("nyit", "v"), ("zár", "v"), ("tör", "v"), ("vág", "v"), ("hajt", "v"),
    ("épít", "v"), ("javít", "v"), ("keres", "v"), ("talál", "v"), ("gyűjt", "v"),
    ("vár", "v"), ("hív", "v"), ("köszön", "v"), ("ölel", "v"), ("dolgozik", "v"),
    ("pihen", "v"), ("siet", "v"), ("késik", "v"), ("kezd", "v"), ("próbál", "v"),
    ("sikerül", "v"), ("felejt", "v"), ("emlékszik", "v"), ("ismer", "v"), ("hisz", "v"),
    ("remél", "v"), ("választ", "v"), ("mutat", "v"), ("takarít", "v"), ("söpör", "v"),
    ("varr", "v"), ("öntöz", "v"), ("ültet", "v"), ("etet", "v"), ("simogat", "v"),
    ("ugat", "v"), ("nyávog", "v"), ("csipog", "v"), ("világít", "v"), ("fúj", "v"),
    ("virágzik", "v"), ("fogad", "v"), ("vezet", "v"), ("visel", "v"), ("gurul", "v"),

    # --- Adjektive (a) ---
    ("nagy", "a"), ("kicsi", "a"), ("kis", "a"), ("hosszú", "a"), ("rövid", "a"),
    ("magas", "a"), ("alacsony", "a"), ("széles", "a"), ("keskeny", "a"), ("vastag", "a"),
    ("vékony", "a"), ("nehéz", "a"), ("könnyű", "a"), ("erős", "a"), ("gyenge", "a"),
    ("gyors", "a"), ("lassú", "a"), ("új", "a"), ("régi", "a"), ("fiatal", "a"),
    ("öreg", "a"), ("jó", "a"), ("rossz", "a"), ("szép", "a"), ("csúnya", "a"),
    ("tiszta", "a"), ("piszkos", "a"), ("meleg", "a"), ("hideg", "a"), ("forró", "a"),
    ("hűvös", "a"), ("száraz", "a"), ("nedves", "a"), ("vizes", "a"), ("üres", "a"),
    ("tele", "a"), ("édes", "a"), ("savanyú", "a"), ("sós", "a"), ("keserű", "a"),
    ("finom", "a"), ("éhes", "a"), ("szomjas", "a"), ("fáradt", "a"), ("álmos", "a"),
    ("vidám", "a"), ("szomorú", "a"), ("boldog", "a"), ("mérges", "a"), ("nyugodt", "a"),
    ("bátor", "a"), ("okos", "a"), ("buta", "a"), ("ügyes", "a"), ("lusta", "a"),
    ("szorgalmas", "a"), ("kedves", "a"), ("csendes", "a"), ("hangos", "a"), ("sötét", "a"),
    ("világos", "a"), ("fényes", "a"), ("puha", "a"), ("kemény", "a"), ("sima", "a"),
    ("kerek", "a"), ("egyenes", "a"), ("görbe", "a"), ("sok", "a"), ("kevés", "a"),
    ("kész", "a"), ("késő", "a"), ("első", "a"), ("második", "a"), ("harmadik", "a"),
    ("utolsó", "a"), ("egész", "a"), ("fél", "a"), ("más", "a"), ("biztos", "a"),
    ("igaz", "a"), ("drága", "a"), ("olcsó", "a"), ("gazdag", "a"), ("szegény", "a"),
    ("beteg", "a"), ("egészséges", "a"), ("éles", "a"), ("bátortalan", "a"), ("büszke", "a"),

    # --- Farben (a) ---
    ("piros", "a"), ("kék", "a"), ("zöld", "a"), ("sárga", "a"), ("fehér", "a"),
    ("fekete", "a"), ("barna", "a"), ("szürke", "a"), ("rózsaszín", "a"), ("lila", "a"),
    ("narancssárga", "a"), ("arany", "a"), ("ezüst", "a"),
]
