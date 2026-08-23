#!/usr/bin/env python3
"""Sichtwort: Wort-Clips mit edge-tts vertonen (Deutsch, Englisch, Sprachpakete).

Technik (aus STIMMEN/gen-de/seraphina_v2.py): Woerter als Komma-Liste im Batch
sprechen - das verhindert die Anglisierung isolierter Woerter bei den
*MultilingualNeural-Stimmen - und das Ergebnis per silencedetect zerschneiden.
Stimmt die Segmentzahl nicht, wird der Batch rekursiv halbiert.

Ausgabe: <prefix><md5(wort)>.mp3, 24 kHz mono 64 kbit/s.
md5 statt Klartext wegen Case-Kollisionen (Weg/weg) auf case-insensitiven FS.

Resumable: vorhandene Dateien werden uebersprungen (--force ueberschreibt).

Aufrufe:
  tools/gen_word_audio.py de                # 1154 dt. Woerter -> Sources/Resources/Audio/
  tools/gen_word_audio.py de_conrad --letters  # dieselben Woerter + Alphabet mit Conrad (maennlich)
  tools/gen_word_audio.py en_us en_gb       # engl. Listen, beide Akzente
  tools/gen_word_audio.py packs             # alle 19 Paketsprachen -> tools/packs/audio/<code>/
  tools/gen_word_audio.py es fr --jobs 4    # einzelne Paketsprachen
  tools/gen_word_audio.py de --dry-run      # nur zeigen, was fehlt

Danach Pakete bauen:
  tools/packs/build_packs.py tools/packs/wordlists tools/packs/audio <out_dir>

ACHTUNG Seraphina-Buchstaben-Clips (de_<md5(buchstabe)>.mp3) stammen NICHT von
hier, sondern aus /STIMMEN/BUCHSTABIEREN/ bzw. Marios Sprachgenerator
(Tragesatz-Verfahren). Dieses Skript fasst sie nicht an. Conrad-Buchstaben
(de_conrad_...) dagegen schon: die Stimme ist monolingual, Batch reicht.
"""
import argparse, concurrent.futures, glob, hashlib, json, os, re, shutil, subprocess, sys, tempfile, threading

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDGE = os.environ.get("EDGE_TTS", "/opt/legasthenie-videos/venv/bin/edge-tts")
APP_AUDIO = os.path.join(REPO, "Sources", "Resources", "Audio")
APP_LISTS = os.path.join(REPO, "Sources", "Resources", "WordLists")
PACK_LISTS = os.path.join(REPO, "tools", "packs", "wordlists")
PACK_AUDIO = os.path.join(REPO, "tools", "packs", "audio")

# Sprachpakete: Code -> (edge-tts-Stimme, Wortlisten-Quelle)
# mx nutzt die es-Woerter, br die pt-Woerter - nur die Stimme ist anders.
PACKS = {
    "es": ("es-ES-ElviraNeural",   "es"), "mx": ("es-MX-DaliaNeural",     "es"),
    "fr": ("fr-FR-DeniseNeural",   "fr"), "it": ("it-IT-ElsaNeural",      "it"),
    "pt": ("pt-PT-RaquelNeural",   "pt"), "br": ("pt-BR-FranciscaNeural", "pt"),
    "nl": ("nl-NL-FennaNeural",    "nl"), "da": ("da-DK-ChristelNeural",  "da"),
    "no": ("nb-NO-PernilleNeural", "no"), "pl": ("pl-PL-ZofiaNeural",     "pl"),
    "tr": ("tr-TR-EmelNeural",     "tr"), "el": ("el-GR-AthinaNeural",    "el"),
    "hu": ("hu-HU-NoemiNeural",    "hu"), "ro": ("ro-RO-AlinaNeural",     "ro"),
    "bs": ("bs-BA-VesnaNeural",    "bs"), "sq": ("sq-AL-AnilaNeural",     "sq"),
    "uk": ("uk-UA-PolinaNeural",   "uk"), "ar": ("ar-SA-ZariyahNeural",   "ar"),
    "af": ("af-ZA-AdriNeural",     "af"),
}
PACK_ORDER = ["es","mx","fr","it","pt","br","nl","da","no","pl","tr","el","hu","ro","bs","sq","uk","ar","af"]

# App-interne Ziele: Stimme, Dateipraefix, Ausgabeordner, Manifest
APP_TARGETS = {
    "de":        ("de-DE-SeraphinaMultilingualNeural", "de_",        APP_AUDIO, "tools/audio_manifest.json"),
    "de_conrad": ("de-DE-ConradNeural",                "de_conrad_", APP_AUDIO, "tools/_manifest_de_conrad.json"),
    "en_us":     ("en-US-AvaMultilingualNeural",       "en_us_",     APP_AUDIO, "tools/_manifest_en_us.json"),
    "en_gb":     ("en-GB-SoniaNeural",                 "en_gb_",     APP_AUDIO, "tools/_manifest_en_gb.json"),
}

print_lock = threading.Lock()

