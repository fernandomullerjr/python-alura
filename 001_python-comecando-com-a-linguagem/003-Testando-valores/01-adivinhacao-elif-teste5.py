# TESTE 5
# Podemos melhorar a legibilidade do nosso código, para que outros programadores que possam vir a desenvolver conosco o entendam melhor. 
# Vamos deixar nossas condições mais claras, o que significa chute == numero_secreto, por exemplo? 
# Que o usuário acertou, logo vamos extrair essa condição para uma variável:
# acertou = chute == numero_secreto
# Agora a condição if fica um pouco mais clara. Vamos fazer a mesma coisa para as outras duas condições:
# maior = chute > numero_secreto
# menor = chute < numero_secreto
# Podemos testar e ver que tudo continua funcionando como antes, mas agora com um código um pouco mais legível. 

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")