# -*- coding: utf-8 -*-
"""Baut hu500.json aus hu_raw.WORDS minus hu_trim.DROP, inkl. Silbentrennung."""
import io, json, sys, collections
sys.path.insert(0, '/home/mario/sichtwort/tools/packs/wordlists')
from hu_raw import WORDS
from hu_trim import DROP

VOWELS = set("aáeéiíoóöőuúüű")
TRI = ["dzs"]
DI = ["cs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]
# geschriebene Langformen der Digraphen: ssz -> sz|sz usw.
LONG = {"ccs": "cs", "ddz": "dz", "ggy": "gy", "lly": "ly",
        "nny": "ny", "ssz": "sz", "tty": "ty", "zzs": "zs"}
# Kompositionsfugen, an denen der zweite Teil vokalisch beginnt
OVERRIDE = {"tűzoltó": "tűz-ol-tó", "rendőr": "rend-őr", "autó": "au-tó"}


def tokens(word):
    """Zerlegt in Einheiten: Vokal oder (mehrbuchstabiger) Konsonant."""
    out, i, n = [], 0, len(word)
    while i < n:
        if word[i] in VOWELS:
            out.append(word[i]); i += 1; continue
        if word[i:i+4] == "ddzs":
            out.append("dzs"); out.append("dzs"); i += 4; continue
        if word[i:i+3] in LONG:
            out.append(LONG[word[i:i+3]]); out.append(LONG[word[i:i+3]]); i += 3; continue
        if word[i:i+3] in TRI:
            out.append(word[i:i+3]); i += 3; continue
        if word[i:i+2] in DI:
            out.append(word[i:i+2]); i += 2; continue
        out.append(word[i]); i += 1
    return out


def syllabify(word):
    if word in OVERRIDE:
        return OVERRIDE[word]
    t = tokens(word)
    vidx = [i for i, u in enumerate(t) if u in VOWELS]
    if len(vidx) < 2:
        return word
    cuts = []
    for a, b in zip(vidx, vidx[1:]):
        gap = b - a - 1              # Konsonanteneinheiten zwischen den Vokalen
        if gap == 0:
            cuts.append(b)           # Vokal + Vokal: davor trennen
        elif gap == 1:
            cuts.append(a + 1)       # V-CV
        else:
            cuts.append(b - 1)       # VC..C-CV: nur letzter Konsonant nach rechts
    parts, prev = [], 0
    for c in cuts:
        parts.append("".join(t[prev:c])); prev = c
    parts.append("".join(t[prev:]))
    return "-".join(parts)


def main():
    seen, uniq = set(), []
    for w, ty in WORDS:
        if w in seen:
            continue
        seen.add(w); uniq.append((w, ty))
    drop = set(DROP)
    kept = [(w, ty) for w, ty in uniq if w not in drop]

    try:
        import pyphen
        dic = pyphen.Pyphen(lang='hu_HU')
    except Exception:
        dic = None

    words, hy, mismatch = [], 0, []
    for w, ty in kept:
        s = syllabify(w)
        if dic is not None:
            p = dic.inserted(w)
            if p.count('-') and p != s:
                mismatch.append((w, s, p))
        if '-' in s:
            hy += 1
        words.append([s, ty])

    data = {"id": "hu500", "language": "hu",
            "nameDE": "Grundwortschatz Ungarisch",
            "nameEN": "Hungarian basic vocabulary",
            "words": words}
    out = '/home/mario/sichtwort/tools/packs/wordlists/hu500.json'
    with io.open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("written", out, len(words), "hyphenated", hy)
    print("types", collections.Counter(t for _, t in words))
    print("pyphen-abweichungen:", len(mismatch))
    for m in mismatch[:60]:
        print("  ", m[0], "| eigen:", m[1], "| pyphen:", m[2])


main()
