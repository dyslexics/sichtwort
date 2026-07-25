#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt die JSON-Wortlisten für die Sichtwort-App.

    /home/mario/sichtwort/tools/venv/bin/python gen_wordlists.py [--check]

--check schreibt nichts, sondern prüft nur Silbentrennung und Konsistenz.
Die Wörter selbst stehen in wordlists_data.py; hier passiert nur
Silbentrennung (pyphen + manuelle Korrekturen) und Qualitätssicherung.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pyphen

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wordlists_data as D  # noqa: E402

OUT_DIR = Path("/home/mario/sichtwort/Sources/Resources/WordLists")

DIC_DE = pyphen.Pyphen(lang="de_DE")
DIC_EN = pyphen.Pyphen(lang="en_US")

# ---------------------------------------------------------------------------
# Manuelle Silbentrennung
#
# pyphen liefert Trennstellen für den Druck: eine Silbe aus einem einzelnen
# Vokalbuchstaben wird am Wortanfang/-ende nicht abgetrennt ("oder", "über",
# "aber"). Fürs Silbenlesen brauchen wir aber die echte Sprechsilbe, deshalb
# hier die Korrekturen. Ebenso Fälle, in denen pyphen falsch trennt
# ("war-um" statt "wa-rum").
# ---------------------------------------------------------------------------

MANUAL_DE = {
    # 1. pyphen trennt einen einzelnen Vokal am Wortanfang nicht ab
    #    (Drucksatzregel), fürs Silbenlesen brauchen wir die Sprechsilbe.
    "aber": "a-ber", "Abend": "A-bend", "Acker": "A-cker", "Ameise": "A-mei-se",
    "Apotheke": "A-po-the-ke", "April": "A-pril", "Asche": "A-sche",
    "eben": "e-ben", "Ecke": "E-cke", "einen": "ei-nen", "Elefant": "E-le-fant",
    "Esel": "E-sel", "Idee": "I-dee", "Igel": "I-gel", "oben": "o-ben",
    "oder": "o-der", "Ofen": "O-fen", "Oma": "O-ma", "Opa": "O-pa",
    "Orange": "O-ran-ge", "orange": "o-ran-ge", "Ufer": "U-fer",
    "Universität": "U-ni-ver-si-tät", "Universum": "U-ni-ver-sum",
    "Uranus": "U-ra-nus", "üben": "ü-ben", "über": "ü-ber",
    "überall": "ü-ber-all", "überlegen": "ü-ber-le-gen",
    "übernachten": "ü-ber-nach-ten", "überraschen": "ü-ber-ra-schen",
    "Überraschung": "Ü-ber-ra-schung", "beobachten": "be-o-bach-ten",

    # 2. pyphen-Fehler: Silbengrenze ohne Vokal ("Fa-r-be", "Sa-lz")
    "Farbe": "Far-be", "Salz": "Salz", "salzig": "sal-zig",
    "scharf": "scharf", "schwarz": "schwarz", "glücklich": "glück-lich",
    "nebenan": "ne-ben-an",

    # 3. falsche Trennstelle
    "warum": "wa-rum", "darum": "da-rum", "herum": "he-rum",
    "worum": "wo-rum", "darauf": "da-rauf", "darin": "da-rin",
    "gegenüber": "ge-gen-ü-ber",

    # 4. Komposita und Fremdwörter, die pyphen zu grob trennt
    "Abendessen": "A-bend-es-sen", "Bibliothek": "Bi-bli-o-thek",
    "Pullover": "Pull-o-ver", "Puzzle": "Puz-zle",
}

MANUAL_EN = {
    # pyphen trennt einsilbig-scheinende Wörter mit Vokal-Anlaut bzw.
    # auslautendem -y nicht ab.
    "about": "a-bout", "above": "a-bove", "again": "a-gain",
    "along": "a-long", "America": "A-mer-i-ca", "any": "a-ny",
    "around": "a-round", "away": "a-way", "city": "cit-y",
    "enough": "e-nough", "idea": "i-de-a", "many": "man-y",
    "open": "o-pen", "over": "o-ver", "study": "stud-y", "very": "ver-y",
    # sonstige Korrekturen
    "farmer": "farm-er", "robin": "rob-in",
}

