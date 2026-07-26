# -*- coding: utf-8 -*-
"""Baut bs500.json aus bs_raw.py: Auswahl auf 500, Silbentrennung, Validierung."""
import json, collections, sys
import pyphen
import bs_raw

DROP = set("""
komšija gost policajac vozač pekar unuk momak drug lektira zvono naslov bojica
gumica ocjena kreda crtež klupa ploča prezime ruksak učionica magarac mače štene
gnijezdo krilo rep vjeverica jež pauk muha mrav puž žirafa tigar jelen guska patka
pijetao koza obraz čelo koža kost suza glas tijelo rame stopalo trbuh leđa maslac
supa povrće kruška grožđe trešnja šljiva breskva lubenica orah brašno torta bombon
keks pita salata večera doručak kafa kupatilo ormar polica lampa ogledalo tepih
jastuk televizor tanjir sapun ručnik četkica peć kanta stepenice dvorište garaža
ograda sjena potok korijen sjeme pijesak staza dim duga mrak praznik sedmica minuta
bolnica crkva igralište autobus avion brod bicikl zmaj balon pismo film ples sport
kino pijaca zoo novac muzika haljina čarapa rukavica dugme suknja kaput papuča šal
jakna lisica kokoš jezero planina
kiseo gorak slan mršav plitak ljubičast smeđ siv blizak pitom divlji mlak ljubazan
različit srednji
svirati plesati mjeriti saditi kopati brati hraniti penjati javiti bojati
ovamo noćas jutros uvečer nikada ponekad mene tebe nama uskoro
""".split())

VOWELS = set("aeiou")
DIGRAPHS = ("lj", "nj", "dž")

# pyphen(hr) legt sC-Gruppen in die Coda (ses-tra) und uebersieht ein paar
# Vokalfolgen. BKS-Silbenregel: Gruppe, die ein Wort beginnen kann, gehoert zur
# folgenden Silbe -- ausser an klarer Praefixgrenze (iz-, is-, raz-, od-).
OVERRIDES = {
    "iza": "i-za", "izaći": "i-za-ći", "iako": "i-a-ko", "auto": "a-u-to",
    "poklon": "po-klon",
    "kasno": "ka-sno", "isto": "i-sto", "sestra": "se-stra", "usta": "u-sta",
    "misliti": "mi-sli-ti", "jesti": "je-sti", "ustati": "u-sta-ti",
    "čistiti": "či-sti-ti", "poslati": "po-sla-ti", "rasti": "ra-sti",
    "pustiti": "pu-sti-ti", "ostati": "o-sta-ti", "sjesti": "sje-sti",
    "zaspati": "za-spa-ti", "bolestan": "bo-le-stan", "desni": "de-sni",
    "zvijezda": "zvi-je-zda",
}


def has_nucleus(seg):
    """Silbenkern: Vokal, oder silbisches r (Segment ganz ohne Vokal, enthaelt r)."""
    if any(c in VOWELS for c in seg):
        return True
    return "r" in seg


def merge_toneless(parts):
    """Segmente ohne Silbenkern an den Nachbarn haengen."""
    out = []
    for p in parts:
        if out and (not has_nucleus(p) or not has_nucleus(out[-1])):
            out[-1] += p
        else:
            out.append(p)
    return out


def fix_digraphs(parts):
    """Kein Trennstrich innerhalb von lj / nj / dž: Grenze nach links schieben."""
    i = 0
    while i < len(parts) - 1:
        if (parts[i][-1] + parts[i + 1][0]) in DIGRAPHS:
            parts[i + 1] = parts[i][-1] + parts[i + 1]
            parts[i] = parts[i][:-1]
        i += 1
    return [p for p in parts if p]


def syllabify(word, dic):
    if word in OVERRIDES:
        return OVERRIDES[word]
    parts = dic.inserted(word).split("-")
    parts = fix_digraphs(parts)
    parts = merge_toneless(parts)
    return "-".join(parts)


def main():
    words = [(w, t) for w, t in bs_raw.WORDS if w not in DROP]
    seen = set()
    uniq = []
    for w, t in words:
        if w in seen:
            continue
        seen.add(w)
        uniq.append((w, t))
    if len(uniq) != 500:
        print("FEHLER: %d Woerter nach Drop (erwartet 500)" % len(uniq))
        unknown = DROP - {w for w, _ in bs_raw.WORDS}
        if unknown:
            print("DROP-Eintraege ohne Treffer:", sorted(unknown))
        sys.exit(1)

    dic = pyphen.Pyphen(lang="hr", left=1, right=1)
    entries = []
    for w, t in uniq:
        h = syllabify(w, dic)
        assert h.replace("-", "") == w, (w, h)
        for seg in h.split("-"):
            assert has_nucleus(seg), (w, h, seg)
        entries.append([h, t])

    data = {
        "id": "bs500",
        "language": "bs",
        "nameDE": "Grundwortschatz BKS (Bosnisch/Kroatisch/Serbisch)",
        "nameEN": "Bosnian/Croatian/Serbian basic vocabulary",
        "words": entries,
    }
    with open("bs500.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")

    multi = sum(1 for h, _ in entries if "-" in h)
    print("geschrieben:", len(entries), "mit Trennung:", multi)
    print(collections.Counter(t for _, t in entries))
    # Digraph-Kontrolle
    for h, _ in entries:
        parts = h.split("-")
        for a, b in zip(parts, parts[1:]):
            if (a[-1] + b[0]) in DIGRAPHS:
                print("DIGRAPH-SPLIT:", h)


if __name__ == "__main__":
    main()
