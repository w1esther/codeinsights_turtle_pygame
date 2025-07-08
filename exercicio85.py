# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 8.5


import turtle

from kareto.fase24 import Abelha


maia = Abelha()

## Seu código a partir aqui
for n in range(4):
    maia.avance()
    maia.avance()
    maia.avance()
    if maia.no_girassol():
        maia.obtenha_nectar()
    if maia.na_colmeia():
        maia.faça_mel()
    maia.direita()
    
    

# Fim do seu código aqui

turtle.mainloop()

