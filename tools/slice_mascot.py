#!/usr/bin/env python3
"""Schneidet das Maskottchen-Sheet in Einzelposen mit transparentem Hintergrund."""
import sys
import numpy as np
from PIL import Image

SRC = sys.argv[1]
OUT = sys.argv[2]

img = Image.open(SRC).convert("RGBA")
a = np.array(img)

# Nur randverbundenes Nahezu-Weiß wird transparent (Augenweiß bleibt!)
rgb = a[..., :3].astype(int)
lightness = rgb.min(axis=2)
near_white = lightness > 235
# Flood-Fill vom Rand: iterative Nachbar-Ausbreitung innerhalb near_white
mask_bg = np.zeros_like(near_white)
mask_bg[0, :] = near_white[0, :]
mask_bg[-1, :] = near_white[-1, :]
mask_bg[:, 0] = near_white[:, 0]
mask_bg[:, -1] = near_white[:, -1]
while True:
    grown = mask_bg.copy()
    grown[1:, :] |= mask_bg[:-1, :]
    grown[:-1, :] |= mask_bg[1:, :]
    grown[:, 1:] |= mask_bg[:, :-1]
    grown[:, :-1] |= mask_bg[:, 1:]
    grown &= near_white
    if (grown == mask_bg).all():
        break
    mask_bg = grown
alpha = np.where(mask_bg, 0, 255).astype(np.uint8)
a[..., 3] = alpha

content = alpha > 0
# Zeilen mit Inhalt -> Zeilenbänder finden
row_has = content.any(axis=1)
rows = []
in_band = False
for y, v in enumerate(row_has):
    if v and not in_band:
        start = y; in_band = True
    elif not v and in_band:
        if y - start > 100:  # Mini-Bänder ignorieren
            rows.append((start, y))
        in_band = False
if in_band:
    rows.append((start, len(row_has)))
print("Zeilenbänder:", rows)

names_by_row = {
    0: ["laufend", "jubelnd", "tafel", "gluehbirne"],
    1: ["winkend", "lesend", "tanzend", "hanteln", "malerin"],
}

for ri, (y0, y1) in enumerate(rows):
    band = content[y0:y1]
    col_has = band.any(axis=0)
    cols = []
    in_c = False
    for x, v in enumerate(col_has):
        if v and not in_c:
            cs = x; in_c = True
        elif not v and in_c:
            if x - cs > 60:
                cols.append((cs, x))
            in_c = False
    if in_c:
        cols.append((cs, len(col_has)))
    print(f"Band {ri}: {len(cols)} Spalten:", cols)
    names = names_by_row.get(ri, [])
    for ci, (x0, x1) in enumerate(cols):
        name = names[ci] if ci < len(names) else f"row{ri}_col{ci}"
        pad = 8
        crop = a[max(0, y0-pad):min(a.shape[0], y1+pad), max(0, x0-pad):min(a.shape[1], x1+pad)]
        # Auf tatsächlichen Inhalt trimmen
        cmask = crop[..., 3] > 0
        ys, xs = np.where(cmask)
        crop = crop[ys.min():ys.max()+1, xs.min():xs.max()+1]
        Image.fromarray(crop).save(f"{OUT}/{name}.png")
        print(f"  -> {name}.png {crop.shape[1]}x{crop.shape[0]}")
