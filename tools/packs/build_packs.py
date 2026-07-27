#!/usr/bin/env python3
"""Baut .swpack-Sprachpakete für Sichtwort.
Format: b"SWPK" + UInt32LE version + UInt32LE indexLen + Index-JSON + mp3-Blob.
Index: {"list": <Wortlisten-JSON>, "voice": "<Anzeigename>", "clips": {wort: [offset, len]}}
Offsets relativ zum Blob-Start (nach dem Index).

Aufruf: build_packs.py <wordlists_dir> <audio_root> <out_dir>
audio_root enthält pro Sprache <code>/ mit <code>_<md5>.mp3.
mx nutzt die es-Liste, br die pt-Liste (nur Stimme anders)."""
import json, os, sys, hashlib, struct

VOICES = {
    "es": "Elvira", "mx": "Dalia", "fr": "Denise", "it": "Elsa", "pt": "Raquel",
    "br": "Francisca", "nl": "Fenna", "da": "Christel", "no": "Pernille",
    "pl": "Zofia", "tr": "Emel", "el": "Athina", "hu": "Noémi", "ro": "Alina",
    "bs": "Vesna", "sq": "Anila", "uk": "Polina", "ar": "Zariyah", "af": "Adri",
}
NAMES = {
    "mx": ("Grundwortschatz Spanisch (Mexiko)", "Spanish (Mexico) basic vocabulary"),
    "br": ("Grundwortschatz Portugiesisch (Brasilien)", "Portuguese (Brazil) basic vocabulary"),
}
DERIVED = {"mx": "es", "br": "pt"}
MANIFEST_NAMES = {
    "es": ("Spanisch", "Spanish"), "mx": ("Spanisch (Mexiko)", "Spanish (Mexico)"),
    "fr": ("Französisch", "French"), "it": ("Italienisch", "Italian"),
    "pt": ("Portugiesisch", "Portuguese"), "br": ("Portugiesisch (Brasilien)", "Portuguese (Brazil)"),
    "nl": ("Niederländisch", "Dutch"), "da": ("Dänisch", "Danish"),
    "no": ("Norwegisch", "Norwegian"), "pl": ("Polnisch", "Polish"),
    "tr": ("Türkisch", "Turkish"), "el": ("Griechisch", "Greek"),
    "hu": ("Ungarisch", "Hungarian"), "ro": ("Rumänisch", "Romanian"),
    "bs": ("BKS (Bosnisch/Kroatisch/Serbisch)", "Bosnian/Croatian/Serbian"),
    "sq": ("Albanisch", "Albanian"), "uk": ("Ukrainisch", "Ukrainian"),
    "ar": ("Arabisch", "Arabic"), "af": ("Afrikaans", "Afrikaans"),
}
ORDER = ["es","mx","fr","it","pt","br","nl","da","no","pl","tr","el","hu","ro","bs","sq","uk","ar","af"]

def md5(w): return hashlib.md5(w.encode("utf-8")).hexdigest()

def build(code, wl_dir, audio_root, out_dir):
    src = DERIVED.get(code, code)
    wl = json.load(open(os.path.join(wl_dir, f"{src}500.json")))
    if code != src:
        wl = dict(wl)
        wl["id"] = f"{code}500"
        wl["language"] = code
        wl["nameDE"], wl["nameEN"] = NAMES[code]
    else:
        wl["language"] = code
    adir = os.path.join(audio_root, code)
    clips, blob, missing = {}, bytearray(), []
    for syl, typ in wl["words"]:
        w = syl.replace("-", "")
        f = os.path.join(adir, f"{code}_{md5(w)}.mp3")
        if not os.path.exists(f):
            missing.append(w); continue
        d = open(f, "rb").read()
        clips[w] = [len(blob), len(d)]
        blob.extend(d)
    # Buchstabennamen fürs Buchstabieren (Easy Reading), seit Paket-Version 2.
    letters = sorted({ch for syl, _ in wl["words"]
                      for ch in syl.replace("-", "").lower() if ch.isalpha()})
    for l in letters:
        if l in clips:
            continue
        f = os.path.join(adir, f"{code}_{md5(l)}.mp3")
        if not os.path.exists(f):
            missing.append(l); continue
        d = open(f, "rb").read()
        clips[l] = [len(blob), len(d)]
        blob.extend(d)
    index = json.dumps({"list": wl, "voice": VOICES[code], "clips": clips},
                       ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    out = os.path.join(out_dir, f"{code}.swpack")
    with open(out, "wb") as fh:
        fh.write(b"SWPK")
        fh.write(struct.pack("<I", 1))
        fh.write(struct.pack("<I", len(index)))
        fh.write(index)
        fh.write(bytes(blob))
    size = os.path.getsize(out)
    print(f"{code}: {len(clips)} Clips, {len(missing)} fehlend, {size/1e6:.2f} MB" +
          (f" MISSING={missing[:5]}" if missing else ""))
    return {"code": code, "nameDE": MANIFEST_NAMES[code][0], "nameEN": MANIFEST_NAMES[code][1],
            "voice": VOICES[code], "sizeMB": round(size / 1e6, 1), "version": 2}, len(missing)

if __name__ == "__main__":
    wl_dir, audio_root, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(out_dir, exist_ok=True)
    manifest, bad = [], 0
    for code in ORDER:
        m, miss = build(code, wl_dir, audio_root, out_dir)
        manifest.append(m)
        bad += miss
    json.dump(manifest, open(os.path.join(out_dir, "manifest.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"FERTIG, {bad} fehlende Clips gesamt")
    sys.exit(1 if bad else 0)
