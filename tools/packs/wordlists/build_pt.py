# -*- coding: utf-8 -*-
"""Baut pt500.json aus pt_raw.py (Silbentrennung via pyphen 'pt_PT')."""
import io, json, os, sys, collections
import pyphen

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pt_raw import WORDS

# pyphen trennt die Diphthonge in 'ao'/'aos' faelschlich und laesst die Hiate
# in aviao/leao/sair/cair/avo ungetrennt; alles andere ist korrekt.
OVERRIDE = {
    "ao": "ao", "aos": "aos",
    "avião": "a-vi-ão", "leão": "le-ão",
    "sair": "sa-ir", "cair": "ca-ir", "avô": "a-vô",
}

dic = pyphen.Pyphen(lang="pt_PT", left=1, right=1)
words = [[OVERRIDE.get(w, dic.inserted(w)), t] for w, t in WORDS]

data = {
    "id": "pt500",
    "language": "pt",
    "nameDE": "Grundwortschatz Portugiesisch",
    "nameEN": "Portuguese basic vocabulary",
    "words": words,
}
out = os.path.join(HERE, "pt500.json")
with io.open(out, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# --- Validierung ------------------------------------------------------------
d = json.load(io.open(out, encoding="utf-8"))
errs = []
if d["id"] != "pt500" or d["language"] != "pt":
    errs.append("header falsch")
if len(d["words"]) != 500:
    errs.append("Anzahl %d != 500" % len(d["words"]))
plain = [e[0].replace("-", "") for e in d["words"]]
dups = [w for w, c in collections.Counter(plain).items() if c > 1]
if dups:
    errs.append("Duplikate: %s" % dups)
orig = [w for w, _ in WORDS]
for i, (e, o) in enumerate(zip(d["words"], orig)):
    if len(e) != 2:
        errs.append("Eintrag %d hat %d Felder" % (i, len(e)))
        continue
    if e[0].replace("-", "") != o:
        errs.append("Rekonstruktion %r != %r" % (e[0].replace("-", ""), o))
    if e[1] not in ("n", "v", "a", "o"):
        errs.append("Typ %r bei %r" % (e[1], o))
    if e[0].startswith("-") or e[0].endswith("-") or "--" in e[0]:
        errs.append("Trennfehler %r" % e[0])

if errs:
    print("FEHLER:")
    for e in errs:
        print(" -", e)
    sys.exit(1)

hy = sum(1 for e in d["words"] if "-" in e[0])
c = collections.Counter(e[1] for e in d["words"])
print("OK pt %d Wörter, %d mit Silbentrennung, n=%d v=%d a=%d o=%d"
      % (len(d["words"]), hy, c["n"], c["v"], c["a"], c["o"]))
