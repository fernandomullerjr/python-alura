
import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    #A variável será inicializada com 0, e faremos um if para verificar o nível escolhido, se o ele for fácil, o usuário terá 20 tentativas, se for médio terá 10, e se for difícil terá 5 tentativas
    total_de_tentativas = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # O bloco de código dentro do loop for será executado por cada rodada do jogo. 
    # O loop é controlado pela variável rodada, que começa com o valor 1 e vai até o valor de total_de_tentativas + 1.
    for rodada in range(1, total_de_tentativas + 1):
        # Os valores de rodada e total_de_tentativas são inseridos nos espaços reservados {} da string de formato usando o método format().
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        #   Nessa linha, estamos comparando se o valor da variável numero_secreto é igual ao valor da variável chute. 
        #  O operador == verifica a igualdade entre os dois valores. Se forem iguais, a variável acertou receberá o valor booleano True, indicando que o jogador 
        #  acertou o número secreto. Caso contrário, receberá o valor False.
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

    print("Fim do jogo")