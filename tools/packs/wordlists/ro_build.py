# -*- coding: utf-8 -*-
"""Trimmt ro_raw.py auf exakt 500 Woerter, silbentrennt mit pyphen, schreibt ro500.json."""
import json, sys, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ro_raw import WORDS

DROP = set("""
mele tăi tale său sa nostru noastră noștri vostru voastră cui altul alta acestea
acela aceea asta unii unele cel cea cei cele dintre către însă ori ci decât deci
altfel totuși adesea astăzi mâinile unsprezece doisprezece douăzeci sută
niciodată uneori înăuntru
munci visa mirosi picta construi repara curăța măsura împărți pescui planta uda
hrăni îngriji mângâia îmbrățișa săruta goli fierbe coace frige călători vizita
locui reuși câștiga explica sosi culege povesti saluta gusta atinge striga
dulceag blând acru amar strâmb bogat sărac iute important adevărat simplu ocupat
gălăgios luminos întunecat
văr bebeluș prietenă doamnă domn mătușă unchi vecin
elevă învățătoare stilou penar cretă foaie pagină propoziție poezie riglă
foarfecă lipici glob muzeu bibliotecă
canapea oglindă perdea acoperiș podea cuptor frigider furculiță oală prosop
săpun perie pieptene pătură saltea poartă gard
jachetă bluză nasture buzunar cizmă fular căciulă
castravete usturoi plăcintă prăjitură dulceață căpșună zmeură strugure pepene
lămâie alună biscuit covrig cozonac făină ciorbă cafea ceai tort salată ceapă
cerb veveriță arici barză bufniță corb porumbel rândunică vrabie păianjen gândac
labă blană pană girafă delfin gâscă capră
obraz bărbie unghie cot talpă burtă sânge os piele buză
ninsoare tunet ceață fum aer nisip deal pom rădăcină ramură sămânță baltă izvor
val insulă peșteră cărare
pod biserică vapor roată pompier brutar bucătar
clipă anotimp sărbătoare petrecere dans film fel parte lume putere vorbă adevăr
greșeală grijă drag dor minut somn
bancă dulap sticlă cutie coș ciorap prună pară oaie furtună
""".split())

known = {w for w, t in WORDS}
missing = DROP - known
if missing:
    sys.exit("DROP-Woerter nicht in Rohliste: %s" % sorted(missing))

kept = [(w, t) for w, t in WORDS if w not in DROP]
if len(kept) != 500:
    sys.exit("Nach Trim %d statt 500 (Delta %d)" % (len(kept), len(kept) - 500))

import pyphen
# left=1 erlaubt einbuchstabige Anfangssilben (a-pă, u-re-che) — fuers Lesetraining
# noetig, TeX-Patterns unterdruecken das sonst als Zeilenumbruch-Regel.
dic1 = pyphen.Pyphen(lang="ro_RO", left=1, right=2)
dic2 = pyphen.Pyphen(lang="ro_RO")

VOWELS = "aeiouăâî"


def ok(s, word):
    if s.replace("-", "") != word:
        return False
    return all(p and any(ch in VOWELS for ch in p.lower()) for p in s.split("-"))


# pyphen behandelt End-"i" als nichtsilbisch (korrekt bei Pluralen wie "lupi",
# falsch bei betonten Infinitiven) und kennt ein paar Woerter nicht.
OVERRIDE = {
    "lua": "lu-a", "scrie": "scri-e", "sări": "să-ri", "dormi": "dor-mi",
    "trezi": "tre-zi", "ieși": "ie-și", "simți": "sim-ți", "lipi": "li-pi",
    "trăi": "tră-i", "dori": "do-ri", "porni": "por-ni", "plăti": "plă-ti",
    "cuțit": "cu-țit", "morcov": "mor-cov", "pământ": "pă-mânt",
    "înalt": "î-nalt", "oferi": "o-fe-ri", "auzi": "a-u-zi",
    "mulțumi": "mul-țu-mi",
    # Diphthong nicht trennen
    "fereastră": "fe-reas-tră", "băiat": "bă-iat", "fiecare": "fie-ca-re",
    "prieten": "prie-ten", "pauză": "pau-ză", "bomboană": "bom-boa-nă",
    "miere": "mie-re", "cireașă": "ci-rea-șă", "fierbinte": "fier-bin-te",
    "ghiozdan": "ghioz-dan",
    # falsche Pattern-Treffer
    "elefant": "e-le-fant", "autobuz": "au-to-buz", "rotund": "ro-tund",
    "săptămână": "săp-tă-mâ-nă", "păpușă": "pă-pu-șă",
    # Endung -ie nach Konsonant = Hiat (DOOM: fa-mi-li-e)
    "familie": "fa-mi-li-e", "rochie": "ro-chi-e", "hârtie": "hâr-ti-e",
    "bucurie": "bu-cu-ri-e", "farfurie": "far-fu-ri-e",
    "jucărie": "ju-că-ri-e", "bucătărie": "bu-că-tă-ri-e",
    "lecție": "lec-ți-e", "roșie": "ro-și-e",
}


def syllabify(word):
    if word in OVERRIDE:
        s = OVERRIDE[word]
        assert ok(s, word), s
        return s
    for d in (dic1, dic2):
        s = d.inserted(word, hyphen="-")
        if "-" not in s:
            continue
        if ok(s, word):
            return s
    return word


out = []
for w, t in kept:
    out.append([syllabify(w), t])

data = {
    "id": "ro500",
    "language": "ro",
    "nameDE": "Grundwortschatz Rumänisch",
    "nameEN": "Romanian basic vocabulary",
    "words": out,
}

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ro500.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

# --- Validierung ---
with open(path, encoding="utf-8") as f:
    chk = json.load(f)
ws = chk["words"]
assert len(ws) == 500, len(ws)
plain = [w.replace("-", "") for w, t in ws]
dups = [k for k, v in collections.Counter(plain).items() if v > 1]
assert not dups, dups
orig = [w for w, t in kept]
assert plain == orig, [ (a,b) for a,b in zip(plain,orig) if a!=b ][:5]
assert all(t in {"n", "v", "a", "o"} for w, t in ws)
assert all("ş" not in w and "ţ" not in w for w, t in ws), "Cedille statt Komma-Diakritik!"
hyph = sum(1 for w, t in ws if "-" in w)
cnt = collections.Counter(t for w, t in ws)
print("OK ro 500 Wörter, %d mit Silbentrennung, n=%d v=%d a=%d o=%d"
      % (hyph, cnt["n"], cnt["v"], cnt["a"], cnt["o"]))
