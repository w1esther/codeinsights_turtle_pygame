# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 11.6

import turtle
from kareto.fase75 import Artista


# definição da função
def desenhe_quadrado():
    for _ in range(4):
        artista.forward(50)
        artista.left(90)

def desenhe_quadrado_2():
    for n in range(4):
        artista.forward(50)
        artista.right(90)

def desenha_uma_linha_de_quadrados():
    for n in range(3):
        desenhe_quadrado()
        artista.penup()
        artista.forward(100)
        artista.pendown()
    artista.right(90)
    # for n in range(3):
    desenhe_quadrado_2()
    artista.penup()
    artista.left(270)
    artista.forward(100)
    artista.pendown()
    desenhe_quadrado()
    artista.penup()
    artista.forward(100)
    artista.pendown()
    desenhe_quadrado()
    




artista = Artista()
desenha_uma_linha_de_quadrados()


turtle.mainloop()
	
