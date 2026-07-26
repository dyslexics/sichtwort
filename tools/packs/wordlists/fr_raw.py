# -*- coding: utf-8 -*-
# Grundwortschatz Franzoesisch fuer Sichtwort (Blitzlesen, 6-10 Jahre)
# Feld 1: Wort (Kleinschreibung, keine Apostroph-Formen, keine Bindestriche)
# Feld 2: n=Nomen v=Verb a=Adjektiv o=Sonstiges
# Zielverteilung: o=150, n=205, v=90, a=55  -> 500

FUNC = [
    "le", "la", "les", "un", "une",
    "des", "de", "du", "au", "aux",
    "ce", "cet", "cette", "ces", "mon",
    "ma", "mes", "ton", "ta", "tes",
    "son", "sa", "ses", "notre", "nos",
    "votre", "vos", "leur", "leurs", "je",
    "tu", "il", "elle", "on", "nous",
    "vous", "ils", "elles", "me", "te",
    "se", "moi", "toi", "lui", "eux",
    "qui", "que", "quoi", "quel", "quelle",
    "chaque", "tout", "tous", "toute", "toutes",
    "autre", "rien", "en", "y", "et",
    "ou", "mais", "donc", "car", "si",
    "quand", "comme", "parce", "pour", "par",
    "avec", "sans", "sous", "sur", "dans",
    "chez", "vers", "entre", "contre", "depuis",
    "pendant", "avant", "après", "devant", "derrière",
    "près", "loin", "ici", "oui", "non",
    "ne", "pas", "plus", "moins", "très",
    "trop", "peu", "beaucoup", "assez", "encore",
    "toujours", "jamais", "souvent", "maintenant", "hier",
    "demain", "bientôt", "alors", "aussi", "puis",
    "ensuite", "comment", "pourquoi", "combien", "voici",
    "voilà", "merci", "bonjour", "salut", "pardon",
    "vite", "bien", "mal", "mieux", "ensemble",
    "dehors", "partout", "presque", "vraiment", "déjà",
    "zéro", "deux", "trois", "quatre", "cinq",
    "six", "sept", "huit", "neuf", "dix",
    "onze", "douze", "treize", "quatorze", "quinze",
    "seize", "vingt", "trente", "cent", "mille",
]

NOUNS = [
    # Familie und Menschen
    "famille", "papa", "maman", "père", "mère",
    "parents", "frère", "sœur", "bébé", "enfant",
    "fille", "garçon", "ami", "tante", "oncle",
    "homme", "femme",
    # Schule
    "école", "classe", "maître", "maîtresse", "élève",
    "cahier", "livre", "crayon", "stylo", "gomme",
    "règle", "feuille", "mot", "lettre", "phrase",
    "histoire", "image", "couleur", "papier", "leçon",
    # Spiel und Freizeit
    "jeu", "jouet", "ballon", "poupée", "vélo",
    "musique", "sport", "vacances", "fête",
    # Tiere
    "animal", "chien", "chat", "oiseau", "poisson",
    "cheval", "vache", "cochon", "poule", "canard",
    "lapin", "souris", "loup", "renard", "ours",
    "lion", "éléphant", "serpent", "grenouille", "papillon",
    "abeille",
    # Essen, Trinken, Geschirr
    "pain", "lait", "eau", "jus", "pomme",
    "banane", "fraise", "orange", "tomate", "carotte",
    "salade", "soupe", "riz", "fromage", "beurre",
    "gâteau", "bonbon", "chocolat", "sucre", "sel",
    "viande", "poulet", "œuf", "glace", "cuisine",
    "assiette", "verre", "cuillère", "fourchette", "couteau",
    # Koerper
    "corps", "tête", "cheveux", "visage", "œil",
    "yeux", "nez", "bouche", "dent", "oreille",
    "bras", "main", "doigt", "dos", "jambe",
    "pied", "cœur",
    # Kleidung
    "vêtement", "robe", "jupe", "pantalon", "pull",
    "manteau", "chaussure", "chaussette", "chapeau",
    # Haus
    "maison", "chambre", "salon", "jardin", "escalier",
    "toit", "porte", "fenêtre", "mur", "clé",
    "lit", "lampe", "bain", "table", "chaise",
    "téléphone", "sac",
    # Natur
    "soleil", "lune", "étoile", "ciel", "nuage",
    "pluie", "neige", "vent", "arbre", "fleur",
    "forêt", "bois", "montagne", "rivière", "lac",
    "mer", "plage", "pierre", "terre", "feu",
    # Zeit
    "jour", "nuit", "matin", "soir", "midi",
    "semaine", "mois", "année", "heure", "temps",
    "printemps", "été", "automne", "hiver", "lundi",
    "mardi", "mercredi", "jeudi", "vendredi", "samedi",
    "dimanche",
    # Stadt, Verkehr, Berufe, Maerchen
    "ville", "village", "rue", "route", "chemin",
    "magasin", "gare", "train", "bus", "voiture",
    "avion", "bateau", "pompier", "police", "docteur",
    "ferme", "roi", "reine", "princesse", "monstre",
    "château", "argent", "idée", "air",
]

VERBS = [
    "être", "avoir", "aller", "faire", "dire",
    "voir", "savoir", "pouvoir", "vouloir", "venir",
    "prendre", "mettre", "donner", "parler", "aimer",
    "jouer", "manger", "boire", "dormir", "courir",
    "marcher", "sauter", "tomber", "lire", "écrire",
    "compter", "chanter", "danser", "rire", "pleurer",
    "crier", "écouter", "regarder", "chercher", "trouver",
    "perdre", "gagner", "ouvrir", "fermer", "monter",
    "descendre", "entrer", "sortir", "rester", "partir",
    "arriver", "rentrer", "porter", "tirer", "pousser",
    "tenir", "toucher", "laver", "ranger", "aider",
    "montrer", "apprendre", "comprendre", "penser", "croire",
    "oublier", "attendre", "appeler", "répondre", "demander",
    "raconter", "dessiner", "couper", "casser", "réparer",
    "acheter", "payer", "vendre", "travailler", "nettoyer",
    "voler", "nager", "grimper", "rouler", "cacher",
    "suivre", "arrêter", "commencer", "finir", "changer",
    "devenir", "vivre", "grandir", "choisir", "passer",
]

ADJS = [
    "grand", "petit", "gros", "long", "court",
    "haut", "beau", "joli", "jeune", "vieux",
    "nouveau", "bon", "mauvais", "gentil", "méchant",
    "content", "heureux", "triste", "sage", "drôle",
    "fort", "rapide", "lent", "chaud", "froid",
    "propre", "sale", "plein", "vide", "lourd",
    "léger", "dur", "doux", "facile", "difficile",
    "malade", "fatigué", "seul", "premier", "ouvert",
    "vrai", "clair", "rond", "fin", "calme",
    # Farben
    "rouge", "bleu", "vert", "jaune", "noir",
    "blanc", "gris", "rose", "violet", "marron",
]

WORDS = (
    [(w, "o") for w in FUNC]
    + [(w, "n") for w in NOUNS]
    + [(w, "v") for w in VERBS]
    + [(w, "a") for w in ADJS]
)
