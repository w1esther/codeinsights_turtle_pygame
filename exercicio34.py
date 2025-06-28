# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 3.4


import turtle
import festa_dançante

dançarino_um = festa_dançante.cria_dançarino("Um", "Direita")
dançarino_dois = festa_dançante.cria_dançarino("Dois", "Esquerda") 

turtle.onkey(dançarino_um.aleatório, "Up") 
turtle.onkey(None, "Down")

turtle.mainloop()

