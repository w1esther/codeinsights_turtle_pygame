# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 10.4


"""Cobrinha, jogo clássico de arcade.

Exercícios

1. Como você pode deixar a cobra mais rápida ou mais lenta? ok
2. Como você pode fazer a cobra atravessar as bordas e aparecer do outro lado? ok
3. Como você poderia mover a comida? ok
4. Modifique o jogo para que a cobra possa ser controlada com cliques do mouse.
"""

from random import randrange
from threading import Timer
import turtle

from freegames import square, vector

comida = vector(0, 0)
cobra = [vector(10, 0)]
direcao = vector(0, -10)

def criar_comida():
    comida.x = randrange(-15, 15) * 10
    comida.y = randrange(-15, 15) * 10



def mudar_direcao(x, y):
    """Muda a direção da cobra."""
    direcao.x = x
    direcao.y = y


def dentro(lider):
    """Retorna True se a cabeça da cobra estiver dentro dos limites."""
    return -200 < lider.x < 190 and -200 < lider.y < 190


def mover():
    """Move a cobra para frente um segmento."""
    lider = cobra[-1].copy()
    # print(lider)
    lider.move(direcao)
    # lider.speed(10)

    if not dentro(lider) or lider in cobra:
        if lider.y == -200:
            lider.y = 190
        elif lider.x == -200:
            lider.x = 190
        elif lider.y == 190:
            lider.y = -200
        elif lider.x == 190:
            lider.x = -200


        # square(lider.x, lider.y, 9, 'red')
        # turtle.update()
        # return
    cobra.append(lider)

    if lider == comida:
        print('Tamanho da cobra:', len(cobra))
        criar_comida()
    else:
        cobra.pop(0)

    turtle.clear()

    for segmento in cobra:
        square(segmento.x, segmento.y, 9, 'black')

    square(comida.x, comida.y, 9, 'green')
    turtle.update()
    turtle.ontimer(mover, 100)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: mudar_direcao(5, 0), 'Right')
turtle.onkey(lambda: mudar_direcao(-5, 0), 'Left')
turtle.onkey(lambda: mudar_direcao(0, 5), 'Up')
turtle.onkey(lambda: mudar_direcao(0, -5), 'Down')
mover()

turtle.mainloop()
