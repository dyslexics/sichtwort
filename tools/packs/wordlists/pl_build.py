# -*- coding: utf-8 -*-
"""Baut pl500.json aus pl_raw.py: kuerzt auf 500 Eintraege und silbentrennt via pyphen."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pl_raw import WORDS
import pyphen

CUT = set("""
kredą ono wasz wszyscy znowu nigdzie wszędzie mniej więcej także czasem razem blisko daleko
dobranoc jeśli więc chyba ktoś coś obok
odpoczywać marzyć rzucić wybierać zbierać ubierać kąpać sprzedawać próbować witać kleić łapać
kopać wołać odpowiadać
fioletowy srebrny złoty pomarańczowy kwaśny słony straszny grzeczny gotowy ostatni bogaty
biedny chudy
mamusia tatuś gość sąsiad nazwisko
uczennica nauczycielka biblioteka przedszkole długopis hulajnoga telefon komputer obrazek
piórnik ławka tablica farby nożyczki
żyrafa zebra krokodyl tygrys lew małpa słoń orzeł bocian wróbel gęś sarna
ślimak biedronka gniazdo skrzydło
kiełbasa szynka dżem winogrono arbuz pomarańcza malina śliwka wiśnia fasola sałata kasza
jogurt śmietana mąka makaron orzech grzyb
ramię plecy
piżama pasek guzik kieszeń spódnica
sufit dywan lustro kanapa poduszka ręcznik szczotka garnek worek świeca kosz koszyk
tęcza mróz gałąź róża łąka wyspa ścieżka plaża dworzec lotnisko poczta szpital
kamień jezioro
traktor tramwaj
minuta godzina urodziny taniec radość śmiech łza historia początek film
""".split())

DIGRAPHS = ("sz", "cz", "rz", "ch", "dz", "dź", "dż")
VOWELS = set("aąeęioóuy")


def tokenize(word):
    """Zerlegt in Tokens; Digraphen bleiben ein Token."""
    toks, i = [], 0
    while i < len(word):
        if word[i:i + 2] in DIGRAPHS:
            toks.append(word[i:i + 2])
            i += 2
        else:
            toks.append(word[i])
            i += 1
    return toks


def nuclei(toks):
    """Indizes der Silbenkerne; 'i' vor Vokal ist Erweichungszeichen, kein Kern."""
    idx = []
    for j, t in enumerate(toks):
        if t in DIGRAPHS or t not in VOWELS:
            continue
        if t == "i" and j + 1 < len(toks) and toks[j + 1] in VOWELS and toks[j + 1] != "i":
            continue
        idx.append(j)
    return idx


def fallback_split(word):
    """Nur fuer Woerter, die pyphen gar nicht trennt: V-CV bzw. VC-CV."""
    toks = tokenize(word)
    kerns = nuclei(toks)
    if len(kerns) < 2:
        return word
    cuts = []
    for a, b in zip(kerns, kerns[1:]):
        gap = b - a - 1
        cuts.append(a + 1 if gap == 0 else (b if gap == 1 else a + 2))
    parts, prev = [], 0
    for c in cuts:
        parts.append("".join(toks[prev:c]))
        prev = c
    parts.append("".join(toks[prev:]))
    return "-".join(merge_vowelless([p for p in parts if p]))


def hyphenate(dic, word):
    """Silbentrennung; bricht nie innerhalb eines Digraphen."""
    if len(word) < 3:
        return word
    positions = sorted(dic.positions(word))
    keep = []
    for p in positions:
        if 0 < p < len(word) and word[p - 1:p + 1].lower() in DIGRAPHS:
            continue
        if p <= 0 or p >= len(word):
            continue
        keep.append(p)
    if not keep:
        return fallback_split(word)
    out, prev = [], 0
    for p in keep:
        out.append(word[prev:p])
        prev = p
    out.append(word[prev:])
    return "-".join(merge_vowelless(out))


def merge_vowelless(parts):
    """Silben ohne Vokalkern an die naechste (bzw. letzte) Silbe anhaengen."""
    res = []
    carry = ""
    for p in parts:
        if not nuclei(tokenize(p)):
            carry += p
            continue
        res.append(carry + p)
        carry = ""
    if carry:
        if res:
            res[-1] += carry
        else:
            res.append(carry)
    return res


# Hiatus, den die pyphen-Muster falsch als Diphthong behandeln
OVERRIDES = {"nauczyciel": "na-u-czy-ciel"}


def main():
    words = [(w, t) for w, t in WORDS if w not in CUT]
    missing = CUT - {w for w, _ in WORDS}
    if missing:
        raise SystemExit("CUT-Woerter nicht in Rohliste: %s" % sorted(missing))
    if len(words) != 500:
        raise SystemExit("Erwartet 500, habe %d" % len(words))

    dic = pyphen.Pyphen(lang="pl_PL", left=1, right=1)
    entries = [[OVERRIDES.get(w) or hyphenate(dic, w), t] for w, t in words]

    out = {
        "id": "pl500",
        "language": "pl",
        "nameDE": "Grundwortschatz Polnisch",
        "nameEN": "Polish basic vocabulary",
        "words": entries,
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pl500.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("geschrieben:", path)


if __name__ == "__main__":
    main()
