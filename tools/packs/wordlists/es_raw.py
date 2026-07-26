# -*- coding: utf-8 -*-
"""Grundwortschatz Spanisch (es) fuer Sichtwort - Blitzlesen, Kinder 6-10.

Genau 500 Woerter des Lese-Erstunterrichts: Funktionswoerter, haeufige Verben,
Alltagsnomen (Familie, Schule, Tiere, Essen, Koerper, Natur, Haus, Kleidung,
Zeit) und Adjektive/Farben.

Typen: n = Nomen, v = Verb, a = Adjektiv, o = Sonstiges (Funktionswoerter,
Zahlen, Adverbien, Praepositionen, Konjunktionen, Interjektionen).
"""

# --- Funktionswoerter, Pronomen, Praepositionen, Konjunktionen, Zahlen ---
FUNCTION = [
    ("el", "o"), ("la", "o"), ("los", "o"), ("las", "o"),
    ("un", "o"), ("una", "o"),
    ("y", "o"), ("o", "o"), ("pero", "o"), ("que", "o"),
    ("de", "o"), ("en", "o"), ("a", "o"), ("con", "o"),
    ("por", "o"), ("para", "o"), ("sin", "o"), ("sobre", "o"),
    ("bajo", "o"), ("entre", "o"), ("hasta", "o"), ("desde", "o"),
    ("hacia", "o"), ("contra", "o"),
    ("yo", "o"), ("tú", "o"), ("él", "o"), ("ella", "o"),
    ("nosotros", "o"), ("ellos", "o"),
    ("me", "o"), ("te", "o"), ("se", "o"), ("nos", "o"),
    ("le", "o"), ("lo", "o"), ("les", "o"), ("mí", "o"), ("ti", "o"),
    ("mi", "o"), ("tu", "o"), ("su", "o"), ("nuestro", "o"),
    ("este", "o"), ("esta", "o"), ("estos", "o"),
    ("ese", "o"), ("esa", "o"), ("esto", "o"), ("eso", "o"),
    ("aquel", "o"),
    ("qué", "o"), ("quién", "o"), ("cuál", "o"), ("cómo", "o"),
    ("cuándo", "o"), ("dónde", "o"),
    ("sí", "o"), ("no", "o"), ("ni", "o"),
    ("también", "o"), ("muy", "o"),
    ("más", "o"), ("menos", "o"), ("mucho", "o"), ("poco", "o"),
    ("todo", "o"), ("todos", "o"), ("nada", "o"), ("nadie", "o"),
    ("algo", "o"), ("alguien", "o"), ("otro", "o"),
    ("tan", "o"), ("casi", "o"), ("siempre", "o"), ("nunca", "o"),
    ("ya", "o"), ("ahora", "o"), ("luego", "o"),
    ("después", "o"), ("antes", "o"), ("pronto", "o"), ("temprano", "o"),
    ("hoy", "o"), ("ayer", "o"), ("aquí", "o"), ("allí", "o"),
    ("cerca", "o"), ("lejos", "o"), ("arriba", "o"), ("abajo", "o"),
    ("dentro", "o"), ("fuera", "o"), ("delante", "o"), ("detrás", "o"),
    ("encima", "o"), ("debajo", "o"),
    ("bien", "o"), ("mal", "o"), ("así", "o"), ("entonces", "o"),
    ("porque", "o"), ("cuando", "o"), ("donde", "o"),
    ("como", "o"), ("si", "o"), ("aunque", "o"), ("mientras", "o"),
    ("uno", "o"), ("dos", "o"), ("tres", "o"), ("cuatro", "o"),
    ("cinco", "o"), ("seis", "o"), ("siete", "o"), ("ocho", "o"),
    ("nueve", "o"), ("diez", "o"), ("once", "o"), ("doce", "o"),
    ("veinte", "o"), ("treinta", "o"), ("cien", "o"), ("mil", "o"),
    ("hola", "o"), ("adiós", "o"), ("gracias", "o"),
]

