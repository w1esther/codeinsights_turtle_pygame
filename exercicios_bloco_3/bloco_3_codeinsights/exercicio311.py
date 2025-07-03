# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 3.11


# Não tem código inicial. É sua vez de brilhar.

import turtle
import festa_dançante

p = festa_dançante.cria_dançarino('Principal', 'Centro')
festa_dançante.defina('Principal', 'color', 'pink')

turtle.onkey(p.anda_direita, 'Right')
turtle.onkey(p.anda_esquerda, 'Left')

turtle.ontimer(p.faz_rodopio, 4000)
turtle.ontimer(p.faz_rodopio, 8000)


a = festa_dançante.cria_dançarinos_apoio(8, 'Apoio', 'Circulo')
festa_dançante.defina('Apoio', 'color', 'pink')

festa_dançante.muda_palco()


turtle.mainloop()