# -*- coding: utf-8 -*-
"""Baut tr500.json aus tr_raw.py.

Türkische Silbentrennung ist streng regelmäßig (kein pyphen-Dict nötig):
 - jede Silbe enthält genau einen Vokal
 - 0 Konsonanten zwischen zwei Vokalen -> Grenze direkt nach dem ersten Vokal
 - 1 Konsonant   -> gehört zur folgenden Silbe (V-CV)
 - n>=2          -> alle bis auf den letzten bleiben vorne (VC(C)-CV)
Anlaut- und Auslautkonsonanten hängen an der ersten bzw. letzten Silbe.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tr_raw import WORDS  # noqa: E402

VOWELS = set("aeıioöuü")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tr500.json")
TARGET = 500


def syllabify(word):
    idx = [i for i, ch in enumerate(word) if ch in VOWELS]
    if len(idx) < 2:
        return word
    cuts = []
    for a, b in zip(idx, idx[1:]):
        gap = b - a - 1
        cuts.append(a + 1 if gap == 0 else b - 1)
    parts, prev = [], 0
    for c in cuts:
        parts.append(word[prev:c])
        prev = c
    parts.append(word[prev:])
    return "-".join(parts)


def main():
    seen, entries, dropped = set(), [], []
    for word, kind in WORDS:
        if kind is None or " " in word:
            dropped.append(word)
            continue
        if word in seen:
            dropped.append("DUP:" + word)
            continue
        seen.add(word)
        entries.append([syllabify(word), kind])

    if len(entries) != TARGET:
        print("Kandidaten nach Dedup: %d (Ziel %d)" % (len(entries), TARGET))
        print("verworfen:", ", ".join(dropped))
        return 1

    data = {
        "id": "tr500",
        "language": "tr",
        "nameDE": "Grundwortschatz Türkisch",
        "nameEN": "Turkish basic vocabulary",
        "words": entries,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write("\n")

    # --- Validierung gegen die frisch geschriebene Datei --------------------
    with open(OUT, encoding="utf-8") as fh:
        chk = json.load(fh)
    words = chk["words"]
    assert chk["id"] == "tr500" and chk["language"] == "tr", "Kopf falsch"
    assert len(words) == TARGET, "Anzahl %d" % len(words)
    plain = [w.replace("-", "") for w, _ in words]
    assert len(set(plain)) == TARGET, "Duplikate vorhanden"
    for (w, t), p in zip(words, plain):
        assert t in {"n", "v", "a", "o"}, "Typ %r bei %s" % (t, w)
        assert p and " " not in p, "Mehrwort/leer: %r" % w
        assert not w.startswith("-") and not w.endswith("-") and "--" not in w, w
        for syl in w.split("-"):
            assert sum(c in VOWELS for c in syl) == 1, "Silbe ohne 1 Vokal: %s" % w

    hy = sum(1 for w, _ in words if "-" in w)
    cnt = {k: sum(1 for _, t in words if t == k) for k in "nvao"}
    print("OK tr %d Wörter, %d mit Silbentrennung, n=%d v=%d a=%d o=%d"
          % (len(words), hy, cnt["n"], cnt["v"], cnt["a"], cnt["o"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
