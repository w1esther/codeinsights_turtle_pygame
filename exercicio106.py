# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 10.6



"""Jogo da Velha

Exercícios

1. Dê ao X e ao O uma cor e espessura diferentes. ok
2. O que acontece quando alguém toca em um espaço já ocupado? ok
3. Como detectar quando alguém venceu? 
4. Como você poderia criar um jogador automático? ok
"""

import turtle
from freegames import line
from random import randint
from tkinter import messagebox


def grade():
    """Desenha a grade do jogo da velha."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)
    


def desenhar_x(x, y):
    """Desenha o jogador X."""
    turtle.color('red')
    turtle.width(5)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)
    

def desenhar_o(x, y):
    """Desenha o jogador O."""

    turtle.color('blue')
    turtle.width(5)
    turtle.up()
    turtle.goto(x + 67, y + 5)
    turtle.down()
    turtle.circle(62)
    


def arredondar(valor):
    """Arredonda o valor para a grade com tamanho de quadrado 133."""
    return ((valor + 200) // 133) * 133 - 200


estado = {'jogador': 0}
jogadores = [desenhar_x, desenhar_o]



tabuleiro = [None] * 9

def obter_indice(x, y):
    coluna = int((x + 200) // 133)
    linha = int((y + 200) // 133)
    return linha * 3 + coluna

def obter_xy(indice):
    linha = indice // 3
    coluna = indice % 3
    x = -200 + coluna * 133
    y = -200 + linha * 133
    return x, y

# 0 é o O, e 1 é o X


def tocar(x, y):
    """Desenha X ou O no quadrado tocado."""
    if estado['jogador'] != 0: # impede que o humano jogue quando for a vez do robô
        return
    indice = obter_indice(x, y)
    if tabuleiro[indice] is None:
        x = arredondar(x)
        y = arredondar(y)
        jogador = estado['jogador'] # guarda o valor que foi jogado
        desenhar = jogadores[0]
        desenhar(x, y)
        turtle.update()
        tabuleiro[indice] = 0 # marca o tabuleiro na opção selecionada
        if verificar_vitoria(0):
            # print('você venceu!')
            messagebox.showinfo("Ganhou!", "Você venceu!")
            exit(turtle)
        estado['jogador'] = 1 # passa a vez para o robô
        turtle.ontimer(jogador_automatico, 1000)
    

def jogador_automatico():
    if estado['jogador'] !=1: 
        return
    while True:
        indice = randint(0, 8)
        if tabuleiro[indice] is None:
            x, y = obter_xy(indice) # por que não posso usar obter_indice
            jogador = estado['jogador']
            desenhar = jogadores[1]
            desenhar(x, y)
            tabuleiro[indice] = 1
            if verificar_vitoria(1):
                # print('o robô venceu!')
                messagebox.showinfo("Perdeu!", "O robô venceu!")
                exit(turtle)
            turtle.update()
            estado['jogador'] = 0
            break

def verificar_vitoria(jogador):
    combinacoes = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6) ]
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador:
            return True
    return False

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grade()
turtle.update()
turtle.onscreenclick(tocar) # não preciso chamar tocar em jogador_automatico, ela é "automática"
turtle.done()