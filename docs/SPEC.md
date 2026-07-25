# Sichtwort — Spezifikation (freigegeben 2026-07-25)

## Positionierung
Freie, werbefreie Open-Source-Alternative zu „Blitzlesen: Das Original" (Simon Storz, iOS, 3,99 €).
Gleiche bewährte Kernmechanik (Sichtwortschatz-Aufbau durch Blitz-Darbietung), alle dokumentierten
Kritikpunkte aus den App-Store-Rezensionen behoben, EÖDL-Branding.
**Gratis. Keine In-App-Käufe. Keine Werbung. Komplett offline. Keine Datenerfassung. GPL-3.0.**

Quelle der Analyse: LEGCHANCE-Report „Blitzlesen: Das Original" (Google Doc, 25.07.2026).

## Rahmen
- **Name:** Sichtwort · **Domain:** sichtwort.com (Stand 25.07.2026 frei, Registrierung durch Mario)
- **Bundle-ID:** at.legasthenie.sichtwort · Apple Team FQZ492F2YC
- **Plattform:** iOS/iPadOS 16+, SwiftUI, Universal (iPhone+iPad). Android-Port = Phase 2.
- **Repo:** github.com/dyslexics/sichtwort (GPL-3.0)
- **Branding:** EÖDL, Primärfarbe #264398, Tropfen-Logo im Info-Bereich, „Ein Projekt des EÖDL",
  Verweis legasthenie.at. Maskottchen: blauer Käfer (Figuren-Sheet von Mario, 9 Posen).

## Kernmechanik (wie Original, gefixt)
1. **Blitz-Darbietung:** Wort erscheint für einstellbare Zeit — **0,02 s bis 5,0 s**
   (Original max. 2 s = Kritikpunkt). Wiederholen-Button zeigt exakt die eingestellte Dauer
   (Original-Bug: Wiederholung zu kurz).
2. **Lehrer:innen-Modus:** Begleitperson bewertet per grünem/rotem Button, steuert Tempo.
3. **Alleine-Modus:** Kind tippt Wort; tolerante Prüfung (Groß-/Kleinschreibung egal),
   automatisches Leeren/Weiterspringen (Original-Kritik: „muss selbst löschen").
4. **Rundengröße:** 5–40 Wörter. Eigene Listen: feste Reihenfolge ODER Zufall; ein Durchlauf
   garantiert alle Wörter der Liste (Original-Kritik).

## Verbesserungen gegenüber dem Original
- **TTS:** AVSpeechSynthesizer (on-device, offline) spricht das Wort nach dem Aufblitzen /
  auf Knopfdruck. Größte funktionale Lücke des Originals.
- **Silbenvisualisierung:** optional Silben farbig alternierend oder dynamisch nacheinander
  aufleuchtend. Silbendaten stecken in den Wortlisten (word = "Fen-ster" Trennmarken).
- **Schriftwahl:** System, OpenDyslexic, Lexend (beide OFL/frei) + Schriftgrößen-Regler.
  Löst das „kleines l vs. großes I"-Problem aus den Rezensionen.
- **Adaptiver Modus („Abenteuer"):** Aufblitzzeit sinkt/Wortlänge steigt bei Erfolg,
  wird leichter bei Fehlern. Manueller Modus bleibt Standard.
- **Fehler-Wiedervorlage (Leitner-light):** falsch gelesene Wörter kommen in den nächsten
  Runden automatisch wieder; Fehlerhistorie pro Profil.
- **Mehrkind-Profile:** mehrere Kinder pro Gerät, je Fortschritt/Statistik/Listen,
  ohne Accounts, alles lokal.
- **CSV-Import UND -Export** (Export fehlt im Original).
- **Sprache pro Wortliste** explizit DE/EN (nicht an Systemsprache gekoppelt —
  historischer Haupt-Bug des Originals). Schalter Schweizer Rechtschreibung (ss statt ß,
  Laufzeit-Transformation).
- **iPad sauber:** Querformat, Split View, externes Display als explizite Testfälle
  (Layout-Bugs des Originals).
- **Barrierefreiheit:** VoiceOver-Labels, Dynamic Type, Kontrast; im Store dokumentiert.

## Inhalte (alle gratis)
- DE Grundwortschatz 500 + 1000 häufigste Wörter; Filter Wortart (Nomen/Verb/Adjektiv/sonstige)
  und Silbenzahl (1/2/3+).
- EN Sight Words: Dolch (220 + Nomen) und Fry (gemeinfrei).
- 8 Themenlisten (beim Original kostenpflichtig, hier gratis, eigene Zusammenstellung):
  Silbenwörter, Dehnungs-h, ei/ie, Doppelkonsonanten, sch, sp/st, d/t, Weltraum.
- Eigene Listen: unbegrenzt, CSV-Import/-Export, umbenennen, sortieren.

## Belohnung & Maskottchen
- Sterne pro Runde → schalten die 9 Käfer-Posen + Hintergrund-Welten frei; danach endloses
  Level-System mit steigenden Zielen (Original-Kritik: „Belohnungspool läuft leer").
- Posen-Zuordnung: winkend=Home · laufend=Rundenstart · jubelnd=„Richtig!" ·
  tanzend=Rundenabschluss · lesend=Wortlisten · Tafel=Einstellungen/Lernbereich ·
  Glühbirne=Tipps/Hilfe · Hanteln=Statistik · Maler:in=Hintergrund-Auswahl.

## Technik
- SwiftUI, iOS 16+, Persistenz: JSON-Dateien in Application Support (Profile, Listen,
  Fortschritt) — bewusst kein SwiftData (iOS-16-Kompatibilität), kein Backend, kein Tracking.
- Privacy-Label: DATA_NOT_COLLECTED. ITSAppUsesNonExemptEncryption=false.
- Launch-Arg-Hooks ab Tag 1: -tab, -demoData, -screen, -lang (Screenshots/Video-Pipeline).
- Lokalisierung DE/EN (Localizable.xcstrings), UI-Standard Deutsch.

## Bewusst weggelassen (YAGNI)
Accounts/Cloud-Sync, Klassenverwaltung, Spracherkennung/KI, Game Center,
Bild-Wort-Zuordnung, Pseudowörter-Fertigliste (über eigene Listen abbildbar).

## Erfolgskriterien
- Simulator-Build grün, TestFlight-Build bei Mario, Review-Submission ohne Debug-Reste.
- Alle Original-Kritikpunkte im Store-Text adressierbar („Was Sichtwort anders macht").