# --- Verben (Infinitiv) ---
VERBS = [
    ("ser", "v"), ("estar", "v"), ("tener", "v"), ("hacer", "v"),
    ("poder", "v"), ("decir", "v"), ("ir", "v"), ("ver", "v"),
    ("dar", "v"), ("saber", "v"), ("querer", "v"), ("llegar", "v"),
    ("pasar", "v"), ("deber", "v"), ("poner", "v"), ("quedar", "v"),
    ("creer", "v"), ("hablar", "v"), ("llevar", "v"), ("dejar", "v"),
    ("seguir", "v"), ("encontrar", "v"), ("llamar", "v"), ("venir", "v"),
    ("pensar", "v"), ("salir", "v"), ("volver", "v"), ("tomar", "v"),
    ("conocer", "v"), ("vivir", "v"), ("sentir", "v"), ("mirar", "v"),
    ("contar", "v"), ("empezar", "v"), ("esperar", "v"), ("buscar", "v"),
    ("entrar", "v"), ("trabajar", "v"), ("escribir", "v"), ("perder", "v"),
    ("entender", "v"), ("pedir", "v"), ("recibir", "v"), ("terminar", "v"),
    ("sacar", "v"), ("leer", "v"), ("caer", "v"), ("cambiar", "v"),
    ("abrir", "v"), ("cerrar", "v"), ("oír", "v"), ("ganar", "v"),
    ("traer", "v"), ("preguntar", "v"), ("contestar", "v"), ("tocar", "v"),
    ("estudiar", "v"), ("correr", "v"), ("pagar", "v"), ("ayudar", "v"),
    ("gustar", "v"), ("jugar", "v"), ("comer", "v"), ("beber", "v"),
    ("dormir", "v"), ("cantar", "v"), ("bailar", "v"), ("saltar", "v"),
    ("caminar", "v"), ("andar", "v"), ("nadar", "v"), ("volar", "v"),
    ("reír", "v"), ("llorar", "v"), ("gritar", "v"), ("romper", "v"),
    ("limpiar", "v"), ("lavar", "v"), ("cocinar", "v"), ("comprar", "v"),
    ("vender", "v"), ("dibujar", "v"), ("pintar", "v"), ("cortar", "v"),
    ("subir", "v"), ("bajar", "v"), ("empujar", "v"), ("tirar", "v"),
    ("guardar", "v"), ("enseñar", "v"), ("aprender", "v"), ("olvidar", "v"),
    ("soñar", "v"), ("descansar", "v"), ("despertar", "v"),
    ("levantar", "v"), ("sentar", "v"), ("vestir", "v"), ("regalar", "v"),
    ("invitar", "v"), ("visitar", "v"), ("viajar", "v"), ("montar", "v"),
    ("pescar", "v"), ("plantar", "v"), ("sumar", "v"), ("elegir", "v"),
    ("probar", "v"), ("oler", "v"), ("escuchar", "v"), ("mostrar", "v"),
    ("encender", "v"), ("apagar", "v"), ("repetir", "v"), ("abrazar", "v"),
    ("besar", "v"), ("cuidar", "v"), ("compartir", "v"),
]

# --- Adjektive und Farben ---
ADJECTIVES = [
    ("rojo", "a"), ("azul", "a"), ("verde", "a"), ("amarillo", "a"),
    ("blanco", "a"), ("negro", "a"), ("gris", "a"), ("marrón", "a"),
    ("grande", "a"), ("pequeño", "a"), ("alto", "a"), ("largo", "a"),
    ("corto", "a"), ("gordo", "a"), ("delgado", "a"),
    ("fuerte", "a"), ("débil", "a"), ("rápido", "a"), ("lento", "a"),
    ("nuevo", "a"), ("viejo", "a"), ("joven", "a"), ("bueno", "a"),
    ("malo", "a"), ("bonito", "a"), ("feo", "a"), ("limpio", "a"),
    ("sucio", "a"), ("caliente", "a"), ("frío", "a"), ("seco", "a"),
    ("mojado", "a"), ("duro", "a"), ("blando", "a"), ("lleno", "a"),
    ("vacío", "a"), ("abierto", "a"), ("cerrado", "a"), ("claro", "a"),
    ("oscuro", "a"), ("dulce", "a"), ("salado", "a"), ("feliz", "a"),
    ("triste", "a"), ("contento", "a"), ("cansado", "a"), ("alegre", "a"),
    ("amable", "a"), ("valiente", "a"), ("tranquilo", "a"), ("fácil", "a"),
    ("difícil", "a"), ("importante", "a"), ("redondo", "a"),
    ("pesado", "a"), ("suave", "a"), ("sano", "a"), ("enfermo", "a"),
    ("guapo", "a"), ("listo", "a"), ("tonto", "a"), ("libre", "a"),
    ("primero", "a"), ("último", "a"), ("mejor", "a"), ("peor", "a"),
]

# --- Nomen: Familie und Menschen ---
NOUNS_FAMILY = [
    ("familia", "n"), ("madre", "n"), ("padre", "n"), ("mamá", "n"),
    ("papá", "n"), ("hijo", "n"), ("hija", "n"), ("hermano", "n"),
    ("hermana", "n"), ("abuelo", "n"), ("abuela", "n"), ("tío", "n"),
    ("tía", "n"), ("bebé", "n"), ("niño", "n"), ("niña", "n"),
    ("hombre", "n"), ("mujer", "n"), ("amigo", "n"), ("amiga", "n"),
    ("chico", "n"),
]

# --- Nomen: Schule und Spiel ---
NOUNS_SCHOOL = [
    ("escuela", "n"), ("clase", "n"), ("maestro", "n"), ("libro", "n"),
    ("cuaderno", "n"), ("lápiz", "n"), ("goma", "n"), ("regla", "n"),
    ("tijeras", "n"), ("mochila", "n"), ("papel", "n"), ("hoja", "n"),
    ("mesa", "n"), ("silla", "n"), ("pizarra", "n"), ("letra", "n"),
    ("palabra", "n"), ("número", "n"), ("cuento", "n"), ("pregunta", "n"),
    ("respuesta", "n"), ("juego", "n"), ("juguete", "n"), ("pelota", "n"),
    ("música", "n"),
]

