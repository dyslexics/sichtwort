# -*- coding: utf-8 -*-
"""Trim-Liste: weniger zentrale Eintraege, die aus hu_raw.WORDS entfernt werden,
um exakt 500 Woerter zu erhalten."""

DROP = [
    # Funktionswoerter / Zahlen
    "belül", "kívül", "mindenhol", "sehol", "valahol", "hurrá", "igazán", "rögtön",
    "velem", "vele", "nappal", "éjjel",
    "tizenegy", "harminc", "negyven", "ötven", "hatvan", "hetven", "nyolcvan", "kilencven",
    # Nomen: Schule / Menschen
    "felnőtt", "tanító", "tanuló", "ragasztó", "kréta", "mondat", "vers", "feladat",
    "lecke", "szünet", "hiba",
    # Nomen: Wohnen
    "fürdőszoba", "szőnyeg", "lépcső", "seprű", "párna", "takaró", "udvar", "tükör",
    # Nomen: Essen
    "körte", "szőlő", "dinnye", "uborka", "hagyma", "paradicsom", "kávé", "sütemény",
    "fagylalt", "bögre", "ital", "étel", "reggeli", "csoki",
    # Nomen: Tiere
    "birka", "kecske", "kakas", "gólya", "bagoly", "szarvas", "őz", "teknős",
    "hörcsög", "papagáj", "delfin", "katica", "légy", "veréb", "sün", "lepke",
    # Nomen: Koerper
    "váll", "csont", "könny",
    # Nomen: Natur
    "vihar", "patak", "domb", "rét", "mag", "gyökér", "sár", "levegő",
    # Nomen: Zeit
    "perc", "délután", "húsvét", "ünnep", "hónap",
    # Nomen: Stadt / Verkehr
    "falu", "posta", "villamos", "motor", "kerék", "gyógyszer", "pék", "játszótér",
    # Nomen: Kleidung
    "pulóver", "gomb", "zseb", "sál",
    # Nomen: Sonstiges
    "rádió", "televízió", "forma", "pont", "vonal", "mosoly", "csók", "öröm",
    "erő", "baj", "csoport", "munka", "kör",
    # Verben
    "virágzik", "csipog", "nyávog", "simogat", "öntöz", "varr", "söpör", "világít", "gurul", "visel", "fogad", "emlékszik", "remél", "sikerül",
    "késik", "javít", "tol", "suttog", "csúszik",
    # Adjektive
    "bátortalan", "büszke", "éles", "egészséges", "gazdag", "szegény", "olcsó",
    "drága", "igaz", "biztos", "más", "egész", "utolsó", "késő", "kész", "görbe",
    "sima", "fényes", "hűvös", "vizes", "savanyú", "keserű", "szomjas",
    "álmos", "buta", "szorgalmas", "lusta", "keskeny",
    "alacsony", "ezüst", "arany",
]

# Wieder aufgenommen (Auffuellen auf exakt 500):
# mutat, választ, ébred, fürdik, gyűjt, emel, takarít, ölel, felejt, nyugodt, mérges, egyenes, gyümölcs, zöldség
