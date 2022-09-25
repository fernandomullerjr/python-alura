

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 5 - aula 04 - Encerrando a interação e o loop."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04 - Encerrando a interação e o loop

# Transcrição

No nosso jogo, sabemos que o número secreto é fixo e definido com o valor 42, por enquanto. Vamos jogar e digitar esse valor de primeira:


*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite o seu número: 42
Você digitou:  42
Você acertou!
Tentativa 2 de 3
Digite o seu número:

Acertamos o número, mas ainda temos uma segunda e terceira tentativas! Não faz muito sentido isso né? Se nós ganhamos, temos que parar as rodadas, não devemos continuar.




# Parando o laço

Dentro do if, se acertarmos, devemos parar e sair do laço. Para isso existe um comando do Python, assim como outras linguagens, o break, que faz com que saiamos do laço:

~~~~python
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
~~~~


Podemos agora jogar novamente e...:

*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite o seu número: 42
Você digitou:  42
Você acertou!
Fim do jogo
Ótimo! Acertamos o número e o jogo foi encerrado, sem mais rodadas.





# Limitando o número a ser digitado

Vamos limitar o número que o usuário deve digitar, de 1 a 100. Vamos deixar isso claro para ele alterando a mensagem do input:

~~~~python
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    ## resto do código comentado
~~~~

Só que agora não devemos aceitar valores fora desse limite, logo vamos verificar o número digitado, e se ele for menor que 1 OU (em Python, a palavra chave or) maior que 100, vamos exibir uma mensagem para o usuário:

~~~~python
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")

## resto do código comentado
~~~~

Mas não faz sentido continuarmos executando o código do loop se o valor não estiver no intervalo exigido. O que queremos não é sair do laço, e sim continuar para a próxima rodada, acabando com a iteração. Para isso existe a palavra chave continue:

~~~~python
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

## resto do código comentado
~~~~

Esse comando faz com que a iteração do laço acabe, e comece a próxima. Vamos testar:

*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite um número entre 1 e 100: 0
Você digitou:  0
Você deve digitar um número entre 1 e 100!
Tentativa 2 de 3
Digite um número entre 1 e 100:
Perfeito! O número digitado era incorreto, então fomos para a próxima tentativa.

Então vimos aqui o break, que acaba, encerra o laço; e o continue, que acaba, encerra a iteração, continuando para a próxima.