# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 10.5



"""Pacman, jogo clássico de arcade.

Exercícios

1. Modifique o tabuleiro. ok
2. Altere o número de fantasmas. ok
3. Mude onde o Pacman começa. ok
4. Faça os fantasmas ficarem mais rápidos/lentos. ok
5. Torne os fantasmas mais inteligentes.
"""

from random import choice
import turtle

from freegames import floor, vector

estado = {'pontuacao': 0}
caminho = turtle.Turtle(visible=False)
escritor = turtle.Turtle(visible=False)
sentido = vector(5, 0)
pacman = vector(-120, -40)
# pacman2 = vector(-80, -40)
fantasmas = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
    [vector(-140, 120), vector(-5, 0)],
    [vector(-140, -120), vector(0, 5)],
    [vector(40, 100), vector(0, -5)],
    [vector(80, -100), vector(-5, 0)]
]

# fmt: off
cenario = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def offset(ponto):
    """Retorna o deslocamento do ponto no cenário."""
    x = (floor(ponto.x, 20) + 200) / 20
    y = (180 - floor(ponto.y, 20)) / 20
    indice = int(x + y * 20)
    return indice

def valido(ponto):
    """Retorna True se o ponto for válido no cenário."""
    indice = offset(ponto)

    if cenario[indice] == 0:
        return False

    indice = offset(ponto + 19)

    if cenario[indice] == 0:
        return False

    return ponto.x % 20 == 0 or ponto.y % 20 == 0

def mundo():
    """Desenha o mundo usando o caminho."""
    turtle.bgcolor('black')
    caminho.color('blue')

    for indice in range(len(cenario)):
        tile = cenario[indice]

        if tile > 0:
            x = (indice % 20) * 20 - 200
            y = 180 - (indice // 20) * 20
            caminho.up()
            caminho.goto(x, y)
            caminho.down()
            caminho.begin_fill()

            for _ in range(4):
                caminho.forward(20)
                caminho.left(90)

            caminho.end_fill()

            if tile == 1:
                caminho.up()
                caminho.goto(x + 10, y + 10)
                caminho.dot(2, 'white')

def mover():
    """Move o Pacman e todos os fantasmas."""
    escritor.undo()
    escritor.write(estado['pontuacao'])

    turtle.clear()

    if valido(pacman + sentido):
        pacman.move(sentido)

    indice = offset(pacman)

    if cenario[indice] == 1:
        cenario[indice] = 2
        estado['pontuacao'] += 1

    turtle.up()
    turtle.goto(pacman.x + 10, pacman.y + 10)
    turtle.dot(20, 'yellow')

    # turtle.goto(pacman2.x + 10, pacman2.y + 10)
    turtle.dot(20, 'pink')

    for ponto, direcao in fantasmas:
        if valido(ponto + direcao):
            ponto.move(direcao)
        else:
            opcoes = [vector(20, 0), vector(-2, 0), vector(0, 20), vector(0, -2), vector(20, 0), vector(-2, 0), vector(0, 20), vector(0, -2)]
            plano = choice(opcoes)
            direcao.x = plano.x
            direcao.y = plano.y

        turtle.up()
        turtle.goto(ponto.x + 10, ponto.y + 10)
        turtle.dot(20, 'red')

    turtle.update()

    for ponto, _ in fantasmas:
        if abs(pacman - ponto) < 20:
            return

    turtle.ontimer(mover, 100)

def mudar_sentido(x, y):
    """Muda o sentido do Pacman se válido."""
    if valido(pacman + vector(x, y)):
        sentido.x = x
        sentido.y = y

turtle.setup(600, 600, 400, 0)
turtle.hideturtle()
turtle.tracer(False)
escritor.goto(160, 160)
escritor.color('white')
escritor.write(estado['pontuacao'])
turtle.listen()
turtle.onkey(lambda: mudar_sentido(5, 0), 'Right')
turtle.onkey(lambda: mudar_sentido(-5, 0), 'Left')
turtle.onkey(lambda: mudar_sentido(0, 5), 'Up')
turtle.onkey(lambda: mudar_sentido(0, -5), 'Down')
mundo()
mover()
turtle.mainloop()
