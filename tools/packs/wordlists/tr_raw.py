# -*- coding: utf-8 -*-
"""Grundwortschatz Türkisch für Sichtwort (Blitzlesen, 6-10 Jahre).
Rohliste: (Wort, Wortart) mit n=Nomen, v=Verb, a=Adjektiv, o=Sonstiges.
Verben stehen im Infinitiv (-mek/-mak). Reihenfolge = Priorität;
der Generator schneidet am Ende auf exakt 500 Einträge zu.
"""

POOL = [
    # --- Pronomen, Frage- und Funktionswörter -------------------------------
    ("ben", "o"), ("sen", "o"), ("o", "o"), ("biz", "o"), ("siz", "o"),
    ("onlar", "o"), ("bu", "o"), ("şu", "o"), ("kendi", "o"), ("kim", "o"),
    ("ne", "o"), ("nerede", "o"), ("nereye", "o"), ("neden", "o"),
    ("nasıl", "o"), ("hangi", "o"), ("kaç", "o"), ("ne zaman", None),
    ("ve", "o"), ("ile", "o"), ("ama", "o"), ("fakat", "o"), ("çünkü", "o"),
    ("veya", "o"), ("ya", "o"), ("eğer", "o"), ("gibi", "o"), ("için", "o"),
    ("kadar", "o"), ("göre", "o"), ("karşı", "o"), ("sonra", "o"),
    ("önce", "o"), ("şimdi", "o"), ("hemen", "o"), ("artık", "o"),
    ("daha", "o"), ("çok", "o"), ("az", "o"), ("hep", "o"), ("hiç", "o"),
    ("bazen", "o"), ("her", "o"), ("bazı", "o"), ("tüm", "o"),
    ("hepsi", "o"), ("birkaç", "o"), ("biraz", "o"), ("evet", "o"),
    ("hayır", "o"), ("tamam", "o"), ("belki", "o"), ("elbette", "o"),
    ("işte", "o"), ("yine", "o"), ("yeniden", "o"), ("henüz", "o"),
    ("birlikte", "o"), ("beraber", "o"), ("yalnız", "o"), ("ancak", "o"),
    ("sadece", "o"), ("bile", "o"), ("herkes", "o"), ("hiçbir", "o"),
    ("burada", "o"), ("orada", "o"), ("içeri", "o"), ("dışarı", "o"),
    ("yukarı", "o"), ("aşağı", "o"), ("ileri", "o"), ("geri", "o"),
    ("sağ", "o"), ("sol", "o"), ("altında", None), ("merhaba", "o"),
    ("günaydın", "o"), ("teşekkür", "n"), ("lütfen", "o"),
    ("hoşça", None), ("selam", "o"),

    # --- Zahlen --------------------------------------------------------------
    ("bir", "o"), ("iki", "o"), ("üç", "o"), ("dört", "o"), ("beş", "o"),
    ("altı", "o"), ("yedi", "o"), ("sekiz", "o"), ("dokuz", "o"), ("on", "o"),
    ("yirmi", "o"), ("otuz", "o"), ("kırk", "o"), ("elli", "o"),
    ("altmış", "o"), ("yetmiş", "o"), ("seksen", "o"), ("doksan", "o"),
    ("yüz", "o"), ("bin", "o"), ("milyon", "o"), ("birinci", "o"),
    ("ikinci", "o"), ("üçüncü", "o"), ("sıfır", "o"),

    # --- Zeit ----------------------------------------------------------------
    ("gün", "n"), ("hafta", "n"), ("ay", "n"), ("yıl", "n"), ("saat", "n"),
    ("dakika", "n"), ("saniye", "n"), ("sabah", "n"), ("öğle", "n"),
    ("akşam", "n"), ("gece", "n"), ("bugün", "o"), ("yarın", "o"),
    ("dün", "o"), ("pazartesi", "n"), ("salı", "n"), ("çarşamba", "n"),
    ("perşembe", "n"), ("cuma", "n"), ("cumartesi", "n"), ("pazar", "n"),
    ("mevsim", "n"), ("ilkbahar", "n"), ("yaz", "n"), ("sonbahar", "n"),
    ("kış", "n"), ("zaman", "n"), ("tatil", "n"), ("doğum", "n"),
    ("bayram", "n"),

    # --- Familie und Menschen -------------------------------------------------
    ("anne", "n"), ("baba", "n"), ("kardeş", "n"), ("abla", "n"),
    ("ağabey", "n"), ("dede", "n"), ("nine", "n"), ("teyze", "n"),
    ("hala", "n"), ("amca", "n"), ("dayı", "n"), ("oğul", "n"), ("kız", "n"),
    ("çocuk", "n"), ("bebek", "n"), ("aile", "n"), ("torun", "n"),
    ("akraba", "n"), ("insan", "n"), ("kişi", "n"), ("adam", "n"),
    ("kadın", "n"), ("erkek", "n"), ("arkadaş", "n"), ("komşu", "n"),
    ("misafir", "n"), ("isim", "n"),

    # --- Schule ---------------------------------------------------------------
    ("okul", "n"), ("sınıf", "n"), ("öğretmen", "n"), ("öğrenci", "n"),
    ("ders", "n"), ("kitap", "n"), ("defter", "n"), ("kalem", "n"),
    ("silgi", "n"), ("cetvel", "n"), ("çanta", "n"), ("tahta", "n"),
    ("sıra", "n"), ("harf", "n"), ("kelime", "n"), ("cümle", "n"),
    ("sayı", "n"), ("soru", "n"), ("cevap", "n"), ("ödev", "n"),
    ("sınav", "n"), ("resim", "n"), ("boya", "n"), ("makas", "n"),
    ("zil", "n"), ("teneffüs", "n"), ("kütüphane", "n"), ("müdür", "n"),
    ("sayfa", "n"), ("kağıt", "n"), ("kutu", "n"), ("masa", "n"),
    ("sandalye", "n"), ("çizgi", "n"), ("nokta", "n"), ("hikaye", "n"),
    ("masal", "n"), ("şiir", "n"), ("kalemtıraş", "n"), ("okuma", "n"),

    # --- Haus und Wohnen ------------------------------------------------------
    ("ev", "n"), ("oda", "n"), ("mutfak", "n"), ("banyo", "n"),
    ("salon", "n"), ("yatak", "n"), ("kapı", "n"), ("pencere", "n"),
    ("duvar", "n"), ("çatı", "n"), ("merdiven", "n"), ("bahçe", "n"),
    ("balkon", "n"), ("halı", "n"), ("perde", "n"), ("dolap", "n"),
    ("koltuk", "n"), ("lamba", "n"), ("ayna", "n"), ("televizyon", "n"),
    ("telefon", "n"), ("bilgisayar", "n"), ("buzdolabı", "n"), ("soba", "n"),
    ("anahtar", "n"), ("sabun", "n"), ("havlu", "n"), ("yastık", "n"),
    ("battaniye", "n"), ("çamaşır", "n"), ("süpürge", "n"), ("bardak", "n"),
    ("tabak", "n"), ("çatal", "n"), ("kaşık", "n"), ("bıçak", "n"),
    ("tencere", "n"), ("şişe", "n"), ("fincan", "n"), ("sepet", "n"),
    ("ütü", "n"), ("raf", "n"),

    # --- Kleidung -------------------------------------------------------------
    ("elbise", "n"), ("gömlek", "n"), ("pantolon", "n"), ("etek", "n"),
    ("ceket", "n"), ("mont", "n"), ("kazak", "n"), ("çorap", "n"),
    ("ayakkabı", "n"), ("terlik", "n"), ("şapka", "n"), ("eldiven", "n"),
    ("atkı", "n"), ("kemer", "n"), ("düğme", "n"),

    # --- Essen und Trinken ----------------------------------------------------
    ("ekmek", "n"), ("su", "n"), ("süt", "n"), ("peynir", "n"),
    ("yumurta", "n"), ("et", "n"), ("balık", "n"), ("tavuk", "n"),
    ("pilav", "n"), ("çorba", "n"), ("makarna", "n"), ("patates", "n"),
    ("domates", "n"), ("salatalık", "n"), ("soğan", "n"), ("sarımsak", "n"),
    ("havuç", "n"), ("biber", "n"), ("marul", "n"), ("elma", "n"),
    ("armut", "n"), ("muz", "n"), ("portakal", "n"), ("üzüm", "n"),
    ("çilek", "n"), ("karpuz", "n"), ("kavun", "n"), ("kiraz", "n"),
    ("şeftali", "n"), ("limon", "n"), ("ceviz", "n"), ("fındık", "n"),
    ("badem", "n"), ("şeker", "n"), ("tuz", "n"), ("yağ", "n"), ("bal", "n"),
    ("reçel", "n"), ("çay", "n"), ("kahve", "n"), ("meyve", "n"),
    ("sebze", "n"), ("dondurma", "n"), ("kek", "n"), ("pasta", "n"),
    ("bisküvi", "n"), ("çikolata", "n"), ("yemek", "n"), ("kahvaltı", "n"),
    ("un", "n"), ("pirinç", "n"), ("zeytin", "n"), ("tereyağı", "n"),

    # --- Tiere ----------------------------------------------------------------
    ("kedi", "n"), ("köpek", "n"), ("kuş", "n"), ("at", "n"), ("inek", "n"),
    ("koyun", "n"), ("keçi", "n"), ("tavşan", "n"), ("fare", "n"),
    ("aslan", "n"), ("kaplan", "n"), ("ayı", "n"), ("fil", "n"),
    ("maymun", "n"), ("zürafa", "n"), ("kurt", "n"), ("tilki", "n"),
    ("karınca", "n"), ("arı", "n"), ("kelebek", "n"), ("böcek", "n"),
    ("örümcek", "n"), ("yılan", "n"), ("kaplumbağa", "n"), ("kurbağa", "n"),
    ("ördek", "n"), ("kaz", "n"), ("horoz", "n"), ("civciv", "n"),
    ("hayvan", "n"), ("kuzu", "n"), ("deve", "n"), ("eşek", "n"),
    ("geyik", "n"), ("sincap", "n"), ("baykuş", "n"), ("martı", "n"),
    ("güvercin", "n"), ("papağan", "n"), ("yunus", "n"), ("yengeç", "n"),
    ("kanat", "n"), ("tüy", "n"), ("yuva", "n"),

    # --- Körper ---------------------------------------------------------------
    ("baş", "n"), ("saç", "n"), ("göz", "n"), ("kulak", "n"), ("burun", "n"),
    ("ağız", "n"), ("diş", "n"), ("dil", "n"), ("dudak", "n"), ("yanak", "n"),
    ("alın", "n"), ("boyun", "n"), ("omuz", "n"), ("kol", "n"), ("el", "n"),
    ("parmak", "n"), ("tırnak", "n"), ("göğüs", "n"), ("karın", "n"),
    ("sırt", "n"), ("bacak", "n"), ("ayak", "n"), ("diz", "n"),
    ("kalp", "n"), ("kemik", "n"), ("deri", "n"), ("vücut", "n"),
    ("kan", "n"), ("ses", "n"),

    # --- Natur ----------------------------------------------------------------
    ("güneş", "n"), ("yıldız", "n"), ("gökyüzü", "n"), ("bulut", "n"),
    ("yağmur", "n"), ("kar", "n"), ("rüzgar", "n"), ("fırtına", "n"),
    ("gökkuşağı", "n"), ("deniz", "n"), ("göl", "n"), ("nehir", "n"),
    ("dere", "n"), ("dağ", "n"), ("tepe", "n"), ("orman", "n"),
    ("ağaç", "n"), ("yaprak", "n"), ("dal", "n"), ("kök", "n"),
    ("çiçek", "n"), ("gül", "n"), ("papatya", "n"), ("çimen", "n"),
    ("ot", "n"), ("taş", "n"), ("toprak", "n"), ("kum", "n"), ("ateş", "n"),
    ("buz", "n"), ("hava", "n"), ("dünya", "n"), ("doğa", "n"),
    ("gölge", "n"), ("ışık", "n"), ("tohum", "n"), ("meyveli", None),

    # --- Ort und Verkehr -------------------------------------------------------
    ("köy", "n"), ("şehir", "n"), ("sokak", "n"), ("yol", "n"),
    ("köprü", "n"), ("park", "n"), ("meydan", "n"), ("araba", "n"),
    ("otobüs", "n"), ("tren", "n"), ("uçak", "n"), ("gemi", "n"),
    ("bisiklet", "n"), ("kamyon", "n"), ("traktör", "n"), ("tekne", "n"),
    ("istasyon", "n"), ("market", "n"), ("mağaza", "n"), ("hastane", "n"),
    ("fırın", "n"), ("bakkal", "n"), ("eczane", "n"), ("banka", "n"),
    ("otel", "n"), ("lokanta", "n"), ("sinema", "n"), ("müze", "n"),
    ("cami", "n"), ("bina", "n"), ("kat", "n"), ("asansör", "n"),

    # --- Berufe ----------------------------------------------------------------
    ("doktor", "n"), ("hemşire", "n"), ("polis", "n"), ("itfaiyeci", "n"),
    ("postacı", "n"), ("aşçı", "n"), ("şoför", "n"), ("çiftçi", "n"),
    ("ressam", "n"), ("terzi", "n"), ("berber", "n"), ("asker", "n"),

    # --- Spiel, Sport, Gefühl ---------------------------------------------------
    ("top", "n"), ("oyun", "n"), ("oyuncak", "n"), ("müzik", "n"),
    ("şarkı", "n"), ("dans", "n"), ("film", "n"), ("renk", "n"),
    ("para", "n"), ("iş", "n"), ("yer", "n"), ("şey", "n"), ("hayat", "n"),
    ("sevgi", "n"), ("mutluluk", "n"), ("korku", "n"), ("rüya", "n"),
    ("kahraman", "n"), ("futbol", "n"), ("basketbol", "n"), ("spor", "n"),
    ("bayrak", "n"), ("balon", "n"), ("hediye", "n"), ("davul", "n"),
    ("flüt", "n"), ("puzzle", None), ("uçurtma", "n"), ("salıncak", "n"),
    ("kaydırak", "n"),

    # --- Farben ------------------------------------------------------------------
    ("kırmızı", "a"), ("mavi", "a"), ("sarı", "a"), ("yeşil", "a"),
    ("siyah", "a"), ("beyaz", "a"), ("turuncu", "a"), ("mor", "a"),
    ("pembe", "a"), ("kahverengi", "a"), ("gri", "a"), ("renkli", "a"),

    # --- Adjektive ----------------------------------------------------------------
    ("büyük", "a"), ("küçük", "a"), ("uzun", "a"), ("kısa", "a"),
    ("yeni", "a"), ("eski", "a"), ("iyi", "a"), ("kötü", "a"),
    ("güzel", "a"), ("çirkin", "a"), ("temiz", "a"), ("kirli", "a"),
    ("sıcak", "a"), ("soğuk", "a"), ("ılık", "a"), ("hızlı", "a"),
    ("yavaş", "a"), ("kolay", "a"), ("zor", "a"), ("mutlu", "a"),
    ("üzgün", "a"), ("yorgun", "a"), ("aç", "a"), ("tok", "a"),
    ("hasta", "a"), ("sağlıklı", "a"), ("güçlü", "a"), ("zayıf", "a"),
    ("kalın", "a"), ("ince", "a"), ("ağır", "a"), ("hafif", "a"),
    ("dolu", "a"), ("boş", "a"), ("açık", "a"), ("kapalı", "a"),
    ("doğru", "a"), ("yanlış", "a"), ("zengin", "a"), ("fakir", "a"),
    ("genç", "a"), ("yaşlı", "a"), ("tatlı", "a"), ("acı", "a"),
    ("tuzlu", "a"), ("ekşi", "a"), ("yumuşak", "a"), ("sert", "a"),
    ("derin", "a"), ("geniş", "a"), ("dar", "a"), ("yüksek", "a"),
    ("alçak", "a"), ("parlak", "a"), ("karanlık", "a"), ("aydınlık", "a"),
    ("sessiz", "a"), ("gürültülü", "a"), ("komik", "a"), ("korkunç", "a"),
    ("önemli", "a"), ("tembel", "a"), ("çalışkan", "a"), ("cesur", "a"),
    ("kibar", "a"), ("neşeli", "a"), ("sevimli", "a"), ("islak", "a"),
    ("kuru", "a"), ("taze", "a"), ("yuvarlak", "a"), ("düz", "a"),
    ("keskin", "a"), ("uzak", "a"), ("yakın", "a"),

    # --- Verben ---------------------------------------------------------------------
    ("olmak", "v"), ("yapmak", "v"), ("etmek", "v"), ("gelmek", "v"),
    ("gitmek", "v"), ("görmek", "v"), ("bakmak", "v"), ("bilmek", "v"),
    ("vermek", "v"), ("almak", "v"), ("demek", "v"), ("söylemek", "v"),
    ("konuşmak", "v"), ("anlamak", "v"), ("dinlemek", "v"), ("duymak", "v"),
    ("okumak", "v"), ("yazmak", "v"), ("çizmek", "v"), ("oynamak", "v"),
    ("koşmak", "v"), ("yürümek", "v"), ("atlamak", "v"), ("uçmak", "v"),
    ("yüzmek", "v"), ("oturmak", "v"), ("kalkmak", "v"), ("durmak", "v"),
    ("uyumak", "v"), ("uyanmak", "v"), ("içmek", "v"), ("pişirmek", "v"),
    ("açmak", "v"), ("kapatmak", "v"), ("sevmek", "v"), ("gülmek", "v"),
    ("ağlamak", "v"), ("bağırmak", "v"), ("sormak", "v"), ("öğrenmek", "v"),
    ("öğretmek", "v"), ("çalışmak", "v"), ("dinlenmek", "v"),
    ("beklemek", "v"), ("bulmak", "v"), ("aramak", "v"), ("kaybetmek", "v"),
    ("kazanmak", "v"), ("başlamak", "v"), ("bitirmek", "v"),
    ("düşünmek", "v"), ("istemek", "v"), ("sevinmek", "v"), ("korkmak", "v"),
    ("kızmak", "v"), ("taşımak", "v"), ("tutmak", "v"), ("bırakmak", "v"),
    ("koymak", "v"), ("çekmek", "v"), ("itmek", "v"), ("kesmek", "v"),
    ("yapıştırmak", "v"), ("boyamak", "v"), ("temizlemek", "v"),
    ("yıkamak", "v"), ("giymek", "v"), ("çıkarmak", "v"), ("gezmek", "v"),
    ("binmek", "v"), ("inmek", "v"), ("düşmek", "v"), ("kalmak", "v"),
    ("dönmek", "v"), ("girmek", "v"), ("çıkmak", "v"), ("göstermek", "v"),
    ("saymak", "v"), ("ölçmek", "v"), ("seçmek", "v"), ("toplamak", "v"),
    ("paylaşmak", "v"), ("hatırlamak", "v"), ("unutmak", "v"),
    ("satmak", "v"), ("ödemek", "v"), ("kurmak", "v"), ("kırmak", "v"),
    ("büyümek", "v"), ("yaşamak", "v"), ("doğmak", "v"), ("susmak", "v"),
    ("gülümsemek", "v"), ("selamlamak", "v"), ("sarılmak", "v"),
    ("öpmek", "v"), ("vurmak", "v"), ("fırlatmak", "v"), ("yakalamak", "v"),
    ("saklamak", "v"), ("aramak2", None), ("çağırmak", "v"),
    ("anlatmak", "v"), ("sürmek", "v"), ("uçurmak", "v"), ("dokunmak", "v"),
    ("koklamak", "v"), ("tatmak", "v"), ("beslemek", "v"), ("sulamak", "v"),
    ("dikmek", "v"), ("örmek", "v"), ("katlamak", "v"), ("açıklamak", "v"),
    ("yardım etmek", None), ("ısırmak", "v"), ("titremek", "v"),
    ("zıplamak", "v"), ("tırmanmak", "v"), ("kaymak", "v"), ("uzanmak", "v"),
    ("kaldırmak", "v"), ("indirmek", "v"), ("doldurmak", "v"),
    ("boşaltmak", "v"), ("karıştırmak", "v"), ("ayırmak", "v"),
    ("bağlamak", "v"), ("çözmek", "v"), ("denemek", "v"), ("başarmak", "v"),
]