def log(msg):
    with print_lock:
        print(msg, flush=True)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def md5(w):
    return hashlib.md5(w.encode("utf-8")).hexdigest()


class Target:
    """Ein Vertonungsauftrag: Stimme + Wortliste + Ausgabeordner."""

    def __init__(self, name, voice, prefix, outdir, manifest, words, letters):
        self.name, self.voice, self.prefix = name, voice, prefix
        self.outdir, self.manifest = outdir, manifest
        self.words, self.letters = words, letters
        self.fails = []

    def path(self, word):
        return os.path.join(self.outdir, self.prefix + md5(word) + ".mp3")

    def todo(self, force):
        items = self.words + self.letters
        return items if force else [w for w in items if not os.path.exists(self.path(w))]


def app_words(language):
    """Woerter aller App-Wortlisten einer Sprache, Reihenfolge stabil, ohne Dubletten."""
    seen, out = set(), []
    for f in sorted(glob.glob(os.path.join(APP_LISTS, "*.json"))):
        data = json.load(open(f, encoding="utf-8"))
        if data.get("language") != language:
            continue
        for syl, _typ in data["words"]:
            w = syl.replace("-", "")
            if w not in seen:
                seen.add(w); out.append(w)
    return out


def pack_words(source):
    data = json.load(open(os.path.join(PACK_LISTS, f"{source}500.json"), encoding="utf-8"))
    seen, out = set(), []
    for syl, _typ in data["words"]:
        w = syl.replace("-", "")
        if w not in seen:
            seen.add(w); out.append(w)
    return out


def alphabet(words):
    """Kleinbuchstaben, die in den Woertern vorkommen - genau die sucht build_packs.py."""
    return sorted({ch for w in words for ch in w.lower() if ch.isalpha()})


def build_target(name, with_letters):
    if name in APP_TARGETS:
        voice, prefix, outdir, manifest = APP_TARGETS[name]
        words = app_words("de" if name.startswith("de") else "en" if name.startswith("en_") else name)
        letters = []
        if with_letters:
            if name == "de":
                log("  Hinweis: dt. Buchstaben-Clips kommen aus /STIMMEN/BUCHSTABIEREN/ - uebersprungen.")
            else:
                # Conrad ist monolingual de-DE - Buchstaben gehen im Batch-Verfahren,
                # kein Tragesatz noetig (der galt der multilingualen Seraphina).
                letters = [l for l in alphabet(words) if l not in words]
                if name == "de_conrad":  # volles Alphabet wie der Seraphina-Bestand (q fehlt in den Listen)
                    letters = sorted(set(letters) | set("abcdefghijklmnopqrstuvwxyzäöüß"))
        return Target(name, voice, prefix, outdir, manifest, words, letters)
    if name in PACKS:
        voice, source = PACKS[name]
        words = pack_words(source)
        outdir = os.path.join(PACK_AUDIO, name)
        letters = [l for l in alphabet(words) if l not in words] if with_letters else []
        return Target(name, voice, name + "_", outdir, os.path.join(outdir, "_manifest.json"), words, letters)
    sys.exit(f"Unbekanntes Ziel: {name}. Bekannt: {', '.join(list(APP_TARGETS) + ['packs'] + PACK_ORDER)}")


def segments(wav, noise="-35dB", d="0.15"):
    """Sprechabschnitte (Start, Ende) per ffmpeg-silencedetect."""
    out = run(["ffmpeg", "-i", wav, "-af", f"silencedetect=noise={noise}:d={d}", "-f", "null", "/dev/null"]).stderr
    dm = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    if not dm:
        return []
    dur = int(dm.group(1)) * 3600 + int(dm.group(2)) * 60 + float(dm.group(3))
    ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    segs, speaking, spst = [], True, 0.0
    for t, k in sorted([(t, "s") for t in ss] + [(t, "e") for t in se]):
        if k == "s" and speaking:
            if t - spst > 0.12:
                segs.append((spst, t))
            speaking = False
        elif k == "e" and not speaking:
            spst, speaking = t, True
    if speaking and dur - spst > 0.12:
        segs.append((spst, dur))
    return segs


def tts(voice, text, mp3):
    for attempt in range(4):
        r = run([EDGE, "--voice", voice, "--text", text, "--write-media", mp3])
        if r.returncode == 0 and os.path.exists(mp3) and os.path.getsize(mp3) > 1000:
            return True
        __import__("time").sleep(2 + attempt * 2)
    return False


def emit(target, wav, a, b, word):
    """Segment ausschneiden -> mp3 24k mono 64k, atomar per .tmp + rename."""
    out = target.path(word)
    tmp = out + ".part.mp3"  # Endung .mp3 noetig, ffmpeg leitet das Format daraus ab
    r = run(["ffmpeg", "-y", "-ss", f"{max(0, a - 0.06)}", "-to", f"{b + 0.10}", "-i", wav,
             "-ar", "24000", "-ac", "1", "-b:a", "64k", tmp])
    if r.returncode == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 500:
        os.replace(tmp, out)
        return True
    if os.path.exists(tmp):
        os.remove(tmp)
    return False


