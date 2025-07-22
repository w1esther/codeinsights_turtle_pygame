# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 9.4

import turtle
from kareto.fase34 import Abelha, tem_nectar_na_colmeia, tem_caminho

maia = Abelha()

# Seu código aqui

for n in range (6):
    while tem_caminho():
        maia.avance()
    while tem_nectar_na_colmeia():
        maia.faça_mel()
    maia.direita()
# Fim do seu código

turtle.mainloop()