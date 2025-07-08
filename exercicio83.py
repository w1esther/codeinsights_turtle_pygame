# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 8.3


import turtle

from kareto.fase22 import Abelha


maia = Abelha()

## Seu código a partir aqui

for n in range(2):
    maia.avance()
    maia.avance()
    if maia.na_colmeia():
        maia.faça_mel()
    maia.direita()

# Fim do seu código aqui

turtle.mainloop()

