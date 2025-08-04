# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 11.2


import turtle
from kareto.fase71 import Artista


# definição da função
def desenhar_quadrado():
    """Desenha um quadrado com lado de 100 pixels."""
    for _ in range(4):
        artista.forward(100)
        artista.right(90)

artista = Artista()

# chamada/execução da função
desenhar_quadrado()

artista.forward(175)

desenhar_quadrado()


turtle.mainloop()
	
