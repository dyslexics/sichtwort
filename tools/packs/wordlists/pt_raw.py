# -*- coding: utf-8 -*-
"""Grundwortschatz Portugiesisch (pt) fuer Sichtwort-Blitzlesen.
Neutral zwischen europaeischem und brasilianischem Portugiesisch:
keine Woerter, die nur in einer Variante ueblich sind (kein autocarro/onibus,
comboio/trem, telemovel/celular, bebe/bebe, tenis/tenis, rapariga, ...).
Rechtschreibung nach Acordo Ortografico.
Typen: n = Nomen, v = Verb (Infinitiv), a = Adjektiv, o = Sonstiges.
"""

WORDS = [
    # --- Artikel, Kontraktionen, Praepositionen -------------------------
    ("o", "o"), ("a", "o"), ("os", "o"), ("as", "o"),
    ("um", "o"), ("uma", "o"), ("uns", "o"), ("umas", "o"),
    ("ao", "o"), ("à", "o"), ("aos", "o"), ("às", "o"),
    ("do", "o"), ("da", "o"), ("dos", "o"), ("das", "o"),
    ("no", "o"), ("na", "o"), ("nos", "o"), ("nas", "o"),
    ("pelo", "o"), ("pela", "o"), ("de", "o"), ("em", "o"),
    ("por", "o"), ("para", "o"), ("com", "o"), ("sem", "o"),
    ("sob", "o"), ("sobre", "o"), ("entre", "o"), ("até", "o"),
    ("desde", "o"), ("contra", "o"), ("antes", "o"), ("depois", "o"),

    # --- Konjunktionen, Frage- und Verweiswoerter -----------------------
    ("e", "o"), ("ou", "o"), ("mas", "o"), ("que", "o"),
    ("se", "o"), ("pois", "o"), ("porque", "o"), ("quando", "o"),
    ("como", "o"), ("onde", "o"), ("quem", "o"), ("qual", "o"),
    ("quanto", "o"),

    # --- Adverbien und Partikeln ----------------------------------------
    ("não", "o"), ("sim", "o"), ("também", "o"), ("já", "o"),
    ("ainda", "o"), ("sempre", "o"), ("nunca", "o"), ("só", "o"),
    ("apenas", "o"), ("muito", "o"), ("pouco", "o"), ("mais", "o"),
    ("menos", "o"), ("tanto", "o"), ("tão", "o"), ("quase", "o"),
    ("talvez", "o"), ("bem", "o"), ("mal", "o"), ("aqui", "o"),
    ("ali", "o"), ("lá", "o"), ("perto", "o"), ("longe", "o"),
    ("dentro", "o"), ("fora", "o"), ("cima", "o"), ("atrás", "o"),
    ("junto", "o"), ("agora", "o"), ("hoje", "o"), ("ontem", "o"),
    ("amanhã", "o"), ("cedo", "o"), ("tarde", "o"), ("logo", "o"),
    ("então", "o"), ("assim", "o"),

    # --- Demonstrativa und Pronomen -------------------------------------
    ("este", "o"), ("esta", "o"), ("isto", "o"), ("esse", "o"),
    ("essa", "o"), ("isso", "o"), ("aquele", "o"), ("aquela", "o"),
    ("aquilo", "o"), ("eu", "o"), ("tu", "o"), ("ele", "o"),
    ("ela", "o"), ("nós", "o"), ("eles", "o"), ("elas", "o"),
    ("me", "o"), ("te", "o"), ("lhe", "o"), ("lhes", "o"),
    ("meu", "o"), ("minha", "o"), ("teu", "o"), ("tua", "o"),
    ("seu", "o"), ("sua", "o"), ("nosso", "o"), ("nossa", "o"),
    ("dele", "o"), ("dela", "o"),

    # --- Quantoren -------------------------------------------------------
    ("tudo", "o"), ("todo", "o"), ("toda", "o"), ("todos", "o"),
    ("todas", "o"), ("nada", "o"), ("ninguém", "o"), ("algo", "o"),
    ("alguém", "o"), ("algum", "o"), ("alguma", "o"), ("nenhum", "o"),
    ("outro", "o"), ("outra", "o"), ("cada", "o"), ("mesmo", "o"),

    # --- Zahlen ----------------------------------------------------------
    ("dois", "o"), ("duas", "o"), ("três", "o"), ("quatro", "o"),
    ("cinco", "o"), ("seis", "o"), ("sete", "o"), ("oito", "o"),
    ("nove", "o"), ("dez", "o"), ("onze", "o"), ("doze", "o"),
    ("treze", "o"), ("quinze", "o"), ("vinte", "o"), ("trinta", "o"),
    ("cem", "o"), ("mil", "o"),

    # --- Grussformeln ----------------------------------------------------
    ("olá", "o"), ("adeus", "o"), ("obrigado", "o"), ("obrigada", "o"),

    # --- Nomen: Familie und Menschen -------------------------------------
    ("família", "n"), ("mãe", "n"), ("pai", "n"), ("filho", "n"),
    ("filha", "n"), ("irmão", "n"), ("irmã", "n"), ("avô", "n"),
    ("avó", "n"), ("tio", "n"), ("tia", "n"), ("primo", "n"),
    ("criança", "n"), ("menino", "n"), ("menina", "n"), ("homem", "n"),
    ("mulher", "n"), ("senhor", "n"), ("senhora", "n"), ("amigo", "n"),
    ("amiga", "n"), ("pessoa", "n"), ("nome", "n"), ("festa", "n"),
    ("beijo", "n"), ("amor", "n"), ("vida", "n"),

    # --- Nomen: Schule und Spiel -----------------------------------------
    ("escola", "n"), ("aula", "n"), ("professor", "n"), ("professora", "n"),
    ("aluno", "n"), ("livro", "n"), ("caderno", "n"), ("lápis", "n"),
    ("caneta", "n"), ("borracha", "n"), ("mochila", "n"), ("papel", "n"),
    ("folha", "n"), ("quadro", "n"), ("sala", "n"), ("letra", "n"),
    ("palavra", "n"), ("frase", "n"), ("número", "n"), ("história", "n"),
    ("desenho", "n"), ("jogo", "n"), ("colega", "n"), ("música", "n"),
    ("caixa", "n"), ("bola", "n"), ("brinquedo", "n"),

    # --- Nomen: Tiere ------------------------------------------------------
    ("animal", "n"), ("cão", "n"), ("gato", "n"), ("cavalo", "n"),
    ("vaca", "n"), ("porco", "n"), ("galinha", "n"), ("pato", "n"),
    ("pássaro", "n"), ("peixe", "n"), ("rato", "n"), ("coelho", "n"),
    ("urso", "n"), ("leão", "n"), ("cobra", "n"), ("sapo", "n"),
    ("abelha", "n"),

    # --- Nomen: Essen und Trinken ------------------------------------------
    ("comida", "n"), ("pão", "n"), ("leite", "n"), ("queijo", "n"),
    ("arroz", "n"), ("feijão", "n"), ("batata", "n"), ("cenoura", "n"),
    ("tomate", "n"), ("maçã", "n"), ("banana", "n"), ("pera", "n"),
    ("uva", "n"), ("limão", "n"), ("laranja", "n"), ("ovo", "n"),
    ("carne", "n"), ("frango", "n"), ("sopa", "n"), ("bolo", "n"),
    ("açúcar", "n"), ("sal", "n"), ("água", "n"), ("mel", "n"),
    ("fruta", "n"), ("prato", "n"), ("copo", "n"), ("faca", "n"),
    ("fome", "n"),

    # --- Nomen: Koerper -----------------------------------------------------
    ("corpo", "n"), ("cabeça", "n"), ("cabelo", "n"), ("olho", "n"),
    ("orelha", "n"), ("nariz", "n"), ("boca", "n"), ("dente", "n"),
    ("língua", "n"), ("cara", "n"), ("braço", "n"), ("mão", "n"),
    ("dedo", "n"), ("perna", "n"), ("joelho", "n"), ("pé", "n"),
    ("coração", "n"),

    # --- Nomen: Natur und Zeit ----------------------------------------------
    ("sol", "n"), ("lua", "n"), ("estrela", "n"), ("céu", "n"),
    ("nuvem", "n"), ("chuva", "n"), ("vento", "n"), ("neve", "n"),
    ("gelo", "n"), ("tempo", "n"), ("dia", "n"), ("noite", "n"),
    ("manhã", "n"), ("semana", "n"), ("mês", "n"), ("ano", "n"),
    ("hora", "n"), ("verão", "n"), ("inverno", "n"), ("terra", "n"),
    ("mar", "n"), ("rio", "n"), ("lago", "n"), ("praia", "n"),
    ("pedra", "n"), ("árvore", "n"), ("flor", "n"), ("planta", "n"),
    ("campo", "n"), ("jardim", "n"), ("fogo", "n"), ("luz", "n"),
    ("ar", "n"), ("mundo", "n"),

    # --- Nomen: Haus und Stadt ------------------------------------------------
    ("casa", "n"), ("porta", "n"), ("janela", "n"), ("parede", "n"),
    ("chão", "n"), ("escada", "n"), ("quarto", "n"), ("cozinha", "n"),
    ("cama", "n"), ("mesa", "n"), ("cadeira", "n"), ("chave", "n"),
    ("telefone", "n"), ("carta", "n"), ("carro", "n"), ("avião", "n"),
    ("barco", "n"), ("cidade", "n"), ("loja", "n"), ("médico", "n"),
    ("parque", "n"), ("rua", "n"), ("caminho", "n"), ("dinheiro", "n"),
    ("sapato", "n"), ("meia", "n"), ("camisa", "n"), ("roupa", "n"),
    ("cor", "n"), ("lado", "n"), ("vez", "n"), ("coisa", "n"),
    ("parte", "n"), ("fim", "n"),

    # --- Verben --------------------------------------------------------------
    ("ser", "v"), ("estar", "v"), ("ter", "v"), ("fazer", "v"),
    ("dizer", "v"), ("ir", "v"), ("vir", "v"), ("ver", "v"),
    ("dar", "v"), ("saber", "v"), ("poder", "v"), ("querer", "v"),
    ("ficar", "v"), ("passar", "v"), ("chegar", "v"), ("deixar", "v"),
    ("falar", "v"), ("olhar", "v"), ("começar", "v"), ("sentir", "v"),
    ("pensar", "v"), ("viver", "v"), ("andar", "v"), ("entrar", "v"),
    ("sair", "v"), ("voltar", "v"), ("conhecer", "v"), ("trazer", "v"),
    ("correr", "v"), ("levar", "v"), ("gostar", "v"), ("escrever", "v"),
    ("ler", "v"), ("comer", "v"), ("beber", "v"), ("dormir", "v"),
    ("acordar", "v"), ("brincar", "v"), ("jogar", "v"), ("cantar", "v"),
    ("dançar", "v"), ("saltar", "v"), ("nadar", "v"), ("voar", "v"),
    ("abrir", "v"), ("fechar", "v"), ("subir", "v"), ("descer", "v"),
    ("comprar", "v"), ("vender", "v"), ("pagar", "v"), ("ajudar", "v"),
    ("esperar", "v"), ("chamar", "v"), ("perguntar", "v"), ("responder", "v"),
    ("contar", "v"), ("mostrar", "v"), ("aprender", "v"), ("estudar", "v"),
    ("ensinar", "v"), ("trabalhar", "v"), ("lavar", "v"), ("limpar", "v"),
    ("cortar", "v"), ("pintar", "v"), ("desenhar", "v"), ("procurar", "v"),
    ("encontrar", "v"), ("perder", "v"), ("ganhar", "v"), ("guardar", "v"),
    ("mudar", "v"), ("parar", "v"), ("seguir", "v"), ("cair", "v"),
    ("bater", "v"), ("tocar", "v"), ("rir", "v"), ("chorar", "v"),
    ("gritar", "v"), ("sorrir", "v"), ("amar", "v"), ("precisar", "v"),
    ("usar", "v"), ("viajar", "v"), ("receber", "v"), ("sentar", "v"),
    ("levantar", "v"), ("vestir", "v"), ("crescer", "v"), ("nascer", "v"),
    ("lembrar", "v"), ("esquecer", "v"), ("entender", "v"), ("acabar", "v"),
    ("tentar", "v"), ("escolher", "v"), ("pôr", "v"), ("pegar", "v"),

    # --- Adjektive -------------------------------------------------------------
    ("bom", "a"), ("boa", "a"), ("mau", "a"), ("grande", "a"),
    ("pequeno", "a"), ("alto", "a"), ("baixo", "a"), ("novo", "a"),
    ("velho", "a"), ("jovem", "a"), ("bonito", "a"), ("feio", "a"),
    ("limpo", "a"), ("sujo", "a"), ("cheio", "a"), ("vazio", "a"),
    ("quente", "a"), ("frio", "a"), ("seco", "a"), ("duro", "a"),
    ("leve", "a"), ("pesado", "a"), ("forte", "a"), ("fraco", "a"),
    ("rápido", "a"), ("lento", "a"), ("fácil", "a"), ("difícil", "a"),
    ("certo", "a"), ("errado", "a"), ("feliz", "a"), ("triste", "a"),
    ("alegre", "a"), ("contente", "a"), ("calmo", "a"), ("doce", "a"),
    ("aberto", "a"), ("fechado", "a"), ("claro", "a"), ("escuro", "a"),
    ("branco", "a"), ("preto", "a"), ("vermelho", "a"), ("azul", "a"),
    ("verde", "a"), ("amarelo", "a"), ("engraçado", "a"), ("cansado", "a"),
    ("doente", "a"), ("sozinho", "a"), ("igual", "a"), ("diferente", "a"),
    ("importante", "a"), ("livre", "a"), ("melhor", "a"), ("pior", "a"),
    ("primeiro", "a"), ("segundo", "a"), ("terceiro", "a"), ("último", "a"),
]
