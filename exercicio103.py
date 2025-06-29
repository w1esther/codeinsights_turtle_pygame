# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid 10.3

import turtle
from random import randint


# Configuração da tela
tela = turtle.Screen()
tela.title("Jogo de Adivinhação")
tela.setup(650, 650)

# Criar objeto para exibir mensagens
caneta = turtle.Turtle()
caneta.hideturtle()
caneta.penup()
caneta.color('pink')

# Número aleatório
inicio, fim = 1, 1000000
secreto = randint(inicio, fim)
tentativas = 0


# Exibir mensagem na tela
def mensagem(texto):
    caneta.clear()
    caneta.goto(0, 100)
    caneta.write(texto, align="center", font=("Times New Roman", 20, "normal"))


mensagem(f"Pensei em um número entre {inicio} e {fim}.\nTente adivinhar!")

# Capturar palpite do usuário
def verificar_palpite():
    global tentativas
    palpite = tela.numinput("Adivinhe", "Digite seu palpite:", minval=inicio, maxval=fim)

    if palpite is None:
        return  # Se o usuário cancelar, não faz nada

    tentativas = tentativas + 1

    if tentativas == 2:
        mensagem("Voce atingiu o numero maximo de tentativas!")
        exit(botao)

    elif palpite < secreto:
        mensagem(f"Mais alto! você fez {tentativas} tentativas, tente novamente.")
    elif palpite > secreto:
        mensagem(f"Mais baixo! você fez {tentativas} tentativas, tente novamente.")
    else:
        mensagem(f"Parabéns! Acertou em {tentativas} tentativas.")

# Botão de tentativa
botao = turtle.Turtle()
botao.color('pink')
botao.penup()
botao.goto(0, -50)
botao.write("Clique aqui para tentar", align="center", font=("Times New Roman", 16, "normal"))
botao.onclick(lambda x, y: verificar_palpite())

turtle.mainloop()
