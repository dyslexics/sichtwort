# -*- coding: utf-8 -*-
"""Baut sq500.json aus sq_raw.py: kuerzt auf 500, silbentrennt, validiert.

Silbentrennung: eigene albanische Regeln. pyphen ("sq"/"sq_AL") ist unbrauchbar,
es liefert konsonantische Pseudo-Silben ("pa-s-t-roj", "hu-n-dë").
"""
import json, collections, sys
import sq_raw

DROP = {
    # Funktionswoerter / Zahlen (Dubletten oder zu selten fuer Erstlesen)
    "sërish", "mbase", "patjetër", "gjithashtu", "midis", "përveç", "sipas",
    "njëmbëdhjetë", "dymbëdhjetë", "pesëdhjetë",
    # Verben
    "falënderoj", "përshëndes", "dashuroj", "humbas",
    # Adjektive
    "mirëfilltë",
    # Nomen
    "shifër", "mbiemër", "stilolaps", "vizore", "shkumës", "provim", "notë",
    "tryezë", "dërrasë", "shembull", "fjalor", "radhë", "gjel", "rosë",
    "dhelpër", "elefant", "majmun", "gjarpër", "bretkosë", "milingonë",
    "merimangë", "breshkë", "pëllumb", "sorrë", "shqiponjë", "gomar", "viç",
    "qingj", "këlysh", "krimb", "gaforre", "balenë", "makarona", "sallatë",
    "kastravec", "karotë", "lakër", "fasule", "dardhë", "banane", "limon",
    "rrush", "luleshtrydhe", "qershi", "pjeshkë", "shalqi", "mjaltë",
    "ëmbëlsirë", "byrek", "miell", "kek", "bërryl", "thua", "supe", "kockë",
    "lëkurë", "stuhi", "vetëtimë", "bubullimë", "ylber", "liqen", "përrua",
    "kodër", "rërë", "ishull", "valë", "bimë", "farë", "frut", "ajër",
    "sekondë", "stinë", "moment", "dysheme", "jastëk", "batanije", "dollap",
    "pasqyrë", "llambë", "televizor", "kompjuter", "filxhan", "tenxhere",
    "qese", "peshqir", "furçë", "pallto", "doreza", "kopsë", "bluzë", "shall",
    "xhep", "shesh", "urë", "aeroplan", "anije", "motor", "treg", "xhami",
    "bibliotekë", "muze", "kinema", "hotel", "postë", "zjarrfikës", "shofer",
    "kuzhinier", "fermer", "piktor", "këngëtar", "monedhë", "flamur",
    "fotografi", "ditëlindje", "ilaç", "rregull", "problem", "zgjidhje",
    "ide", "mendim", "sëmundje", "teze", "hallë", "kushëri", "dajë",
    "xhaxha", "foshnjë", "fqinj", "moshë", "histori", "lexim", "shkrim",
    "vizatim", "hije", "shpinë",
}

# ---------------- Silbentrennung: albanische Regeln ----------------
DIGRAPHS = ("dh", "gj", "ll", "nj", "rr", "sh", "th", "xh", "zh")
VOWELS = set("aeiouyë")
# Erlaubte Anlautgruppen (Verschluss-/Reibelaut + Liquid) bleiben zusammen.
ONSET2 = {c + l for c in "bdfgkptv" for l in "rl"}

# Hand-Ausnahmen: Hiatus (zwei Vokale = zwei Silben) bzw. Morphemgrenzen,
# die eine rein phonotaktische Regel nicht treffen kann.
MANUAL = {
    "gjithçka": "gjith-çka",
    "diell": "di-ell",
    "qiell": "qi-ell",
    "luan": "lu-an",
    "pyetje": "py-e-tje",
    "pyes": "py-es",
    "mësues": "më-su-es",
    "mësuese": "më-su-e-se",
}


def units(word):
    """Wort in Buchstabeneinheiten zerlegen; Digraphen zaehlen als EIN Zeichen."""
    out, i = [], 0
    while i < len(word):
        if word[i:i + 2] in DIGRAPHS:
            out.append(word[i:i + 2])
            i += 2
        else:
            out.append(word[i])
            i += 1
    return out


def syllabify(word):
    if word in MANUAL:
        return MANUAL[word]
    u = units(word)
    nuclei = [i for i, c in enumerate(u) if c in VOWELS]
    if len(nuclei) < 2:
        return word
    cuts = []
    for a, b in zip(nuclei, nuclei[1:]):
        k = b - a - 1                      # Konsonanteneinheiten dazwischen
        if k == 0:
            continue                       # Vokalfolge: nie trennen (Diphthong/Hiatus)
        if k == 1:
            cuts.append(a + 1)             # V-CV
        elif k == 2:
            onset = "".join(u[a + 1:b])
            cuts.append(a + 1 if onset in ONSET2 else a + 2)
        else:
            onset2 = "".join(u[b - 2:b])
            cuts.append(b - 2 if onset2 in ONSET2 else b - 1)
    if not cuts:
        return word
    parts, prev = [], 0
    for c in sorted(set(cuts)):
        parts.append("".join(u[prev:c]))
        prev = c
    parts.append("".join(u[prev:]))
    return "-".join(parts)


def digraph_ok(hy):
    for i, ch in enumerate(hy):
        if ch == "-" and (hy[i - 1:i] + hy[i + 1:i + 2]) in DIGRAPHS:
            return False
    return True


# ---------------- Bauen ----------------
unknown = DROP - {w for w, _ in sq_raw.WORDS}
if unknown:
    sys.exit("DROP enthaelt unbekannte Woerter: %s" % sorted(unknown))
words = [(w, t) for w, t in sq_raw.WORDS if w not in DROP]
out = [[syllabify(w), t] for w, t in words]

# ---------------- Validierung ----------------
assert len(out) == 500, "nicht 500, sondern %d" % len(out)
plain = [w.replace("-", "") for w, _ in out]
dups = [k for k, v in collections.Counter(plain).items() if v > 1]
assert not dups, "Duplikate: %s" % dups
for (hy, t), (orig, ot) in zip(out, words):
    assert hy.replace("-", "") == orig, "Trennung veraendert Wort: %s -> %s" % (orig, hy)
    assert t == ot and t in ("n", "v", "a", "o")
    assert digraph_ok(hy), "Digraph getrennt: %s" % hy
    assert " " not in hy and "'" not in hy, "kein Einzelwort: %s" % hy
    assert all(any(c in VOWELS for c in p) for p in hy.split("-")), "Silbe ohne Vokal: %s" % hy

data = {
    "id": "sq500",
    "language": "sq",
    "nameDE": "Grundwortschatz Albanisch",
    "nameEN": "Albanian basic vocabulary",
    "words": out,
}
path = "/home/mario/sichtwort/tools/packs/wordlists/sq500.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

with open(path, encoding="utf-8") as f:
    chk = json.load(f)
assert len(chk["words"]) == 500
assert all(len(x) == 2 and x[1] in ("n", "v", "a", "o") for x in chk["words"])
assert len({x[0].replace("-", "") for x in chk["words"]}) == 500

cnt = collections.Counter(t for _, t in chk["words"])
hyc = sum(1 for w, _ in chk["words"] if "-" in w)
print("OK sq 500 Woerter, %d mit Silbentrennung, n=%d v=%d a=%d o=%d"
      % (hyc, cnt["n"], cnt["v"], cnt["a"], cnt["o"]))
print("Stichprobe:", [w for w, _ in chk["words"][::29]])
print("mehrsilbig ungetrennt:", [w for w, _ in chk["words"]
                                 if "-" not in w and sum(1 for c in w if c in VOWELS) > 1])
