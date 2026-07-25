# Wortlisten-Schema (Sichtwort)

Eine JSON-Datei pro Wortliste, UTF-8, Dateiname = `id` + `.json`.
Die Dateien werden reproduzierbar erzeugt von
`/home/mario/sichtwort/tools/gen_wordlists.py` (Wortdaten in `wordlists_data.py`).

```json
{
  "id": "de500",
  "language": "de",
  "nameDE": "Grundwortschatz 500",
  "nameEN": "German Basic 500",
  "words": [["und","o"],["Fens-ter","n"],["ge-hen","v"],["schön","a"]]
}
```

## Felder

| Feld       | Bedeutung                                                        |
|------------|------------------------------------------------------------------|
| `id`       | Eindeutiger Schlüssel, zugleich Dateiname (`de500` → `de500.json`) |
| `language` | `de` oder `en` — steuert Vorlesestimme und Prüflogik              |
| `nameDE`   | Anzeigename in der deutschen Oberfläche                           |
| `nameEN`   | Anzeigename in der englischen Oberfläche                          |
| `words`    | Liste aus `[silbenmarkiertes_wort, typ]`                          |

## Silbenmarkierung

- Silbengrenzen werden mit `-` markiert: `Fens-ter`, `ge-hen`, `Ra-ke-te`.
- Das **echte Wort** ist die Silbenfolge ohne `-` (`Fens-ter` → `Fenster`).
  So prüft die App die Eingabe, und so wird das Wort ohne Silbenanzeige gezeigt.
- Einsilbige Wörter stehen ohne `-` (`und`, `Hund`, `groß`).
- Kein `-` am Wortanfang oder -ende, keine leeren Silben, jede Silbe hat einen Vokal.
- Ausnahme Englisch: `good-bye` ist als Wort `goodbye` gespeichert, die Silbenform
  `good-bye` entspricht zugleich der üblichen Schreibweise.

## Wortarten (`typ`)

| Wert | Bedeutung                                                            |
|------|----------------------------------------------------------------------|
| `n`  | Nomen — deutsch immer mit großem Anfangsbuchstaben                    |
| `v`  | Verb                                                                  |
| `a`  | Adjektiv                                                              |
| `o`  | sonstige: Artikel, Pronomen, Präpositionen, Konjunktionen, Adverbien, Zahlwörter |

Deutsch: Nur Nomen werden großgeschrieben, alles andere klein.
Englisch: alles klein außer Eigennamen (`I`, `Christmas`, `Santa Claus`,
`America`, `Indian`).

## Rechtschreibung

- Deutsche Wörter in normaler Rechtschreibung **mit ß** (`groß`, `Straße`, `weiß`).
- Die **Schweizer Variante (ss statt ß) wird zur Laufzeit abgeleitet**
  (`WordEntry.display(swiss:)`), nicht in den Daten gedoppelt.

## Vorhandene Listen

| Datei                          | Wörter | Inhalt                                  |
|--------------------------------|--------|------------------------------------------|
| `de500.json`                   | 500    | Grundwortschatz Grundschule              |
| `de1000.json`                  | 1000   | Obermenge von `de500` + 500 weitere      |
| `theme_silben.json`            | 58     | Silbenwörter (2–4 Silben)                |
| `theme_dehnungs_h.json`        | 58     | Dehnungs-h                               |
| `theme_ei_ie.json`             | 60     | ei und ie                                |
| `theme_doppelkonsonanten.json` | 60     | Doppelkonsonanten                        |
| `theme_sch.json`               | 58     | Wörter mit sch                           |
| `theme_sp_st.json`             | 59     | sp und st                                |
| `theme_d_t.json`               | 59     | d und t (Auslaut, Verwechslungswörter)   |
| `theme_weltraum.json`          | 59     | Weltraum                                 |
| `en_dolch.json`                | 315    | Dolch Sight Words (220 + 95 Nomen)       |
| `en_fry.json`                  | 300    | Fry Sight Words 1–300                    |

Die Reihenfolge in der App steuert `WordLists.builtinOrder` in
`Sources/Models/WordData.swift`; eine neue Liste muss dort eingetragen werden.

## Neue Liste hinzufügen

1. Wörter in `tools/wordlists_data.py` als `[(wort, typ), ...]` ergänzen.
2. In `tools/gen_wordlists.py` in `specs` eintragen (id, Sprache, Namen).
3. `tools/venv/bin/python tools/gen_wordlists.py --check` — prüft Duplikate,
   Wortarten, Groß-/Kleinschreibung und Silbentrennung, schreibt nichts.
4. Ohne `--check` erneut laufen lassen; die JSON-Dateien werden neu geschrieben.

Die Silbentrennung kommt aus pyphen und wird gegen eine Vokalkern-Schätzung
geprüft. pyphen liefert Drucktrennstellen und trennt einzelne Vokale am
Wortanfang nicht ab (`oder`, `über`); solche Fälle stehen in `MANUAL_DE`
bzw. `MANUAL_EN` in `gen_wordlists.py`.
