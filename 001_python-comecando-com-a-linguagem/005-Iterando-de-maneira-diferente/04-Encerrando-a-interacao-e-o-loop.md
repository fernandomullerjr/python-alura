

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






# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Testes dos códigos

- Novo código do jogo, usando break:

~~~~python
numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
~~~~

- Testando o break
/home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/005-modulo-Iterando-de-maneira-diferente/04-break.py

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/005-modulo-Iterando-de-maneira-diferente/04-break.py
Tentativa 1 de 3
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Tentativa 2 de 3
Digite o seu número: 42
Você digitou:  42
Você acertou!
Fim do jogo
fernando@debian10x64:~/cursos/python/python-alura$
~~~~





- Novo código do jogo, usando break:

~~~~python
numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

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
~~~~


- Testando
/home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/005-modulo-Iterando-de-maneira-diferente/04-continue.py

python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/005-modulo-Iterando-de-maneira-diferente/04-continue.py

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/005-modulo-Iterando-de-maneira-diferente/04-continue.py
Tentativa 1 de 3
Digite o seu número: 14555
Você digitou:  14555
Você deve digitar um número entre 1 e 100!
Tentativa 2 de 3
Digite o seu número: -68
Você digitou:  -68
Você deve digitar um número entre 1 e 100!
Tentativa 3 de 3
Digite o seu número: 22
Você digitou:  22
Você errou! O seu chute foi menor que o número secreto.
Fim do jogo
fernando@debian10x64:~/cursos/python/python-alura$
~~~~



# PUSH

git status
git add .
git commit -m "Modulo 5 - aula 04 - Encerrando a interação e o loop. pt2"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status













# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Dia 27/05/2023

# GPT

Esse código é um jogo de adivinhação em que o jogador deve tentar adivinhar um número secreto. Vamos analisar seu funcionamento passo a passo:

    A primeira linha declara uma variável chamada numero_secreto e atribui o valor 42 a ela. Esse é o número que o jogador precisa adivinhar.
    A segunda linha declara uma variável chamada total_de_tentativas e atribui o valor 3 a ela. Essa variável indica quantas tentativas o jogador terá para acertar o número secreto.
    O bloco de código dentro do loop for será executado por cada rodada do jogo. O loop é controlado pela variável rodada, que começa com o valor 1 e vai até o valor de total_de_tentativas + 1.
    A linha print("Tentativa {} de {}".format(rodada, total_de_tentativas)) exibe a mensagem indicando a tentativa atual e o número total de tentativas.
    A linha chute_str = input("Digite o seu número: ") solicita ao jogador que digite um número.
    A linha print("Você digitou: ", chute_str) exibe o número que o jogador digitou.
    A linha chute = int(chute_str) converte a entrada do jogador, que é uma string, em um número inteiro e atribui o valor à variável chute.
    As variáveis acertou, maior e menor são usadas para verificar se o jogador acertou o número secreto, se o chute foi maior que o número secreto ou se foi menor, respectivamente.
    O bloco if (chute < 1 or chute > 100): verifica se o chute está fora do intervalo válido (entre 1 e 100). Se estiver, exibe a mensagem "Você deve digitar um número entre 1 e 100!" e continua para a próxima rodada do loop usando o comando continue.
    O bloco if (acertou): verifica se o jogador acertou o número secreto. Se sim, exibe a mensagem "Você acertou!" e encerra o jogo usando o comando break.
    Se o jogador não acertar o número secreto, o programa verifica se o chute foi maior ou menor. Se foi maior, exibe a mensagem "Você errou! O seu chute foi maior que o número secreto." Se foi menor, exibe a mensagem "Você errou! O seu chute foi menor que o número secreto."
    Ao final de cada rodada, o loop volta ao início para a próxima rodada, caso o número de tentativas não tenha sido alcançado.
    Depois que o loop termina, ou seja, quando o jogador acerta o número secreto ou esgota todas as tentativas, o código exibe a mensagem "Fim do jogo".

