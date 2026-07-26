# -*- coding: utf-8 -*-
"""Grundwortschatz Albanisch (sq) fuer Sichtwort - Rohliste (Wort, Wortart).
Wortarten: n=Nomen, v=Verb, a=Adjektiv, o=Sonstiges (Funktionswoerter, Zahlen, Adverbien)
Standardalbanisch. Adjektive in Grundform ohne Artikel (i/e).
"""

WORDS = [
    # --- Pronomen / Determinative ---
    ("unë", "o"), ("ti", "o"), ("ai", "o"), ("ajo", "o"), ("ne", "o"),
    ("ju", "o"), ("ata", "o"), ("ato", "o"), ("ky", "o"), ("kjo", "o"),
    ("këta", "o"), ("këto", "o"), ("im", "o"), ("ime", "o"), ("yt", "o"),
    ("jote", "o"), ("tij", "o"), ("saj", "o"), ("ynë", "o"), ("jonë", "o"),
    ("juaj", "o"), ("tyre", "o"), ("vetë", "o"), ("kush", "o"), ("çfarë", "o"),
    ("cili", "o"), ("cila", "o"), ("asgjë", "o"), ("diçka", "o"), ("dikush", "o"),
    ("askush", "o"), ("secili", "o"), ("gjithçka", "o"), ("tjetër", "o"), ("gjithë", "o"),

    # --- Konjunktionen / Praepositionen / Partikeln ---
    ("dhe", "o"), ("ose", "o"), ("por", "o"), ("sepse", "o"), ("që", "o"),
    ("nëse", "o"), ("kur", "o"), ("si", "o"), ("ku", "o"), ("pse", "o"),
    ("sa", "o"), ("në", "o"), ("me", "o"), ("pa", "o"), ("për", "o"),
    ("nga", "o"), ("tek", "o"), ("mbi", "o"), ("nën", "o"), ("mes", "o"),
    ("midis", "o"), ("para", "o"), ("pas", "o"), ("deri", "o"), ("rreth", "o"),
    ("sipas", "o"), ("përveç", "o"), ("bashkë", "o"), ("jo", "o"), ("po", "o"),
    ("nuk", "o"), ("edhe", "o"), ("as", "o"), ("veç", "o"), ("gjithashtu", "o"),

    # --- Adverbien ---
    ("shumë", "o"), ("pak", "o"), ("mjaft", "o"), ("fare", "o"), ("sot", "o"),
    ("nesër", "o"), ("dje", "o"), ("tani", "o"), ("pastaj", "o"), ("atëherë", "o"),
    ("gjithmonë", "o"), ("kurrë", "o"), ("ndonjëherë", "o"), ("shpesh", "o"), ("këtu", "o"),
    ("atje", "o"), ("lart", "o"), ("poshtë", "o"), ("brenda", "o"), ("jashtë", "o"),
    ("afër", "o"), ("larg", "o"), ("majtas", "o"), ("djathtas", "o"), ("përpara", "o"),
    ("prapa", "o"), ("ashtu", "o"), ("kështu", "o"), ("mirë", "o"), ("keq", "o"),
    ("shpejt", "o"), ("ngadalë", "o"), ("përsëri", "o"), ("vetëm", "o"), ("ndoshta", "o"),
    ("patjetër", "o"), ("mbase", "o"), ("sërish", "o"),

    # --- Zahlen ---
    ("një", "o"), ("dy", "o"), ("tre", "o"), ("tri", "o"), ("katër", "o"),
    ("pesë", "o"), ("gjashtë", "o"), ("shtatë", "o"), ("tetë", "o"), ("nëntë", "o"),
    ("dhjetë", "o"), ("njëmbëdhjetë", "o"), ("dymbëdhjetë", "o"), ("njëzet", "o"), ("tridhjetë", "o"),
    ("dyzet", "o"), ("pesëdhjetë", "o"), ("njëqind", "o"), ("mijë", "o"),
    ("numër", "n"), ("shifër", "n"),

    # --- Familie / Menschen ---
    ("nënë", "n"), ("baba", "n"), ("prind", "n"), ("vëlla", "n"), ("motër", "n"),
    ("gjysh", "n"), ("gjyshe", "n"), ("djalë", "n"), ("vajzë", "n"), ("fëmijë", "n"),
    ("foshnjë", "n"), ("burrë", "n"), ("grua", "n"), ("njeri", "n"), ("familje", "n"),
    ("dajë", "n"), ("xhaxha", "n"), ("teze", "n"), ("hallë", "n"), ("kushëri", "n"),
    ("mik", "n"), ("shok", "n"), ("shoqe", "n"), ("fqinj", "n"), ("emër", "n"),
    ("mbiemër", "n"), ("moshë", "n"),

    # --- Schule ---
    ("shkollë", "n"), ("mësues", "n"), ("mësuese", "n"), ("nxënës", "n"), ("klasë", "n"),
    ("mësim", "n"), ("libër", "n"), ("fletore", "n"), ("laps", "n"), ("stilolaps", "n"),
    ("gomë", "n"), ("vizore", "n"), ("çantë", "n"), ("tabelë", "n"), ("shkumës", "n"),
    ("detyrë", "n"), ("provim", "n"), ("notë", "n"), ("fjalë", "n"), ("shkronjë", "n"),
    ("fjali", "n"), ("faqe", "n"), ("histori", "n"), ("përrallë", "n"), ("gjuhë", "n"),
    ("matematikë", "n"), ("ngjyrë", "n"), ("vizatim", "n"), ("lojë", "n"), ("pushim", "n"),
    ("oborr", "n"), ("bankë", "n"), ("karrige", "n"), ("tryezë", "n"), ("dërrasë", "n"),
    ("lexim", "n"), ("shkrim", "n"), ("pyetje", "n"), ("përgjigje", "n"), ("shembull", "n"),
    ("fjalor", "n"), ("radhë", "n"),

    # --- Tiere ---
    ("qen", "n"), ("mace", "n"), ("zog", "n"), ("peshk", "n"), ("kalë", "n"),
    ("lopë", "n"), ("dele", "n"), ("dhi", "n"), ("derr", "n"), ("pulë", "n"),
    ("gjel", "n"), ("rosë", "n"), ("mi", "n"), ("lepur", "n"), ("dhelpër", "n"),
    ("ujk", "n"), ("ari", "n"), ("luan", "n"), ("elefant", "n"), ("majmun", "n"),
    ("gjarpër", "n"), ("bretkosë", "n"), ("flutur", "n"), ("bletë", "n"), ("milingonë", "n"),
    ("mizë", "n"), ("merimangë", "n"), ("breshkë", "n"), ("kafshë", "n"), ("pëllumb", "n"),
    ("sorrë", "n"), ("shqiponjë", "n"), ("gomar", "n"), ("viç", "n"), ("qingj", "n"),
    ("këlysh", "n"), ("krimb", "n"), ("gaforre", "n"), ("balenë", "n"),

    # --- Essen / Trinken ---
    ("bukë", "n"), ("ujë", "n"), ("qumësht", "n"), ("djathë", "n"), ("gjalpë", "n"),
    ("vezë", "n"), ("mish", "n"), ("oriz", "n"), ("makarona", "n"), ("supë", "n"),
    ("sallatë", "n"), ("domate", "n"), ("kastravec", "n"), ("patate", "n"), ("qepë", "n"),
    ("karotë", "n"), ("lakër", "n"), ("fasule", "n"), ("mollë", "n"), ("dardhë", "n"),
    ("banane", "n"), ("portokall", "n"), ("limon", "n"), ("rrush", "n"), ("luleshtrydhe", "n"),
    ("qershi", "n"), ("pjeshkë", "n"), ("shalqi", "n"), ("sheqer", "n"), ("kripë", "n"),
    ("mjaltë", "n"), ("çaj", "n"), ("kafe", "n"), ("lëng", "n"), ("ëmbëlsirë", "n"),
    ("çokollatë", "n"), ("akullore", "n"), ("byrek", "n"), ("drekë", "n"), ("darkë", "n"),
    ("mëngjes", "n"), ("ushqim", "n"), ("vaj", "n"), ("miell", "n"), ("kek", "n"),

    # --- Koerper ---
    ("kokë", "n"), ("flokë", "n"), ("sy", "n"), ("vesh", "n"), ("hundë", "n"),
    ("gojë", "n"), ("dhëmb", "n"), ("buzë", "n"), ("fytyrë", "n"), ("qafë", "n"),
    ("krah", "n"), ("dorë", "n"), ("gisht", "n"), ("këmbë", "n"), ("gju", "n"),
    ("bark", "n"), ("shpinë", "n"), ("zemër", "n"), ("gjak", "n"), ("lëkurë", "n"),
    ("kockë", "n"), ("supe", "n"), ("thua", "n"), ("bërryl", "n"), ("trup", "n"),

    # --- Natur ---
    ("diell", "n"), ("hënë", "n"), ("yll", "n"), ("qiell", "n"), ("re", "n"),
    ("shi", "n"), ("borë", "n"), ("erë", "n"), ("stuhi", "n"), ("vetëtimë", "n"),
    ("bubullimë", "n"), ("ylber", "n"), ("det", "n"), ("liqen", "n"), ("lumë", "n"),
    ("përrua", "n"), ("mal", "n"), ("kodër", "n"), ("fushë", "n"), ("pyll", "n"),
    ("pemë", "n"), ("degë", "n"), ("gjethe", "n"), ("rrënjë", "n"), ("lule", "n"),
    ("bar", "n"), ("gur", "n"), ("rërë", "n"), ("tokë", "n"), ("zjarr", "n"),
    ("akull", "n"), ("hije", "n"), ("dritë", "n"), ("natyrë", "n"), ("ishull", "n"),
    ("valë", "n"), ("bimë", "n"), ("farë", "n"), ("frut", "n"), ("kopsht", "n"),
    ("ajër", "n"),

    # --- Zeit ---
    ("ditë", "n"), ("natë", "n"), ("mbrëmje", "n"), ("javë", "n"), ("muaj", "n"),
    ("vit", "n"), ("orë", "n"), ("minutë", "n"), ("sekondë", "n"), ("kohë", "n"),
    ("stinë", "n"), ("pranverë", "n"), ("verë", "n"), ("vjeshtë", "n"), ("dimër", "n"),
    ("moment", "n"), ("fillim", "n"), ("fund", "n"),

    # --- Haus / Gegenstaende ---
    ("shtëpi", "n"), ("dhomë", "n"), ("kuzhinë", "n"), ("banjë", "n"), ("derë", "n"),
    ("dritare", "n"), ("mur", "n"), ("çati", "n"), ("dysheme", "n"), ("shkallë", "n"),
    ("krevat", "n"), ("jastëk", "n"), ("batanije", "n"), ("dollap", "n"), ("pasqyrë", "n"),
    ("llambë", "n"), ("televizor", "n"), ("telefon", "n"), ("kompjuter", "n"), ("çelës", "n"),
    ("lugë", "n"), ("pirun", "n"), ("thikë", "n"), ("pjatë", "n"), ("gotë", "n"),
    ("filxhan", "n"), ("tenxhere", "n"), ("shishe", "n"), ("kuti", "n"), ("qese", "n"),
    ("letër", "n"), ("sapun", "n"), ("peshqir", "n"), ("furçë", "n"),

    # --- Kleidung ---
    ("rroba", "n"), ("këmishë", "n"), ("pantallona", "n"), ("fustan", "n"), ("xhaketë", "n"),
    ("pallto", "n"), ("çorape", "n"), ("këpucë", "n"), ("kapelë", "n"), ("shall", "n"),
    ("doreza", "n"), ("xhep", "n"), ("kopsë", "n"), ("bluzë", "n"),

    # --- Stadt / Verkehr / Berufe ---
    ("qytet", "n"), ("fshat", "n"), ("rrugë", "n"), ("shesh", "n"), ("urë", "n"),
    ("makinë", "n"), ("autobus", "n"), ("tren", "n"), ("aeroplan", "n"), ("anije", "n"),
    ("biçikletë", "n"), ("motor", "n"), ("dyqan", "n"), ("treg", "n"), ("spital", "n"),
    ("kishë", "n"), ("xhami", "n"), ("park", "n"), ("bibliotekë", "n"), ("muze", "n"),
    ("kinema", "n"), ("hotel", "n"), ("postë", "n"), ("punë", "n"), ("mjek", "n"),
    ("polic", "n"), ("zjarrfikës", "n"), ("shofer", "n"), ("kuzhinier", "n"), ("fermer", "n"),
    ("piktor", "n"), ("këngëtar", "n"), ("vend", "n"), ("botë", "n"), ("flamur", "n"),
    ("monedhë", "n"),

    # --- Spiel / Gefuehle / Abstrakt ---
    ("top", "n"), ("lodër", "n"), ("kukull", "n"), ("dhuratë", "n"), ("ditëlindje", "n"),
    ("festë", "n"), ("muzikë", "n"), ("këngë", "n"), ("film", "n"), ("fotografi", "n"),
    ("gëzim", "n"), ("frikë", "n"), ("dashuri", "n"), ("ëndërr", "n"), ("gjumë", "n"),
    ("shëndet", "n"), ("sëmundje", "n"), ("ilaç", "n"), ("ndihmë", "n"), ("rregull", "n"),
    ("problem", "n"), ("zgjidhje", "n"), ("ide", "n"), ("mendim", "n"), ("zë", "n"),
    ("herë", "n"),

    # --- Verben ---
    ("jam", "v"), ("kam", "v"), ("bëj", "v"), ("shkoj", "v"), ("vij", "v"),
    ("shoh", "v"), ("dëgjoj", "v"), ("flas", "v"), ("them", "v"), ("pyes", "v"),
    ("përgjigjem", "v"), ("lexoj", "v"), ("shkruaj", "v"), ("mësoj", "v"), ("di", "v"),
    ("mendoj", "v"), ("dua", "v"), ("mund", "v"), ("duhet", "v"), ("jap", "v"),
    ("marr", "v"), ("sjell", "v"), ("çoj", "v"), ("hap", "v"), ("mbyll", "v"),
    ("ha", "v"), ("pi", "v"), ("fle", "v"), ("zgjohem", "v"), ("ngrihem", "v"),
    ("ulem", "v"), ("rri", "v"), ("eci", "v"), ("vrapoj", "v"), ("kërcej", "v"),
    ("luaj", "v"), ("qesh", "v"), ("qaj", "v"), ("këndoj", "v"), ("vallëzoj", "v"),
    ("punoj", "v"), ("ndihmoj", "v"), ("blej", "v"), ("shes", "v"), ("laj", "v"),
    ("pastroj", "v"), ("gatuaj", "v"), ("pres", "v"), ("gjej", "v"), ("humbas", "v"),
    ("filloj", "v"), ("mbaroj", "v"), ("hyj", "v"), ("dal", "v"), ("kthehem", "v"),
    ("nisem", "v"), ("udhëtoj", "v"), ("fluturoj", "v"), ("notoj", "v"), ("ngjitem", "v"),
    ("bie", "v"), ("mbaj", "v"), ("lë", "v"), ("vendos", "v"), ("ndaj", "v"),
    ("mbledh", "v"), ("numëroj", "v"), ("vizatoj", "v"), ("ngjyros", "v"), ("prek", "v"),
    ("ndiej", "v"), ("dashuroj", "v"), ("shpresoj", "v"), ("besoj", "v"), ("kujtoj", "v"),
    ("harroj", "v"), ("kuptoj", "v"), ("tregoj", "v"), ("shpjegoj", "v"), ("dërgoj", "v"),
    ("pranoj", "v"), ("kërkoj", "v"), ("hedh", "v"), ("kap", "v"), ("tërheq", "v"),
    ("shtyj", "v"), ("ndal", "v"), ("vazhdoj", "v"), ("rritem", "v"), ("jetoj", "v"),
    ("lind", "v"), ("bëhem", "v"), ("dukem", "v"), ("shikoj", "v"), ("thërras", "v"),
    ("përshëndes", "v"), ("falënderoj", "v"), ("veshem", "v"), ("lodhem", "v"),

    # --- Adjektive (Grundform ohne Artikel) ---
    ("madh", "a"), ("vogël", "a"), ("bukur", "a"), ("shëmtuar", "a"), ("ri", "a"),
    ("vjetër", "a"), ("plak", "a"), ("gjerë", "a"), ("ngushtë", "a"), ("lartë", "a"),
    ("ulët", "a"), ("shkurtër", "a"), ("trashë", "a"), ("hollë", "a"), ("rëndë", "a"),
    ("lehtë", "a"), ("fortë", "a"), ("dobët", "a"), ("shpejtë", "a"), ("ngadaltë", "a"),
    ("nxehtë", "a"), ("ftohtë", "a"), ("ngrohtë", "a"), ("thatë", "a"), ("lagësht", "a"),
    ("pastër", "a"), ("ndotur", "a"), ("plotë", "a"), ("zbrazët", "a"), ("hapur", "a"),
    ("mbyllur", "a"), ("lumtur", "a"), ("trishtuar", "a"), ("zemëruar", "a"), ("qetë", "a"),
    ("zhurmshëm", "a"), ("urtë", "a"), ("zgjuar", "a"), ("trim", "a"), ("frikacak", "a"),
    ("bardhë", "a"), ("zi", "a"), ("kuq", "a"), ("verdhë", "a"), ("gjelbër", "a"),
    ("kaltër", "a"), ("blu", "a"), ("portokalli", "a"), ("rozë", "a"), ("gri", "a"),
    ("vjollcë", "a"), ("ëmbël", "a"), ("hidhur", "a"), ("kripur", "a"), ("shijshëm", "a"),
    ("gjallë", "a"), ("gëzuar", "a"), ("vështirë", "a"), ("thjeshtë", "a"), ("rëndësishëm", "a"),
    ("interesant", "a"), ("mërzitshëm", "a"), ("shtrenjtë", "a"), ("lirë", "a"), ("butë", "a"),
    ("ashpër", "a"), ("rrumbullakët", "a"), ("drejtë", "a"), ("shtrembër", "a"), ("sigurt", "a"),
    ("rrezikshëm", "a"), ("sëmurë", "a"), ("shëndetshëm", "a"), ("gjatë", "a"), ("mirëfilltë", "a"),
]
