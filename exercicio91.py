# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 9.1

import turtle
from kareto.fase31 import Abelha, tem_nectar_no_girassol

maia = Abelha()


# Seu código aqui
for n in range(5):
    maia.avance()
    while tem_nectar_no_girassol():
        maia.obtenha_nectar()

# Fim do seu código

maia.avance()

turtle.mainloop()