def process(target, batch, tmpdir):
    """Einen Batch sprechen und zerschneiden; bei Segment-Mismatch rekursiv halbieren."""
    tag = md5("|".join(batch))[:10]
    mp3, wav = os.path.join(tmpdir, f"b{tag}.mp3"), os.path.join(tmpdir, f"b{tag}.wav")
    text = ", ".join(batch) + "." if len(batch) > 1 else batch[0] + "."
    try:
        if not tts(target.voice, text, mp3):
            target.fails.extend([(w, "tts") for w in batch]); return
        run(["ffmpeg", "-y", "-i", mp3, "-ar", "44100", "-ac", "1", wav])
        segs = segments(wav)
        if len(segs) != len(batch):
            segs = segments(wav, noise="-30dB", d="0.22")
        if len(segs) != len(batch):
            if len(batch) == 1:
                # Einzelwort: gesamtes Audio getrimmt nehmen (Verschlusslaute haben
                # Stille MITTEN im Wort - erstes bis letztes Segment, nicht nur eins).
                allsegs = segments(wav)
                if allsegs and emit(target, wav, allsegs[0][0], allsegs[-1][1], batch[0]):
                    return
                target.fails.append((batch[0], "seg1")); return
            mid = len(batch) // 2
            process(target, batch[:mid], tmpdir)
            process(target, batch[mid:], tmpdir)
            return
        for (a, b), w in zip(segs, batch):
            if not emit(target, wav, a, b, w):
                target.fails.append((w, "emit"))
    finally:
        for f in (mp3, wav):
            if os.path.exists(f):
                os.remove(f)


def generate(target, batchsize, jobs, force, dry, limit=0):
    todo = target.todo(force)
    if limit:
        todo = todo[:limit]
    have = len(target.words) + len(target.letters) - len(target.todo(False))
    log(f"[{target.name}] {target.voice}")
    log(f"[{target.name}] {len(target.words)} Woerter + {len(target.letters)} Buchstaben, "
        f"{have} vorhanden, {len(todo)} zu erzeugen -> {target.outdir}")
    if dry:
        log(f"[{target.name}] dry-run, Beispiele: {todo[:8]}")
        return 0
    if not todo:
        write_manifest(target)
        return 0
    os.makedirs(target.outdir, exist_ok=True)
    tmpdir = tempfile.mkdtemp(prefix=f"sichtwort-{target.name}-")
    batches = [todo[i:i + batchsize] for i in range(0, len(todo), batchsize)]
    done = 0
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
            futures = [pool.submit(process, target, b, tmpdir) for b in batches]
            for fut in concurrent.futures.as_completed(futures):
                fut.result()
                done += 1
                if done % 10 == 0 or done == len(batches):
                    log(f"[{target.name}] {done}/{len(batches)} Batches")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    scope = todo if limit else target.words + target.letters
    missing = [w for w in scope if not os.path.exists(target.path(w))]
    write_manifest(target)
    log(f"[{target.name}] FERTIG. Fehlend: {len(missing)} {missing[:20]}")
    if target.fails:
        log(f"[{target.name}] Fails: {target.fails[:20]}")
    return len(missing)


def write_manifest(target):
    path = target.manifest if os.path.isabs(target.manifest) else os.path.join(REPO, target.manifest)
    data = {w: os.path.basename(target.path(w)) for w in target.words + target.letters
            if os.path.exists(target.path(w))}
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", default=["de"],
                    help="de | en_us | en_gb | packs | einzelne Paketcodes (es fr ...). Standard: de")
    ap.add_argument("--batch", type=int, default=8, help="Woerter pro TTS-Aufruf (Standard 8)")
    ap.add_argument("--jobs", type=int, default=4, help="parallele TTS-Auftraege (Standard 4)")
    ap.add_argument("--letters", action="store_true",
                    help="zusaetzlich Buchstaben-Clips (Paketsprachen brauchen die fuers Buchstabieren)")
    ap.add_argument("--force", action="store_true", help="vorhandene Clips neu erzeugen")
    ap.add_argument("--limit", type=int, default=0, help="nur die ersten N fehlenden Clips (Test)")
    ap.add_argument("--dry-run", action="store_true", help="nur zeigen, was fehlt")
    args = ap.parse_args()

    if not os.path.exists(EDGE):
        sys.exit(f"edge-tts nicht gefunden: {EDGE} (via EDGE_TTS ueberschreibbar)")
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg nicht gefunden")

    names = []
    for t in (args.targets or ["de"]):
        names.extend(PACK_ORDER if t == "packs" else [t])

    bad = 0
    for name in names:
        bad += generate(build_target(name, args.letters), args.batch, args.jobs,
                        args.force, args.dry_run, args.limit)
    if bad:
        log(f"GESAMT: {bad} fehlende Clips - Skript nochmal laufen lassen (es ist resumable).")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
