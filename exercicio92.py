# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 9.2

import turtle
from kareto.fase32 import Abelha, tem_nectar_na_colmeia

maia = Abelha()

# Seu código aqui

for n in range(3):
    maia.avance()
    while tem_nectar_na_colmeia():
        maia.faça_mel()
    maia.direita()
    maia.avance()
    while tem_nectar_na_colmeia():
        maia.faça_mel()
    maia.esquerda()
# Fim do seu código

turtle.mainloop()