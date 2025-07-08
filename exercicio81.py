# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 8.1


import turtle

from kareto.fase20 import Abelha


maia = Abelha()

## Seu código a partir aqui

for n in range(2):
    maia.avance()
    if maia.no_girassol():
        maia.obtenha_nectar()
    maia.avance()  
    maia.direita()
    if maia.no_girassol():
        maia.obtenha_nectar()
# Fim do seu código aqui

turtle.mainloop()

