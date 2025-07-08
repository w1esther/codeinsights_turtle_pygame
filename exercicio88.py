# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 8.8


import turtle

from kareto.fase27 import Abelha


maia = Abelha()

## Seu código a partir aqui
maia.obtenha_nectar()
for n in range(8):
    for n in range(7):
        maia.avance()
        if maia.no_girassol():
            maia.obtenha_nectar()
        else:
            for n in range(7):
                maia.faça_mel()


# Fim do seu código aqui

turtle.mainloop()

