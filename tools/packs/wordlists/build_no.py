# -*- coding: utf-8 -*-
"""Baut no500.json aus no_raw.py (Silbentrennung via pyphen nb + Overrides).

Das nb-Wörterbuch von pyphen folgt typografischen Trennregeln und trennt
kurze Wörter (<=4 Zeichen) grundsätzlich nicht. Für das Blitzlese-Training
brauchen wir echte Sprechsilben, daher die OVERRIDES-Tabelle.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pyphen  # noqa: E402
from no_raw import WORDS  # noqa: E402

OVERRIDES = {
    # von pyphen gar nicht getrennt (zu kurz für typografische Regeln)
    "dere": "de-re", "mine": "mi-ne", "dine": "di-ne", "våre": "vå-re",
    "sine": "si-ne", "også": "og-så", "ikke": "ik-ke", "uten": "u-ten",
    "over": "o-ver", "etter": "et-ter", "ute": "u-te", "oppe": "op-pe",
    "nede": "ne-de", "borte": "bor-te", "igjen": "i-gjen", "ofte": "of-te",
    "alle": "al-le", "noen": "no-en", "bare": "ba-re", "enda": "en-da",
    "mye": "my-e", "fire": "fi-re", "åtte": "åt-te", "tjue": "tju-e",
    "være": "væ-re", "løpe": "lø-pe", "lese": "le-se", "male": "ma-le",
    "lære": "læ-re", "vite": "vi-te", "høre": "hø-re", "rope": "ro-pe",
    "sove": "so-ve", "bade": "ba-de", "leke": "le-ke", "dele": "de-le",
    "åpne": "åp-ne", "bære": "bæ-re", "like": "li-ke", "håpe": "hå-pe",
    "lage": "la-ge", "bake": "ba-ke", "koke": "ko-ke", "møte": "mø-te",
    "føle": "fø-le", "vise": "vi-se", "vokse": "vok-se", "åpen": "å-pen",
    "rosa": "ro-sa", "baby": "ba-by", "hode": "ho-de", "øye": "ø-ye",
    "øre": "ø-re", "nese": "ne-se", "elev": "e-lev", "stue": "stu-e",
    "hage": "ha-ge", "kake": "ka-ke", "eple": "ep-le", "løve": "lø-ve",
    "ape": "a-pe", "måne": "må-ne", "uke": "u-ke", "gave": "ga-ve",
    "lue": "lu-e", "lege": "le-ge",
    # von pyphen unvollständig/typografisch getrennt
    "alene": "a-le-ne", "oransje": "o-ran-sje", "elleve": "el-le-ve",
    "familie": "fa-mi-lie", "sommerfugl": "som-mer-fugl",
    "sjokolade": "sjo-ko-la-de", "elefant": "e-le-fant",
    "eventyr": "e-ven-tyr", "telefon": "te-le-fon", "prinsesse": "prin-ses-se",
    "bestemor": "bes-te-mor", "bestefar": "bes-te-far",
}

dic = pyphen.Pyphen(lang="nb")

out = []
hyph = 0
for word, typ in WORDS:
    h = OVERRIDES.get(word) or dic.inserted(word, hyphen="-")
    if h.replace("-", "") != word:
        h = word  # im Zweifel ungetrennt
    if "-" in h:
        hyph += 1
    out.append([h, typ])

data = {
    "id": "no500",
    "language": "no",
    "nameDE": "Grundwortschatz Norwegisch",
    "nameEN": "Norwegian basic vocabulary",
    "words": out,
}

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "no500.json")
rows = ",\n  ".join(json.dumps(p, ensure_ascii=False) for p in out)
head = ",\n".join(
    '  %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False))
    for k, v in data.items() if k != "words"
)
with open(path, "w", encoding="utf-8") as f:
    f.write("{\n%s,\n  \"words\": [\n  %s\n ]\n}\n" % (head, rows))

print("written", path, "hyphenated", hyph)
