# TESTE 4
# Podemos melhorar a legibilidade do nosso código, para que outros programadores que possam vir a desenvolver conosco o entendam melhor. 
# Vamos deixar nossas condições mais claras, o que significa chute == numero_secreto, por exemplo? 
# Que o usuário acertou, logo vamos extrair essa condição para uma variável:
# acertou = chute == numero_secreto

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")