# --- Nomen: Tiere ---
NOUNS_ANIMALS = [
    ("animal", "n"), ("perro", "n"), ("gato", "n"), ("pájaro", "n"),
    ("pez", "n"), ("caballo", "n"), ("vaca", "n"), ("cerdo", "n"),
    ("oveja", "n"), ("gallina", "n"), ("pollo", "n"), ("pato", "n"),
    ("conejo", "n"), ("ratón", "n"), ("león", "n"), ("tigre", "n"),
    ("oso", "n"), ("lobo", "n"), ("elefante", "n"), ("mono", "n"),
    ("rana", "n"), ("tortuga", "n"), ("abeja", "n"), ("mariposa", "n"),
]

# --- Nomen: Essen und Trinken ---
NOUNS_FOOD = [
    ("comida", "n"), ("pan", "n"), ("agua", "n"), ("leche", "n"),
    ("queso", "n"), ("huevo", "n"), ("carne", "n"), ("pescado", "n"),
    ("arroz", "n"), ("sopa", "n"), ("fruta", "n"), ("manzana", "n"),
    ("plátano", "n"), ("naranja", "n"), ("limón", "n"), ("uva", "n"),
    ("fresa", "n"), ("tomate", "n"), ("patata", "n"), ("zanahoria", "n"),
    ("azúcar", "n"), ("sal", "n"), ("chocolate", "n"), ("pastel", "n"),
    ("helado", "n"), ("plato", "n"), ("vaso", "n"), ("cuchara", "n"),
]

# --- Nomen: Koerper ---
NOUNS_BODY = [
    ("cuerpo", "n"), ("cabeza", "n"), ("pelo", "n"), ("cara", "n"),
    ("ojo", "n"), ("oreja", "n"), ("nariz", "n"), ("boca", "n"),
    ("diente", "n"), ("brazo", "n"), ("mano", "n"), ("dedo", "n"),
    ("espalda", "n"), ("pierna", "n"), ("rodilla", "n"), ("pie", "n"),
    ("corazón", "n"),
]

# --- Nomen: Natur ---
NOUNS_NATURE = [
    ("sol", "n"), ("luna", "n"), ("estrella", "n"), ("cielo", "n"),
    ("nube", "n"), ("lluvia", "n"), ("nieve", "n"), ("viento", "n"),
    ("tierra", "n"), ("mar", "n"), ("río", "n"), ("playa", "n"),
    ("montaña", "n"), ("bosque", "n"), ("árbol", "n"), ("flor", "n"),
    ("rosa", "n"), ("planta", "n"), ("piedra", "n"), ("fuego", "n"),
    ("campo", "n"), ("jardín", "n"), ("mundo", "n"),
]

# --- Nomen: Haus, Stadt, Verkehr ---
NOUNS_HOUSE = [
    ("casa", "n"), ("puerta", "n"), ("ventana", "n"), ("pared", "n"),
    ("suelo", "n"), ("cocina", "n"), ("baño", "n"), ("cama", "n"),
    ("luz", "n"), ("llave", "n"), ("reloj", "n"), ("teléfono", "n"),
    ("coche", "n"), ("bicicleta", "n"), ("tren", "n"), ("avión", "n"),
    ("calle", "n"), ("ciudad", "n"), ("pueblo", "n"), ("parque", "n"),
    ("tienda", "n"), ("dinero", "n"),
]

# --- Nomen: Kleidung ---
NOUNS_CLOTHES = [
    ("ropa", "n"), ("camisa", "n"), ("camiseta", "n"), ("pantalón", "n"),
    ("falda", "n"), ("vestido", "n"), ("abrigo", "n"), ("zapato", "n"),
    ("bota", "n"),
]

# --- Nomen: Zeit ---
NOUNS_TIME = [
    ("día", "n"), ("noche", "n"), ("tarde", "n"), ("semana", "n"),
    ("mes", "n"), ("año", "n"), ("hora", "n"), ("tiempo", "n"),
    ("lunes", "n"), ("martes", "n"), ("miércoles", "n"), ("jueves", "n"),
    ("viernes", "n"), ("sábado", "n"), ("domingo", "n"), ("invierno", "n"),
    ("verano", "n"), ("fiesta", "n"), ("cumpleaños", "n"),
]

WORDS = (
    FUNCTION
    + VERBS
    + ADJECTIVES
    + NOUNS_FAMILY
    + NOUNS_SCHOOL
    + NOUNS_ANIMALS
    + NOUNS_FOOD
    + NOUNS_BODY
    + NOUNS_NATURE
    + NOUNS_HOUSE
    + NOUNS_CLOTHES
    + NOUNS_TIME
)


if __name__ == "__main__":
    from collections import Counter
    print("total:", len(WORDS), "unique:", len({w for w, _ in WORDS}))
    print(Counter(k for _, k in WORDS))
    dupes = [w for w, c in Counter(w for w, _ in WORDS).items() if c > 1]
    print("dupes:", dupes)
