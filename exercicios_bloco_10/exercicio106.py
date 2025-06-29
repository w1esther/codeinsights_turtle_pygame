# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 10.6



"""Jogo da Velha

Exercícios

1. Dê ao X e ao O uma cor e espessura diferentes. ok
2. O que acontece quando alguém toca em um espaço já ocupado? !!!
3. Como detectar quando alguém venceu? 
4. Como você poderia criar um jogador automático?
"""

import turtle
from freegames import line
from random import choice


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

# tabuleiro = [None] * 9

# def obter_indice(x, y):
#     coluna = int((x + 200) // 133)
#     linha = int((y + 200) // 133)
#     return linha * 3 + coluna


def tocar(x, y):
    """Desenha X ou O no quadrado tocado."""
    # indice = obter_indice(x, y)
    x = arredondar(x)
    y = arredondar(y)
    jogador = estado['jogador']
    desenhar = jogadores[jogador]
    desenhar(x, y)
    turtle.update()
    estado['jogador'] = not jogador
    turtle.color('pink')
    # if tabuleiro[indice] is not None:
    #     return



turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grade()
turtle.update()
turtle.onscreenclick(tocar)
turtle.done()