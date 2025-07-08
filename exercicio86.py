# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 8.6


import turtle

from kareto.fase25 import Abelha


maia = Abelha()

## Seu código a partir aqui

for n in range(7):
    maia.avance()
    if maia.no_girassol():
        maia.obtenha_nectar()
    else:
        maia.faça_mel()

# Fim do seu código aqui

turtle.mainloop()

