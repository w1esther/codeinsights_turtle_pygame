# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 11.3

import turtle
from kareto.fase72 import Artista


# definição da função
def desenhe_estrela():
    for n in range(8):
        artista.forward(25)
        artista.backward(25)
        artista.right(45)


artista = Artista()
desenhe_estrela() # chamada da função


turtle.mainloop()
	
