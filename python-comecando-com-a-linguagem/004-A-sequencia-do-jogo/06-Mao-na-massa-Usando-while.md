
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 06 - Mão na massa: Usando while."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 06 - Mão na massa: Usando while

Vamos implementar o loop do nosso jogo usando o laço com while. Para isso:

1) Defina duas novas variáveis, total_de_tentativas e rodada no início do jogo:

~~~~python
total_de_tentativas = 3
rodada = 1
~~~~


2) Use o while para testar se ainda há rodadas:

~~~~python
while (rodada <= total_de_tentativas):
    chute_str = input("Digite o seu número: ")
    #resto omitido
~~~~


3) Logo após o while, imprima a rodada e as tentativas usando a função format:

~~~~python
while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # resto do código omitido
~~~~



4) Depois do elif, mas antes do último print, incremente a variável rodada:

~~~~python
rodada = rodada + 1
~~~~


5) Salve e rode o seu código no PyCharm. Fique atento à saída.





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Opinião do instrutor

Segue o código com uma possível implementação. Sempre tenha cuidado com as indentações, o código abaixo usa 4 espaços em todo lugar:

~~~~python
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

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

    rodada = rodada + 1

print("Fim do jogo")
~~~~