# ---------------------------------------------------------------------------
# Silbentrennung
# ---------------------------------------------------------------------------

VOWELS_DE = "aeiouäöüy"
DIPHTHONGS_DE = {"ei", "ai", "au", "eu", "äu", "ey", "ay", "oi", "ui",
                 "ie", "aa", "ee", "oo", "uu"}


def estimate_syllables_de(word: str) -> int:
    """Grobe Sprechsilbenzahl: Anzahl der Vokalkerne.

    Nur ein Prüfwerkzeug — Abweichungen von der pyphen-Trennung werden
    gemeldet und dann manuell entschieden (MANUAL_DE).
    """
    w = word.lower().replace("qu", "kw_")  # u nach q ist kein Kern
    w = w.replace("_", "")
    runs = re.findall(f"[{VOWELS_DE}]+", w)
    count = 0
    for run in runs:
        i = 0
        while i < len(run):
            if i + 1 < len(run) and run[i:i + 2] in DIPHTHONGS_DE:
                i += 2
            else:
                i += 1
            count += 1
    return max(count, 1)


def syllabify(word: str, lang: str) -> str:
    manual = MANUAL_DE if lang == "de" else MANUAL_EN
    if word in manual:
        return manual[word]
    dic = DIC_DE if lang == "de" else DIC_EN
    if " " in word:  # z.B. "Santa Claus"
        return " ".join(dic.inserted(part) for part in word.split(" "))
    return dic.inserted(word)


# Wörter, bei denen die Vokalkern-Schätzung danebenliegt, die Trennung aber
# geprüft und korrekt ist (Hiate wie e-u, u-i, o-i, die keine Diphthonge sind).
OK_SYLL = {
    "Ferien",     # Fe-ri-en  (ie ist hier kein Diphthong)
    "Pinguin",    # Pin-gu-in
    "Museum",     # Mu-se-um
    "Asteroid",   # As-te-ro-id
    "Countdown",  # engl. Lehnwort, zweisilbig gesprochen
    "Meteorit",   # Me-te-o-rit
    "Familie",    # Fa-mi-lie
}


def check_de(word: str, syl: str) -> str | None:
    """Meldet verdächtige Trennungen zurück (oder None, wenn plausibel)."""
    parts = syl.split("-")
    est = estimate_syllables_de(word)
    if len(parts) != est and word not in OK_SYLL:
        return f"{word}: '{syl}' hat {len(parts)} Silben, geschätzt {est}"
    for p in parts:
        if not p:
            return f"{word}: leere Silbe in '{syl}'"
        if not re.search(f"[{VOWELS_DE}]", p.lower()):
            return f"{word}: Silbe ohne Vokal in '{syl}'"
    return None


# ---------------------------------------------------------------------------
# Listenaufbau + Qualitätssicherung
# ---------------------------------------------------------------------------

VALID_TYPES = {"n", "v", "a", "o"}
EN_UPPER_OK = {"I", "Christmas", "Santa Claus", "America", "Indian"}


def build(pairs, lang: str, list_id: str) -> list[list[str]]:
    words: list[list[str]] = []
    seen: set[str] = set()
    problems: list[str] = []

    for word, typ in pairs:
        if typ not in VALID_TYPES:
            problems.append(f"{list_id}: ungültiger Typ '{typ}' bei {word}")
        if word in seen:
            problems.append(f"{list_id}: DUPLIKAT {word}")
            continue
        seen.add(word)

        syl = syllabify(word, lang)
        if syl.replace("-", "").replace(" ", "") != word.replace(" ", ""):
            problems.append(f"{list_id}: Silben passen nicht zum Wort: {word} -> {syl}")
        if syl.startswith("-") or syl.endswith("-") or "--" in syl:
            problems.append(f"{list_id}: fehlerhafter Bindestrich: {syl}")

        first = word[0]
        if lang == "de":
            if typ == "n" and not first.isupper():
                problems.append(f"{list_id}: Nomen klein geschrieben: {word}")
            if typ != "n" and first.isupper():
                problems.append(f"{list_id}: Nicht-Nomen groß geschrieben: {word}")
            msg = check_de(word, syl)
            if msg:
                problems.append(f"{list_id}: SILBEN? {msg}")
        else:
            if first.isupper() and word not in EN_UPPER_OK:
                problems.append(f"{list_id}: EN groß geschrieben: {word}")

        words.append([syl, typ])

    if problems:
        print(f"\n--- Probleme in {list_id} ({len(problems)}) ---")
        for p in problems:
            print("  " + p)
    return words


