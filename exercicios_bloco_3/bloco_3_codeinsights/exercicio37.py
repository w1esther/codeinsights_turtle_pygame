# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 3.7


import turtle

import festa_dançante

dancarino = turtle.Turtle()
dancarino.shape('turtle')

festa_dançante.cria_dançarino(dancarino, 'Centro')
festa_dançante.cria_dançarinos_apoio(10, 'Apoio', 'Circulo')
festa_dançante.muda_palco()



turtle.mainloop()

	