Esse é um jogo simples de adivinhação em que o jogador tem três tentativas para adivinhar o número secreto. O código verifica se o chute está dentro do intervalo válido, informa se o chute foi maior ou menor que o número secreto e encerra o jogo quando o jogador acerta ou esgota as tentativas.
User
Como funcionam estas linhas exatamente?

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
ChatGPT

Vamos analisar essas linhas separadamente:

    acertou = numero_secreto == chute

    Nessa linha, estamos comparando se o valor da variável numero_secreto é igual ao valor da variável chute. O operador == verifica a igualdade entre os dois valores. Se forem iguais, a variável acertou receberá o valor booleano True, indicando que o jogador acertou o número secreto. Caso contrário, receberá o valor False.

    maior = chute > numero_secreto

    Aqui, estamos verificando se o valor da variável chute é maior do que o valor da variável numero_secreto. O operador > verifica a relação de maior que entre os dois valores. Se o chute for maior, a variável maior receberá o valor booleano True. Caso contrário, receberá o valor False.

    menor = chute < numero_secreto

    Nessa linha, estamos verificando se o valor da variável chute é menor do que o valor da variável numero_secreto. O operador < verifica a relação de menor que entre os dois valores. Se o chute for menor, a variável menor receberá o valor booleano True. Caso contrário, receberá o valor False.

Essas linhas são utilizadas para determinar se o chute do jogador foi maior, menor ou igual ao número secreto. Dependendo dessas condições, são exibidas mensagens ao jogador informando se ele acertou o número ou se seu chute foi maior ou menor. Essas informações são usadas posteriormente no fluxo do programa para tomar decisões sobre o jogo.


Como funciona o == exatamente?

ChatGPT

O operador == é um operador de igualdade usado para comparar dois valores e determinar se eles são iguais. Ele retorna o valor booleano True se os valores forem iguais e False caso contrário.

Quando você usa o operador ==, o Python verifica se os dois operandos têm o mesmo valor. Se tiverem, a expressão retorna True; caso contrário, retorna False. É importante destacar que o operador == compara apenas o valor dos operandos, não o tipo.

Aqui estão alguns exemplos de uso do operador ==:

~~~~python
x = 5
y = 10
z = 5

print(x == y)  # False, pois 5 não é igual a 10
print(x == z)  # True, pois 5 é igual a 5

texto1 = "Olá"
texto2 = "olá"

print(texto1 == texto2)  # False, pois "Olá" não é igual a "olá"
~~~~

No contexto do código que você forneceu, a expressão numero_secreto == chute está sendo usada para verificar se o número digitado pelo jogador (chute) é igual ao número secreto (numero_secreto). A variável acertou recebe o valor True se os números forem iguais e False caso contrário. Isso permite determinar se o jogador acertou o número secreto ou não.



Como funcionam as chaves e o format nesta linha de código?

print("Tentativa {} de {}".format(rodada, total_de_tentativas))
ChatGPT

Nessa linha de código, as chaves {} e o método format() são usados para formatar uma string de saída que exibe o número da tentativa atual e o número total de tentativas.

Vou explicar o funcionamento em detalhes:

    A string "Tentativa {} de {}" é a string de formato que será usada como modelo para a criação da saída formatada. As chaves {} são espaços reservados onde os valores serão inseridos.

    O método format() é chamado na string de formato. Ele permite substituir os espaços reservados pelas informações desejadas.

    Os argumentos do método format() são fornecidos dentro dos parênteses e estão separados por vírgulas. No caso dessa linha de código específica, são passadas duas variáveis: rodada e total_de_tentativas.

    O método format() substitui cada espaço reservado {} na string de formato pelos valores dos argumentos na ordem em que foram fornecidos. No exemplo dado, o valor de rodada será inserido no primeiro espaço reservado {} e o valor de total_de_tentativas será inserido no segundo espaço reservado {}.

    O resultado é uma nova string formatada que contém os valores substituídos nos espaços reservados. Essa nova string é o resultado da chamada do método format() e é exibida usando a função print().

Em resumo, a linha de código print("Tentativa {} de {}".format(rodada, total_de_tentativas)) exibe uma mensagem indicando a tentativa atual e o número total de tentativas. Os valores de rodada e total_de_tentativas são inseridos nos espaços reservados {} da string de formato usando o método format().