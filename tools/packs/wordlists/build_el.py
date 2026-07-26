# -*- coding: utf-8 -*-
"""Baut el500.json aus el_raw.py.

Silbentrennung nach den griechischen Schulregeln (Triantafyllidis):
 - Diphthonge/Digraphen (αι ει οι υι ου αυ ευ ηυ) bleiben zusammen,
   ausser bei Trema oder Akzent auf dem ersten Vokal.
 - Synizese: unbetontes ι/υ (auch ει/οι) vor Vokal bildet eine Silbe (μά-τια, δου-λειά).
 - Ein Konsonant zwischen Vokalen geht zur folgenden Silbe.
 - Zwei+ Konsonanten gehen zur folgenden Silbe, wenn ein griechisches Wort
   mit ihnen (bzw. den ersten beiden) beginnen kann; sonst bleibt der erste.
 - Doppelkonsonanten (λλ μμ σσ γγ ...) werden getrennt.
"""
import io
import json
import os
import unicodedata

from el_raw import WORDS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "el500.json")

ACCENTED = set("άέήίόύώΐΰ")
DIAERESIS = set("ϊϋΐΰ")
VOWELS = set("αεηιουω") | ACCENTED | DIAERESIS

DIGRAPHS = {"αι", "ει", "οι", "υι", "ου", "αυ", "ευ", "ηυ"}
GLIDES = {"ι", "υ", "ει", "οι", "υι"}

ONSETS = {
    "βγ", "βδ", "βλ", "βρ", "γδ", "γκ", "γλ", "γν", "γρ", "δρ",
    "θλ", "θν", "θρ", "κλ", "κν", "κρ", "κτ", "μν", "μπ", "ντ",
    "πλ", "πν", "πρ", "πτ", "σβ", "σγ", "σθ", "σκ", "σλ", "σμ",
    "σν", "σπ", "στ", "σφ", "σχ", "τζ", "τμ", "τρ", "τσ",
    "φθ", "φκ", "φλ", "φρ", "φτ", "φχ", "χθ", "χλ", "χν", "χρ", "χτ",
}


def base(ch):
    """Buchstabe ohne Akzent/Trema, Schluss-Sigma normalisiert."""
    if ch == "ς":
        return "σ"
    d = unicodedata.normalize("NFD", ch)
    return "".join(c for c in d if not unicodedata.combining(c))


def nuclei(run):
    """Zerlegt einen Vokal-Lauf in Silbenkerne."""
    out = []
    i = 0
    while i < len(run):
        if i + 1 < len(run):
            pair = base(run[i]) + base(run[i + 1])
            if (pair in DIGRAPHS and run[i] not in ACCENTED
                    and run[i + 1] not in DIAERESIS):
                out.append(run[i:i + 2])
                i += 2
                continue
        out.append(run[i])
        i += 1
    # Synizese: unbetontes ι/υ/ει/οι verschmilzt mit dem folgenden Kern
    merged = []
    for n in out:
        if (merged and "".join(base(c) for c in merged[-1]) in GLIDES
                and not any(c in ACCENTED or c in DIAERESIS for c in merged[-1])):
            merged[-1] += n
        else:
            merged.append(n)
    return merged


def syllabify(word):
    # Wort in abwechselnde Vokal-/Konsonantengruppen zerlegen
    groups = []
    for ch in word:
        kind = "V" if base(ch) in VOWELS else "C"
        if groups and groups[-1][0] == kind:
            groups[-1][1] += ch
        else:
            groups.append([kind, ch])

    parts = []
    for kind, text in groups:
        if kind == "V":
            parts.extend(("V", n) for n in nuclei(text))
        else:
            parts.append(("C", text))

    if not any(k == "V" for k, _ in parts):
        return word

    syls = []
    cur = ""
    for idx, (kind, text) in enumerate(parts):
        if kind == "V":
            if any(base(c) in VOWELS for c in cur):
                syls.append(cur)  # Hiatus: zwei Kerne ohne Konsonant dazwischen
                cur = ""
            cur += text
            continue
        rest = parts[idx + 1:]
        if not cur or not any(k == "V" for k, _ in rest):
            cur += text  # Anlaut vor erstem Vokal oder Auslaut am Wortende
            continue
        n = len(text)
        if n == 1:
            head, tail = "", text
        elif base(text[0]) == base(text[1]):
            head, tail = text[0], text[1:]
        elif base(text[0]) + base(text[1]) in ONSETS:
            head, tail = "", text
        else:
            head, tail = text[0], text[1:]
        syls.append(cur + head)
        cur = tail
    syls.append(cur)
    return "-".join(s for s in syls if s)


def main():
    words = [[syllabify(w), t] for w, t in WORDS]

    data = {
        "id": "el500",
        "language": "el",
        "nameDE": "Grundwortschatz Griechisch",
        "nameEN": "Greek basic vocabulary",
        "words": words,
    }
    with io.open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
        fh.write("\n")

    # --- Validierung ---
    with io.open(OUT, encoding="utf-8") as fh:
        chk = json.load(fh)
    ws = chk["words"]
    assert chk["id"] == "el500" and chk["language"] == "el"
    assert len(ws) == 500, "Anzahl: %d" % len(ws)
    plain = [w.replace("-", "") for w, _ in ws]
    assert len(set(plain)) == 500, "Duplikate"
    orig = [w for w, _ in WORDS]
    assert plain == orig, "Wort != Wort ohne Trennung"
    assert all(t in {"n", "v", "a", "o"} for _, t in ws), "unbekannter Typ"
    assert all(w and not w.startswith("-") and not w.endswith("-")
               and "--" not in w for w, _ in ws), "Trennzeichen-Fehler"

    hyph = sum(1 for w, _ in ws if "-" in w)
    counts = {t: sum(1 for _, x in ws if x == t) for t in "nvao"}
    print("OK el %d Wörter, %d mit Silbentrennung, n=%d v=%d a=%d o=%d"
          % (len(ws), hyph, counts["n"], counts["v"], counts["a"], counts["o"]))


if __name__ == "__main__":
    main()
