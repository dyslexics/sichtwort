# Sichtwort

**Blitzlesen-Training für Kinder — gratis, werbefrei, offline, Open Source.**

Sichtwort trainiert den Sichtwortschatz: Ein Wort blitzt kurz auf, das Kind erfasst es
als Ganzes. So werden häufige Wörter automatisiert — das entlastet das Arbeitsgedächtnis
beim Lesen. Ein Projekt des [EÖDL — Erster Österreichischer Dachverband Legasthenie](https://www.legasthenie.at).

## Funktionen

- **Aufblitzzeit 0,02–5 Sekunden**, frei einstellbar; Wiederholen-Button mit exakt gleicher Dauer
- **Gemeinsam-Modus** (Erwachsener bewertet) und **Alleine-Modus** (Kind tippt, tolerante Prüfung)
- **Sprachausgabe** (on-device, offline) — das Kind hört, wie das Wort korrekt klingt
- **Easy-Reading-Overlay**: digitale Nachbildung der EASY-Reading™-Leseschablone — die blaue
  Karte mit Lesefenster gleitet über das Wort. „Read" liest das ganze Wort vor, „ABC"
  buchstabiert es Buchstabe für Buchstabe; das Fenster wandert mit, jeder Buchstabe wird
  mit seinem echten Buchstabennamen gesprochen
- **21 Sprachen**: Deutsch und Englisch (US-/GB-Stimme umschaltbar) sind integriert; 19 weitere
  Sprachen als gratis Sprachpakete direkt in der App ladbar — Spanisch, Spanisch (Mexiko),
  Französisch, Italienisch, Portugiesisch, Portugiesisch (Brasilien), Niederländisch, Dänisch,
  Norwegisch, Polnisch, Türkisch, Griechisch, Ungarisch, Rumänisch, BKS (Bosnisch/Kroatisch/
  Serbisch), Albanisch, Ukrainisch, Arabisch, Afrikaans. Jedes Paket: die 500 häufigsten
  Wörter der Sprache mit nativer Sprachausgabe, nach dem Download komplett offline
- **Silbenvisualisierung**: farbig alternierend oder Silben nacheinander aufleuchtend
- **Schriftwahl**: Standard, OpenDyslexic, Lexend + Schriftgrößenregler
- **Abenteuer-Modus**: adaptive Schwierigkeit (schneller bei Erfolg, langsamer bei Fehlern)
- **Fehler-Wiedervorlage**: falsch gelesene Wörter kommen automatisch wieder, bis sie sitzen
- **Mehrkind-Profile** mit eigener Statistik — ohne Accounts, alles bleibt auf dem Gerät
- **Wortschätze**: 500/1000 häufigste deutsche Wörter, englische Sight Words (Dolch & Fry),
  8 Themenlisten (Dehnungs-h, ei/ie, Doppelkonsonanten, sch, sp/st, d/t, Silbenwörter, Weltraum) — alle gratis
- **Eigene Wortlisten** mit CSV-Import und -Export, feste oder zufällige Reihenfolge,
  garantiert alle Wörter pro Durchlauf
- **Schweizer Rechtschreibung** (ss statt ß) zuschaltbar; Sprache pro Liste, nicht per Systemsprache
- Belohnungssystem mit endlosem Levelsystem, iPad-Unterstützung inkl. Querformat und Split View

## Datenschutz

Sichtwort erfasst **keine Daten**. Keine Accounts, keine Cloud, kein Tracking, keine Werbung,
keine In-App-Käufe. Die App funktioniert vollständig offline.

## Technik

SwiftUI, iOS/iPadOS 16+. Projekt wird mit [xcodegen](https://github.com/yonaskolb/XcodeGen)
aus `project.yml` generiert:

```bash
xcodegen generate
xcodebuild -scheme Sichtwort -destination "generic/platform=iOS Simulator" build CODE_SIGNING_ALLOWED=NO
```

Wortlisten liegen als JSON in `Sources/Resources/WordLists/` (Schema: siehe `SCHEMA.md` dort)
und werden mit `tools/gen_wordlists.py` generiert.

## Lizenz

[GPL-3.0](LICENSE). Schriften: [OpenDyslexic](https://opendyslexic.org) und
[Lexend](https://www.lexend.com) (SIL Open Font License).
