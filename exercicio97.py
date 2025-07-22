# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 9.7

# Este é 100% com você.

import turtle
from kareto.fase37 import Abelha, tem_nectar_no_girassol, tem_caminho, tem_nectar_na_colmeia

maia = Abelha()

for n in range(3):
    while tem_caminho():
        maia.avance()

        while tem_nectar_no_girassol():
            maia.obtenha_nectar()

        while tem_nectar_na_colmeia():
            maia.faça_mel()

    maia.direita()

turtle.mainloop()