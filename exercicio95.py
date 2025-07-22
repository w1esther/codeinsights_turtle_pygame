# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 9.5

import turtle
from kareto.fase35 import Abelha, tem_nectar_no_girassol, tem_caminho

maia = Abelha()

# Seu código aqui

for n in range(3):
    while tem_caminho():
        maia.avance()
    while tem_nectar_no_girassol():
        maia.obtenha_nectar()
    maia.esquerda()
    while tem_caminho():
        maia.avance()
    maia.direita()
# Fim do seu código

turtle.mainloop()