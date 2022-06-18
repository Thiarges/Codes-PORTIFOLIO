# |||INTEGRANTES|||
# Pedro Henrique Serrato de Castro
# Vitor Prado Zambaldi
# Lucas Gabriel Nunes Geremias
# Lucas Henrique Rudiniki Costanski
# Thiago Vinícius Pereira Borges

import random
import time


# Critério de definição para a vitória
def vitoria(mt):
    cont = 0
    tam = len(mt)
    for i in range(0, tam):
        for j in range(0, tam):
            if mt[i][j] != '#':
                cont += 1

    return cont


# Função para gerar a dica
def dica(mt, mte):
    mostrar(mt)
    time.sleep(3)
    limpar()
    mostrar(mte)
    return


# Criar tabela escondida
def tabesc(tm):
    tb = []
    for i in range(0, tm):
        tb.append([])
        for j in range(0, tm):
            tb[i].append('#')
    return tb


# Criar tabela embaralhada
def tabemb(tm, mat):
    tabe = mat
    perc = int(((tm ** 2) / 2))
    for i in range(0, perc):
        b = 0

        elemento = random.randint(65, 90)
        while (b != 2):
            l1 = int(random.uniform(0, tm))
            c1 = int(random.uniform(0, tm))
            l = l1
            c = c1
            if tabe[l][c] == '#':
                tabe[l][c] = chr(elemento)
                b += 1
    return tabe


# Mostrar a Matriz de forma clara
def mostrar(mt):
    tam = len(mt)
    for i in range(0, tam):
        print("\n", mt[i])

    return


# Função para descobrir o resultado
def resultado(l, c, l1, c1, mt, mte):
    cont = 0
    if (mt[l][c] == mt[l1][c1]):
        mte[l][c] = mt[l][c]
        mte[l1][c1] = mt[l1][c1]
        print("\nVOCE ACERTOU!!!")
        cont += 1
    else:
        print("\nVOCE ERROU!!!")
    return


# Limpar o terminal
def limpar():
    for i in range(0, 50):
        print("\n")


# Variavel definida para entrar no While
d = 0

while (d != 1 and d != 2 and d != 3):
    print("BEM VINDO AO JOGO DA MEMORIA!!!!")

    d = int(input(
        "Temos o modo 1-Facil, 2-Medio e 3-Dificil\n Selecione a dificuldade que voce quer? (OBS: SE QUISER ENCERRAR O JOGO DIGITE 4):  "))

    if d == 1:
        tm = 4
    elif d == 2:
        tm = 8
    elif d == 3:
        tm = 10
    elif d == 4:
        exit()
    else:
        print("Não tem essa dificuldade!!!\n Digite novamente!")

    tab = tabesc(tm)
    tab_esc = tabesc(tm)

tabela = tabemb(tm, tab)
print("Voce vai ter 5 SEGUNDOS para decorar a matriz!!!")
mostrar(tabela)
time.sleep(5)
limpar()
ent = True
dicas = 0
dica1 = 1
cont = 0

# While para executar a comparação de posiçóes
while (ent == True):
    mostrar(tab_esc)
    if dicas < 2 and dica1 == 1:
        dica2 = int(input("Voce vai querer uma dica?(LEMBRE-SE so pode usar 2 VEZES)\n 1-Sim\n 2-Não\nR: "))
        if (dicas < 2 and dica2 == 1):
            dica(tabela, tab_esc)
            dicas += 1

    l = int(input("Digite a posicao da linha que vc quer:"))
    c = int(input("Digite a posicao da coluna que vc quer:"))

    print("\n")
    mostrar(tab_esc)

    l1 = int(input("Digite a posição da OUTRA linha que vc quer: "))
    c1 = int(input("Digite a posição da OUTRA coluna que vc quer: "))

    des = int(input("Voce quer desistir? Digite 1 para Sim e 2 para Não\nR: "))
    if des == 1:
        print("Voce desistiu, encerrando o jogo")
        ent = False
    elif des == 2:
        print("Continuando...")

    resultado(l, c, l1, c1, tabela, tab_esc)
    cont = vitoria(tab_esc)
    if (cont == tm ** 2):
        print("PARABENS!!!\nVOCE VENCEU O JOGO!!!")
        ent = False
