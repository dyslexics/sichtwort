#!/usr/bin/env python3
"""Sichtwort: alle deutschen Wörter mit Seraphina vertonen.
Technik aus STIMMEN/gen-de/seraphina_v2.py: Komma-Liste sprechen (verhindert
Anglisierung isolierter Wörter), per silencedetect zerschneiden.
Resumable: existierende Ausgabedateien werden übersprungen."""
import json, subprocess, os, re, sys, time, hashlib

EDGE = "/opt/legasthenie-videos/venv/bin/edge-tts"
VOICE = "de-DE-SeraphinaMultilingualNeural"
BASE = "/tmp/claude-1000/-home-mario/6ddd3e09-6073-478d-bfc8-d53b0a7119d9/scratchpad"
OUT = f"{BASE}/word_audio"
TMP = f"{BASE}/wa_tmp"
os.makedirs(OUT, exist_ok=True)
os.makedirs(TMP, exist_ok=True)

def run(c): return subprocess.run(c, capture_output=True, text=True)
def fname(w): return "de_" + hashlib.md5(w.encode("utf-8")).hexdigest() + ".mp3"

def segments(wav, noise="-35dB", d="0.15"):
    out = run(["ffmpeg", "-i", wav, "-af", f"silencedetect=noise={noise}:d={d}", "-f", "null", "/dev/null"]).stderr
    dm = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    dur = int(dm.group(1))*3600 + int(dm.group(2))*60 + float(dm.group(3))
    ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    segs = []
    ev = sorted([(t, 's') for t in ss] + [(t, 'e') for t in se])
    speaking = True; spst = 0.0
    for t, k in ev:
        if k == 's' and speaking:
            if t - spst > 0.12: segs.append((spst, t))
            speaking = False
        elif k == 'e' and not speaking:
            spst = t; speaking = True
    if speaking and dur - spst > 0.12: segs.append((spst, dur))
    return segs

def tts(text, mp3):
    for a in range(4):
        r = run([EDGE, "--voice", VOICE, "--text", text, "--write-media", mp3])
        if r.returncode == 0 and os.path.exists(mp3) and os.path.getsize(mp3) > 1000:
            return True
        time.sleep(2 + a * 2)
    return False

def emit(wav, a, b, word):
    """Segment ausschneiden -> mp3 24k mono 64k"""
    out = os.path.join(OUT, fname(word))
    r = run(["ffmpeg", "-y", "-ss", f"{max(0, a-0.06)}", "-to", f"{b+0.10}", "-i", wav,
             "-ar", "24000", "-ac", "1", "-b:a", "64k", out])
    return r.returncode == 0 and os.path.getsize(out) > 500

fails = []

def process(batch, depth=0):
    """TTS-Batch; bei Segment-Mismatch rekursiv halbieren."""
    tag = hashlib.md5(("|".join(batch)).encode()).hexdigest()[:10]
    mp3 = f"{TMP}/b{tag}.mp3"; wav = f"{TMP}/b{tag}.wav"
    text = ", ".join(batch) + "." if len(batch) > 1 else batch[0] + "."
    if not tts(text, mp3):
        fails.extend([(w, "tts") for w in batch]); return
    run(["ffmpeg", "-y", "-i", mp3, "-ar", "44100", "-ac", "1", wav])
    segs = segments(wav)
    if len(segs) != len(batch):
        segs = segments(wav, noise="-30dB", d="0.22")
    if len(segs) != len(batch):
        if len(batch) == 1:
            # Einzelwort: gesamtes Audio (getrimmt) nehmen
            allsegs = segments(wav)
            if allsegs:
                a = allsegs[0][0]; b = allsegs[-1][1]
                if emit(wav, a, b, batch[0]): return
            fails.append((batch[0], "seg1")); return
        mid = len(batch) // 2
        process(batch[:mid], depth+1)
        process(batch[mid:], depth+1)
        return
    for (a, b), w in zip(segs, batch):
        if not emit(wav, a, b, w):
            fails.append((w, "emit"))

words = json.load(open(f"{BASE}/de_words.json"))
todo = [w for w in words if not os.path.exists(os.path.join(OUT, fname(w)))]
print(f"{len(words)} Wörter, {len(todo)} zu generieren", flush=True)

B = 8
for i in range(0, len(todo), B):
    process(todo[i:i+B])
    done = len(words) - len([w for w in words if not os.path.exists(os.path.join(OUT, fname(w)))])
    if (i // B) % 10 == 0:
        print(f"[{i+B}/{len(todo)}] fertig={done}", flush=True)

missing = [w for w in words if not os.path.exists(os.path.join(OUT, fname(w)))]
print("FERTIG. Fehlend:", len(missing), missing[:20], flush=True)
print("Fails:", fails[:20], flush=True)
# Manifest Wort -> Datei (für Doku/Debug)
json.dump({w: fname(w) for w in words}, open(f"{OUT}/_manifest.json", "w"), ensure_ascii=False, indent=0)
sys.exit(1 if missing else 0)
