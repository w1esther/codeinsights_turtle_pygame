# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 11.4

import turtle
from kareto.fase73 import Artista


# definição da função
artista = Artista()

def desenhe_janela():
    artista.penup()
    artista.forward(25)
    artista.pendown()
    artista.left(90)
    artista.forward(25)
    for n in range(4):
        artista.left(90)
        artista.forward(50)
    artista.left(90)
    artista.forward(25)
    artista.left(90)
    artista.forward(50)
    artista.backward(25)
    artista.left(90)
    artista.forward(25)
    artista.backward(50)
        
desenhe_janela()

for n in range(2):
    artista.penup()
    artista.forward(125)
    artista.pendown()
    desenhe_janela()
artista.right(90)
artista.penup()
artista.forward(150)
artista.left(90)
artista.forward(25)
artista.pendown()
desenhe_janela()
artista.penup()
artista.backward(175)
artista.pendown()
desenhe_janela()
    



turtle.mainloop()
	
