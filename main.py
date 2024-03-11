import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    while tentativas == 0:
        print("Escolha um nivel de dificuldade: \n 1  nivel facil \n 2 nivel medio \n 3 nivel dificil ")
        escolha = int(input("=> "))
        if escolha == 1:
            tentativas = 10
        elif escolha == 2:
            tentativas = 7
        elif escolha == 3:
            tentativas = 5
        else:
            print("Escolha invalida.")
    print(f"Você tem {tentativas} tentativas.")

    while tentativas > 0:
        chute = int(input("Digite seu chute: "))

        if chute < numero_secreto:
            print("O número secreto é maior.")
        elif chute > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("Parabéns! Você acertou!")
            return

        tentativas -= 1
        if tentativas > 0:
            print(f"Você tem mais {tentativas} tentativas.")

    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)

jogo_adivinhacao()

