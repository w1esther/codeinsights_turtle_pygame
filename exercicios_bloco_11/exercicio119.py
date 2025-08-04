# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 11.9

import turtle
from kareto.fase78 import Artista

def hexagono():
    for _ in range(6):
        artista.forward(25)
        artista.right(60)

def linha_de_hexagonos():
    for _ in range(8):
        hexagono()
        artista.pule_para_frente(25)

def linha_de_hexagonos_2():
    for _ in range(8):
        hexagono()
        artista.backward(25)

def quadrado():
    for _ in range(4):
        artista.forward(50)
        artista.left(90)

def linha_de_quadrados():
    for _ in range(3):
        quadrado()
        artista.pule_para_frente(100)

def quadrado_deslocados():
    for _ in range(2):
        linha_de_hexagonos()
        artista.right(180)

artista = Artista()
artista.mude_cor()
artista.penup()
artista.backward(50)
artista.pendown()
linha_de_hexagonos()
for n in range(3):
    artista.left(120)
    linha_de_hexagonos()
    artista.penup()
    linha_de_hexagonos_2()
    artista.pendown()
for n in range(3):
    artista.right(120)
    linha_de_hexagonos()
    artista.penup()
    linha_de_hexagonos_2()
    artista.pendown()


turtle.mainloop()