# Der Pool ist bewusst größer als 500. DROP enthält die aussortierten,
# selteneren bzw. für Erstleser weniger wichtigen Einträge, damit die
# Auswahl nachvollziehbar bleibt. WORDS = Pool - DROP = exakt 500.
DROP = frozenset("""
nereye elbette yeniden henüz beraber hiçbir selam işte ya bazı tüm
milyon birinci ikinci üçüncü
saniye mevsim doğum bayram
ağabey nine akraba misafir torun
cetvel sınav müdür teneffüs kalemtıraş şiir okuma çizgi
salon balkon perde ayna soba süpürge fincan sepet ütü raf battaniye
çamaşır tencere halı
mont kazak terlik eldiven atkı kemer düğme
pilav marul salatalık sarımsak şeftali ceviz badem fındık reçel bisküvi
pasta un pirinç tereyağı zeytin kavun
zürafa civciv deve geyik sincap baykuş martı güvercin yunus yengeç kanat
tüy yuva kaz
yanak alın omuz göğüs sırt kemik deri vücut kan
fırtına dere papatya çimen tohum gölge ışık kök doğa
traktör tekne istasyon mağaza bakkal eczane banka otel lokanta müze cami
bina kat asansör kamyon meydan
itfaiyeci postacı aşçı şoför terzi berber asker ressam
dans kahraman basketbol bayrak davul flüt uçurtma salıncak kaydırak rüya
mutluluk hediye
renkli
ılık zengin fakir ekşi tuzlu alçak aydınlık gürültülü korkunç önemli
tembel çalışkan cesur kibar neşeli sevimli islak taze yuvarlak düz
keskin çirkin sağlıklı zayıf parlak dar
sevinmek dinlenmek kaybetmek ölçmek paylaşmak ödemek kurmak doğmak
susmak gülümsemek selamlamak sarılmak öpmek fırlatmak saklamak çağırmak
sürmek uçurmak koklamak tatmak beslemek sulamak dikmek örmek katlamak
açıklamak ısırmak titremek zıplamak tırmanmak kaymak uzanmak boşaltmak
karıştırmak ayırmak bağlamak çözmek denemek başarmak indirmek
taşımak itmek gezmek satmak kırmak
""".split())

WORDS = [(w, t) for w, t in POOL
         if t is not None and " " not in w and w not in DROP]
