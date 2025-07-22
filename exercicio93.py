# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 9.3

import turtle
from kareto.fase33 import Abelha, tem_nectar_na_colmeia, tem_caminho

maia = Abelha()

# Seu código aqui

for n in range(4):
    while tem_caminho():
        maia.avance()
    maia.faça_mel()
    maia.esquerda()
# Fim do seu código

turtle.mainloop()