# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 3.3


import turtle
import festa_dançante

# Crie o seu dançarino aqui

dancarinos = turtle.Turtle()
dancarinos.shape('turtle')
dancarinos = festa_dançante.cria_dançarino(dancarinos, 'Centro')

turtle.onkey(dancarinos.anda_esquerda, 'Left')
turtle.onkey(dancarinos.anda_direita, 'Right')

turtle.mainloop()