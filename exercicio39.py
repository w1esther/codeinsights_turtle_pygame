# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 3.9


import turtle

import festa_dançante

dancarino1 = festa_dançante.cria_dançarino('principal1', 'Centro')
dancarino1.setx(-45)
dancarino1.speed(10)
dancarino1.color('pink')
turtle.ontimer(dancarino1.faz_rodopio, 4000)

dancarino2 = festa_dançante.cria_dançarino('pincipal 2', 'Centro')
dancarino2.setx(45)
dancarino2.speed(10)
dancarino2.color('purple')
turtle.ontimer(dancarino2.faz_rodopio, 4000)

festa_dançante.cria_dançarinos_apoio(10, 'apoio', 'Circulo')
festa_dançante.defina('apoio', 'color', 'red')

turtle.mainloop()

	


	
