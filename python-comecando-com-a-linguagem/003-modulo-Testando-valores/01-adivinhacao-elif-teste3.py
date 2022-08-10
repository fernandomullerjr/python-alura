# TESTE 3
# Usando 1 if e 1 elif, se cair na condição, senão é a outra.
# Mas para esses casos, podemos fazer um else com uma condição de entrada, o elif. 
# Vamos utilizá-lo para deixar o código mais semântico, já que na prática não há diferença:

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")