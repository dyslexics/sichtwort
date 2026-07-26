# -*- coding: utf-8 -*-
"""Regelbasierte spanische Silbentrennung.

Das pyphen-Woerterbuch hyph_es ist unvollstaendig (sano, mono, contra, salir,
traer bleiben ungetrennt), deshalb hier die RAE-Silbenregeln direkt:
Diphthong/Hiat, Digraphen (ch, ll, rr), stummes u in qu/gu+e,i sowie
untrennbare Konsonant+l/r-Gruppen.
"""

VOWELS = set("aeiouáéíóúü")
STRONG = set("aeoáéó")
WEAK = set("iuüy")
ACCENTED_WEAK = set("íú")          # bildet immer einen Hiat
INSEPARABLE = {
    "bl", "br", "cl", "cr", "dr", "fl", "fr",
    "gl", "gr", "kl", "kr", "pl", "pr", "tr",
}


def _units(word):
    """Zerlegt in Einheiten: ('C', text) bzw. ('V', text)."""
    out = []
    i, n = 0, len(word)
    while i < n:
        ch = word[i]
        # stummes u in que/qui und gue/gui -> gehoert zum Konsonanten
        if ch in "qg" and i + 2 < n and word[i + 1] == "u" and word[i + 2] in "eiéí":
            out.append(("C", word[i:i + 2]))
            i += 2
            continue
        if word[i:i + 2] in ("ch", "ll", "rr"):
            out.append(("C", word[i:i + 2]))
            i += 2
            continue
        if ch == "y":
            # vor einem Vokal ist y Konsonant (ma-yo), sonst Vokal (hoy, muy)
            out.append(("C" if i + 1 < n and word[i + 1] in VOWELS else "V", ch))
            i += 1
            continue
        out.append(("V" if ch in VOWELS else "C", ch))
        i += 1
    return out


def _same_nucleus(v1, v2):
    if v1 in ACCENTED_WEAK or v2 in ACCENTED_WEAK:
        return False                      # rí-o, re-ír
    if v1 in STRONG and v2 in STRONG:
        return False                      # le-ón, cre-er, ma-es-tro
    if v1 == v2:
        return False
    return True                           # Diphthong: ie, ua, ei, iu ...


def syllables(word):
    units = _units(word)
    nuclei = []
    i = 0
    while i < len(units):
        if units[i][0] == "V":
            j = i
            while (j + 1 < len(units) and units[j + 1][0] == "V"
                   and _same_nucleus(units[j][1], units[j + 1][1])):
                j += 1
            nuclei.append((i, j))
            i = j + 1
        else:
            i += 1
    if len(nuclei) < 2:
        return [word]

    starts = [0]
    for k in range(len(nuclei) - 1):
        cons = list(range(nuclei[k][1] + 1, nuclei[k + 1][0]))
        if not cons:
            starts.append(nuclei[k + 1][0])          # Hiat
        elif len(cons) == 1:
            starts.append(cons[0])                   # V-CV
        else:
            a, b = units[cons[-2]][1], units[cons[-1]][1]
            group = a + b
            if len(a) == 1 and len(b) == 1 and group in INSEPARABLE:
                starts.append(cons[-2])              # ...-CCV (con-tra)
            else:
                starts.append(cons[-1])              # ...C-CV (car-ta)

    starts.append(len(units))
    return ["".join(t for _, t in units[starts[s]:starts[s + 1]])
            for s in range(len(starts) - 1)]


def hyphenate(word):
    return "-".join(syllables(word))
