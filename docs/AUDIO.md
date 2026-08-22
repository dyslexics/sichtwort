# Audio: wie die Sprachclips entstehen

Alle Clips kommen von **edge-tts** (Microsoft Neural Voices), werden zugeschnitten
und als `<prefix><md5(wort)>.mp3` abgelegt — 24 kHz mono, 64 kbit/s.
md5 statt Klartext, weil `Weg` und `weg` sonst auf case-insensitiven Dateisystemen
dieselbe Datei wären.

Abgespielt wird in `Sources/Engine/Speech.swift` per `AVAudioPlayer`
(Session `.playback`); Fallback für eigene Wortlisten ist `AVSpeechSynthesizer`.

## 1. Wort-Clips — `tools/gen_word_audio.py`

```bash
tools/gen_word_audio.py de                 # 1154 dt. Wörter  -> Sources/Resources/Audio/de_<md5>.mp3
tools/gen_word_audio.py en_us en_gb        # 420 engl. Wörter je Akzent -> en_us_/en_gb_<md5>.mp3
tools/gen_word_audio.py packs --letters    # 19 Paketsprachen -> tools/packs/audio/<code>/<code>_<md5>.mp3
tools/gen_word_audio.py es fr --letters    # einzelne Paketsprachen
tools/gen_word_audio.py de --dry-run       # nur zeigen, was fehlt
```

Optionen: `--batch` (Wörter pro TTS-Aufruf, Standard 8), `--jobs` (parallel, Standard 4),
`--force` (vorhandene neu erzeugen), `--limit N` (Testlauf), `--letters`.

Die Wortliste wird direkt aus den JSON-Dateien gelesen — deutsch/englisch aus
`Sources/Resources/WordLists/`, Paketsprachen aus `tools/packs/wordlists/<code>500.json`.
Es gibt keine separate Wortdatei mehr, die veralten kann.

### Der Trick: Batch statt Einzelwort

`de-DE-SeraphinaMultilingualNeural` erkennt die Sprache am Text. Ein einzelnes kurzes
Wort ohne Kontext kippt ins Englische. Deshalb werden **8 Wörter als Komma-Liste in
einem Aufruf** gesprochen (`"Fenster, Haus, Baum, …"`) und danach zerschnitten:

1. mp3 → wav 44,1 kHz mono
2. `ffmpeg silencedetect=noise=-35dB:d=0.15`, Fallback `-30dB:d=0.22`
3. Segmentzahl ≠ Batchgröße → **Batch rekursiv halbieren**; bei einem Einzelwort als
   letzter Ausweg das ganze getrimmte Audio nehmen
4. Schnittkanten mit Polster −0,06 s / +0,10 s

Wichtig beim Zuschnitt: Verschlusslaute („Zett", „Eff", „Iks") haben bis 250 ms Stille
**mitten im Wort**. Immer vom ersten bis zum letzten Segment schneiden, nie nur das
letzte nehmen — sonst bleibt bloß das /t/ übrig.

Das Skript ist **resumable**: vorhandene Dateien werden übersprungen, Zwischendateien
liegen in einem temporären Verzeichnis und werden aufgeräumt. Nach dem Lauf steht in
`tools/audio_manifest.json` bzw. `tools/_manifest_en_*.json` die Zuordnung Wort → Datei.

### Stimmen

| Ziel | Stimme |
|------|--------|
| `de` | de-DE-SeraphinaMultilingualNeural (Marios Favorit) |
| `en_us` / `en_gb` | en-US-AvaMultilingualNeural / en-GB-SoniaNeural |
| Pakete | Elvira, Dalia, Denise, Elsa, Raquel, Francisca, Fenna, Christel, Pernille, Zofia, Emel, Athina, Noémi, Alina, Vesna, Anila, Polina, Zariyah, Adri |

`mx` benutzt die spanischen Wörter mit Dalia, `br` die portugiesischen mit Francisca.

## 2. Buchstaben-Clips

**Deutsch kommt NICHT aus diesem Skript.** Die 30 deutschen Buchstabennamen sind im
„deutlich"-Stil auf H15 entstanden (`/var/www/html/STIMMEN/BUCHSTABIEREN/`, ab Build 18
aus dem Sprachgenerator `/STIMMEN/GENERATOR/`) und liegen als `de_<md5(kleinbuchstabe)>.mp3`
im Audio-Ordner. `gen_word_audio.py de --letters` fasst sie bewusst nicht an.

Grund: Einzelne kurze Tokens kippen bei der multilingualen Stimme ins Englische
(„Bee" → /biː/). Dort hilft nur der **Tragesatz** („Wir lernen jetzt das deutsche
Alphabet. Weh.") mit Schnitt am `SentenceBoundary`-Event plus RMS-Hüllkurve.

Für die Paketsprachen sind die Stimmen monolingual, dort genügt `--letters`
mit demselben Batch-Verfahren.

## 3. Sprachpakete bauen

```bash
tools/gen_word_audio.py packs --letters
tools/packs/build_packs.py tools/packs/wordlists tools/packs/audio /pfad/zu/packs
rsync -av /pfad/zu/packs/ web105@s178.goserver.host:~/www/sichtwort.com/packs/
```

`.swpack` = `SWPK` + UInt32LE Version + UInt32LE Indexlänge + Index-JSON + mp3-Blob.
`tools/packs/audio/` ist Zwischenmaterial und steht in `.gitignore`.

## Voraussetzungen

* `edge-tts` unter `/opt/legasthenie-videos/venv/bin/edge-tts` (per `EDGE_TTS=` überschreibbar)
* `ffmpeg` / `ffprobe` im Pfad

## Qualitätssicherung

Whisper taugt für die **Zuordnung** (sitzt der richtige Clip auf dem richtigen Wort),
nicht als Urteil über die Aussprache — bei Buchstabenketten erkennt es selbst korrekte
deutsche Namen nur zu 14/30. Abnahme läuft über die Abhörseite
`https://h15.drcag.com/SICHTWORT-AUDIO/`.
