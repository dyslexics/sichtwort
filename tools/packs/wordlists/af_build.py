# -*- coding: utf-8 -*-
"""Baut af500.json aus af_raw.py: dedupe -> trim auf 500 -> Silbentrennung -> Validierung."""
import json, collections, sys
import af_raw

# Weniger essenzielle Woerter, die auf dem Weg von 682 -> 500 rausfallen.
DROP = set("""
onse waarheen waarom rondom saggies hardop regtig verder byna skielik hoewel sodat
terwyl sommige selfde mekaar dertien dertig duisend eerste laaste twintig u joune syne
verkoop betaal eindig borsel kam uittrek waai proe oefen verf plak vou pak dek vee
skoonmaak herhaal tik klop lek gaap wakker opstaan wegloop terugkom knip
ronde sagte wonderlik belangrik ernstig helder blink smal wyd veilig jammer dapper
bitter gesond dors hartseer vroeg laat diep stout
bakker koning buurman niggie neef
nommer reël pouse toets liniaal gom
trap kombers mat rak spieël kers horlosie besem emmer mandjie boks foto
brug mark wêreld biblioteek
renoster seekoei kameelperd sebra jakkals wolf luiperd dolfyn akkedis krap wurm
kuiken haan kraai duif uil veer poot
perske aarbei peer ui pampoen ertjie boontjie heuning middagete aandete ketel pan pot
peper slaai rys koffie tee
elmboog stem wang lip duim maag vel bloed toon
das knoop handskoen romp pet
saad wortels dou mis skaduwee donder blits hout ys
speelding sent rand koerant fluit trommel vlieër kroon swaard wa kaart brief
herfs lente fees minuut
polisie boer geskenk ballon vakansie hospitaal vlerk stert kussing
""".split())

# 1) dedupe, erste Nennung gewinnt
seen = {}
order = []
for w, t in af_raw.WORDS:
    if w not in seen:
        seen[w] = t
        order.append(w)

unknown = DROP - set(order)
if unknown:
    sys.exit("DROP enthaelt unbekannte Woerter: %s" % sorted(unknown))

words = [(w, seen[w]) for w in order if w not in DROP]
if len(words) != 500:
    sys.exit("Nach Trim: %d Woerter (erwartet 500)" % len(words))

# 2) Silbentrennung
import pyphen
dic = pyphen.Pyphen(lang="af_ZA")
MANUAL = {
    "asseblief": "as-se-blief",
    "venster": "vens-ter",
    "dikwels": "dik-wels",
    "totsiens": "tot-siens",
    "môre": "mô-re",
    "verjaarsdag": "ver-jaars-dag",
    "onderwyser": "on-der-wy-ser",
    "reënboog": "reën-boog",
    "spinnekop": "spin-ne-kop",
    "aartappel": "aar-tap-pel",
    "sjokolade": "sjo-ko-la-de",
    "huiswerk": "huis-werk",
    "slaapkamer": "slaap-ka-mer",
    "badkamer": "bad-ka-mer",
    "hardloop": "hard-loop",
    "oopmaak": "oop-maak",
    "toemaak": "toe-maak",
    "aantrek": "aan-trek",
    "handdoek": "hand-doek",
    "vliegtuig": "vlieg-tuig",
    "skilpad": "skil-pad",
    "roomys": "room-ys",
}

out = []
hyph = 0
for w, t in words:
    if w in MANUAL:
        s = MANUAL[w]
    else:
        s = dic.inserted(w)
    if s.replace("-", "") != w:      # Trennung veraendert das Wort -> ungetrennt lassen
        s = w
    if any(len(p) < 2 for p in s.split("-")):
        s = w
    if "-" in s:
        hyph += 1
    out.append([s, t])

data = {
    "id": "af500",
    "language": "af",
    "nameDE": "Grundwortschatz Afrikaans",
    "nameEN": "Afrikaans basic vocabulary",
    "words": out,
}
path = "/home/mario/sichtwort/tools/packs/wordlists/af500.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

# 3) Validierung
with open(path, encoding="utf-8") as f:
    d = json.load(f)
assert d["id"] == "af500" and d["language"] == "af"
ws = d["words"]
assert len(ws) == 500, len(ws)
plain = [x[0].replace("-", "") for x in ws]
assert len(set(plain)) == 500, "Duplikate: %s" % [k for k, v in collections.Counter(plain).items() if v > 1]
orig = dict(words)
for (s, t), p in zip(ws, plain):
    assert p == p, p
    assert p in orig and orig[p] == t, (s, t)
    assert t in "nvao" and len(t) == 1
    assert not s.startswith("-") and not s.endswith("-") and "--" not in s
    assert "'" not in s and " " not in s
c = collections.Counter(t for _, t in ws)
print("OK af 500 Woerter, %d mit Silbentrennung, n=%d v=%d a=%d o=%d"
      % (hyph, c["n"], c["v"], c["a"], c["o"]))
