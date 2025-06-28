# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 3.10


import turtle

import festa_dançante

d = festa_dançante.cria_dançarino("Principal", "Centro")

a = festa_dançante.cria_dançarinos_apoio(10, "Apoio", "Circulo")
festa_dançante.defina('Principal', 'color', 'green')
festa_dançante.defina('Apoio', 'color', 'orange')

# Essa linha abaixo está comentada para não dar erro de sintaxe

festa_dançante.a_cada_compasso(festa_dançante.muda_palco, 2)
                               
# Comece removendo o # do inicio dela e depois alterando os ???
# pelos valores dos argumentos. Então acrescente outras chamadas
# a a_cada_compasso para alterar outras propriedades das dançarinas 

turtle.mainloop()


	