def write_list(list_id: str, lang: str, name_de: str, name_en: str,
               pairs, check_only: bool) -> dict:
    words = build(pairs, lang, list_id)
    data = {
        "id": list_id,
        "language": lang,
        "nameDE": name_de,
        "nameEN": name_en,
        "words": words,
    }
    if not check_only:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        path = OUT_DIR / f"{list_id}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8")
    return data


def type_counts(data: dict) -> dict:
    counts = {"n": 0, "v": 0, "a": 0, "o": 0}
    for _, t in data["words"]:
        counts[t] = counts.get(t, 0) + 1
    return counts


def main() -> int:
    check_only = "--check" in sys.argv

    de1000_pairs = list(D.DE500) + list(D.DE1000_EXTRA)
    dolch_pairs = list(D.DOLCH_SERVICE) + [(n, "n") for n in D.DOLCH_NOUNS]

    specs = [
        ("de500", "de", "Grundwortschatz 500", "German Basic 500", D.DE500),
        ("de1000", "de", "Grundwortschatz 1000", "German Basic 1000", de1000_pairs),
        ("theme_silben", "de", "Silbenwörter", "Syllable words", D.THEME_SILBEN),
        ("theme_dehnungs_h", "de", "Dehnungs-h", "Silent h (long vowel)", D.THEME_DEHNUNGS_H),
        ("theme_ei_ie", "de", "ei und ie", "ei and ie", D.THEME_EI_IE),
        ("theme_doppelkonsonanten", "de", "Doppelkonsonanten", "Double consonants",
         D.THEME_DOPPELKONSONANTEN),
        ("theme_sch", "de", "Wörter mit sch", "Words with sch", D.THEME_SCH),
        ("theme_sp_st", "de", "sp und st", "sp and st", D.THEME_SP_ST),
        ("theme_d_t", "de", "d und t", "d and t", D.THEME_D_T),
        ("theme_weltraum", "de", "Weltraum", "Outer space", D.THEME_WELTRAUM),
        ("en_dolch", "en", "Dolch Sight Words", "Dolch Sight Words", dolch_pairs),
        ("en_fry", "en", "Fry Sight Words 300", "Fry Sight Words 300", D.FRY300),
    ]

    results = {}
    for list_id, lang, name_de, name_en, pairs in specs:
        results[list_id] = write_list(list_id, lang, name_de, name_en, pairs, check_only)

    # --- Anzahl-Checks ---
    errors = []
    for list_id, expected in (("de500", 500), ("de1000", 1000), ("en_dolch", 315),
                              ("en_fry", 300)):
        got = len(results[list_id]["words"])
        if got != expected:
            errors.append(f"{list_id}: {got} Wörter statt {expected}")

    # --- de500 ⊂ de1000 ---
    w500 = {w[0].replace("-", "") for w in results["de500"]["words"]}
    w1000 = {w[0].replace("-", "") for w in results["de1000"]["words"]}
    missing = w500 - w1000
    if missing:
        errors.append(f"de500 nicht in de1000: {sorted(missing)}")

    # --- Themenlisten 40–60 Wörter ---
    for list_id in results:
        if list_id.startswith("theme_"):
            n = len(results[list_id]["words"])
            if not 40 <= n <= 60:
                errors.append(f"{list_id}: {n} Wörter (erwartet 40–60)")

    print("\n=== Zusammenfassung ===")
    for list_id, _, _, _, _ in specs:
        data = results[list_id]
        c = type_counts(data)
        print(f"{list_id + '.json':30s} {len(data['words']):5d} Wörter   "
              f"n={c['n']:4d} v={c['v']:4d} a={c['a']:4d} o={c['o']:4d}")

    if errors:
        print("\n!!! FEHLER !!!")
        for e in errors:
            print("  " + e)
        return 1

    print("\nAlle Prüfungen bestanden."
          + ("  (--check: nichts geschrieben)" if check_only else f"  Geschrieben nach {OUT_DIR}"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
