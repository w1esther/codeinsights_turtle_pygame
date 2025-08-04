# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 11.8

# Este é todo com você

import turtle
from kareto.fase77 import Artista

artista = Artista()

def desenhe_triangulo():
    for n in range(3):
        artista.forward(50)
        artista.right(120)

desenhe_triangulo()
for n in range(3):
    artista.forward(50)
    desenhe_triangulo()
artista.forward(50)
artista.right(60)
for n in range(4):
    desenhe_triangulo()
    artista.forward(50)
artista.right(120)
artista.forward(50)
for n in range(3):
    desenhe_triangulo()
    artista.forward(50)
artista.right(60)
for n in range(3):
    desenhe_triangulo()
    artista.forward(50)



turtle.mainloop()