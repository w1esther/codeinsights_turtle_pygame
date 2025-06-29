# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 10.2


"""Paint, para desenhar formas.

Exercícios:

1. Adicionar uma cor. ok
2. Completar o círculo. ok
3. Completar o retângulo. ok
4. Completar o triângulo. ok
5. Adicionar parâmetro de largura. ok
"""

import turtle
from freegames import vector


def linha(inicio, fim):
    """Desenha uma linha do ponto de início ao ponto de fim."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.goto(fim.x, fim.y)


def quadrado(inicio, fim):
    """Desenha um quadrado do ponto de início ao ponto de fim."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(fim.x - inicio.x)
        turtle.left(90)

    turtle.end_fill()


def circulo(inicio, fim):
    """Desenha um círculo do ponto de início ao ponto de fim."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.begin_fill()

    turtle.circle(fim.x - inicio.y)

    turtle.end_fill()


def retangulo(inicio, fim):
    """Desenha um retângulo do ponto de início ao ponto de fim."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(fim.x - inicio.x)
        turtle.left(90)
        turtle.forward((fim.x - inicio.y)/2)
        turtle.left(90)
    
    turtle.end_fill()


def triangulo(inicio, fim):
    """Desenha um triângulo do ponto de início ao ponto de fim."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.begin_fill()

    for _ in range(3):
        turtle.forward(fim.x - inicio.x)
        turtle.left(120)


def toque(x, y):
    """Armazena o ponto inicial ou desenha a forma."""
    inicio = estado['inicio']

    if inicio is None:
        estado['inicio'] = vector(x, y)
    else:
        forma = estado['forma']
        fim = vector(x, y)
        forma(inicio, fim)
        estado['inicio'] = None


def armazenar(chave, valor):
    """Armazena um valor no estado usando a chave."""
    estado[chave] = valor


estado = {'inicio': None, 'forma': linha}

tela = turtle.Screen()
tela.title("Espessura da Linha")
tela.setup(300, 200)

espessura_linha = tela.numinput("Espessura Linha", "Digite um valor para espessura da linha:")
turtle.width(espessura_linha)


turtle.setup(420, 420, 370, 0)
turtle.onscreenclick(toque)
turtle.listen()
turtle.onkey(turtle.undo, 'u')
turtle.onkey(lambda: turtle.color('black'), 'K')
turtle.onkey(lambda: turtle.color('white'), 'W')
turtle.onkey(lambda: turtle.color('green'), 'G')
turtle.onkey(lambda: turtle.color('blue'), 'B')
turtle.onkey(lambda: turtle.color('red'), 'R')
turtle.onkey(lambda: turtle.color('pink'), 'P')
turtle.onkey(lambda: turtle.color('orange'), 'O')
turtle.onkey(lambda: armazenar('forma', linha), 'l')
turtle.onkey(lambda: armazenar('forma', quadrado), 's')
turtle.onkey(lambda: armazenar('forma', circulo), 'c')
turtle.onkey(lambda: armazenar('forma', retangulo), 'r')
turtle.onkey(lambda: armazenar('forma', triangulo), 't')
turtle.mainloop()
