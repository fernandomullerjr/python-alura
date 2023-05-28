

# ################################################################################################################################################################
# ################################################################################################################################################################
# ################################################################################################################################################################
# 05 - Mão na massa: Dando dicas

Como apresentado no vídeo, implemente a lógica no seu jogo para mostrar se o chute do usuário foi maior ou menor do que o número secreto.

Para tal:

Crie para cada condição uma variável: acertou, maior e menor.
Teste o chute e imprima uma mensagem.
Mãos à obra!




- Código criado

~~~~python
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
elif (maior):
    print("Você errou! O seu chute foi maior que o número secreto.")
elif (menor):
    print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
~~~~





# ################################################################################################################################################################
# ################################################################################################################################################################
# ################################################################################################################################################################
# Opinião do instrutor

Para sua comparação, segue o código completo:

~~~~python
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou " , chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Parabéns! Você acertou!")
else:
    if(maior):
        print("O seu chute foi maior do que o número secreto!")
    elif(menor):
        print("O seu chute foi menor do que o número secreto!")

print("Fim do jogo")
~~~~





# ################################################################################################################################################################
# ################################################################################################################################################################
# ################################################################################################################################################################
# Testes adicionais

- Criando um código que traz os tipos dos valores das variáveis utilizadas:

~~~~python
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
elif (maior):
    print("Você errou! O seu chute foi maior que o número secreto.")
elif (menor):
    print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")

print("*********************************")
print("Tipos dos valores e variáveis deste código:")
print(type(acertou))
print(type(maior))
print(type(menor))
print("*********************************")
~~~~



- Validando:

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/003-modulo-Testando-valores/05-Mao-na-massa-e-imprimindo-os-tipos.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Fim do jogo
*********************************
Tipos dos valores e variáveis deste código:
<class 'bool'>
<class 'bool'>
<class 'bool'>
*********************************
fernando@debian10x64:~/cursos/python/python-alura$
~~~~