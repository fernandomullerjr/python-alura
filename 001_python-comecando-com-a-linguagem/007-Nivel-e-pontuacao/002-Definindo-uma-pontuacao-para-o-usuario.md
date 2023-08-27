
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 7 - aula 02 Definindo uma pontuação para o usuário."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 02 Definindo uma pontuação para o usuário

## Transcrição

Com os níveis definidos, vamos agora calcular uma pontuação. Ela funcionará da seguinte maneira, o usuário começa o jogo com 1000 pontos, e a cada rodada que ele não acerta o número secreto, ele perderá pontos. Quanto mais distante for o chute, mais pontos o usuário irá perder. Por exemplo, se o número secreto for 40, e o usuário chutar 20, ele irá perder 20 pontos, que corresponde à distância entre os valores.

Vamos começar definindo a variável com 1000 pontos:

~~~~python
pontos = 1000
~~~~

Após isso, o usuário irá perder pontos caso ele erre o chute, logo temos que implementar isso dentro da condição else:

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


Vamos definir a variável pontos_perdidos, que subtrai o chute do número secreto:

~~~~python
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = numero_secreto - chute
~~~~


Depois, vamos subtrair os pontos perdidos da pontuação total:

~~~~python
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = numero_secreto - chute
    pontos = pontos - pontos_perdidos
~~~~

Isso funciona caso o usuário chute um número menor que o número secreto, mas e se for maior? Por exemplo, se o número secreto for 40 e o usuário chutar 60, de acordo com o cálculo do nosso código os pontos perdidos serão -20, e ao subtrair esse valor da pontuação total, ela irá aumentar!

Então queremos fazer a subtração dos pontos perdidos, mas caso essa subtração tenha como resultado um número negativo, queremos que "esquecer" esse sinal, queremos sempre o número absoluto.

E para extrair o número absoluto, existe mais uma função built-in, a abs():

~~~~python
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
~~~~

Por fim, falta exibirmos a pontuação final ao usuário. Vamos alterar a mensagem de acerto do usuário, acrescentando a pontuação total. Faremos uso novamente da interpolação de strings:

~~~~python
if (acertou):
    print("Você acertou e fez {} pontos!".format(pontos))
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
~~~~

Com isso chegamos ao final do nosso jogo! No próximo capítulo veremos um pouco sobre linguagens compiladas e interpretadas, entre outros assuntos. Até lá!







# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 02 Definindo uma pontuação para o usuário


Vamos definir a variável pontos_perdidos, que subtrai o chute do número secreto:

~~~~python
if (acertou):
    print("Você acertou!")
    break
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = numero_secreto - chute
~~~~




Temos o seguinte caso, neste exemplo o número fica ok, fica positivo:

~~~~python
    pontos_perdidos = numero_secreto - chute   #40-20 = 20
~~~~


Porém, neste exemplo o número fica negativo:

~~~~python
    pontos_perdidos = numero_secreto - chute   #40-60 = -20
~~~~


Então precisamos usar uma função built-in do Python:
abs

https://docs.python.org/3/library/functions.html#abs
<https://docs.python.org/3/library/functions.html#abs>
abs(x)

    Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). If the argument is a complex number, its magnitude is returned.






- Testando a função


fernando@debian10x64:~$ python3
Python 3.8.3 (default, Jun  4 2023, 19:15:23)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>> abs(-10)
10
>>>
>>>
>>> abs(11)
11
>>>
>>> abs(-11)
11
>>>




- Ajustando o código

~~~~python
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
~~~~





Por fim, falta exibirmos a pontuação final ao usuário. Vamos alterar a mensagem de acerto do usuário, acrescentando a pontuação total. Faremos uso novamente da interpolação de strings:

~~~~python
if (acertou):
    print("Você acertou e fez {} pontos!".format(pontos))
~~~~


O código que você compartilhou é escrito em linguagem de programação Python e serve para exibir uma mensagem formatada na saída. Vou explicar o que cada parte do código faz:

    print: Isso é uma função embutida no Python que exibe texto na saída padrão (normalmente no terminal ou console).

    "Você acertou e fez {} pontos!": Esta é uma string que contém um espaço reservado {} onde um valor será inserido usando o método format().

    .format(pontos): Isso é um método aplicado à string que formata a mensagem. O valor contido na variável pontos será colocado no espaço reservado {} na string.

Portanto, se você tiver uma variável chamada pontos com um valor, digamos, 100, o código imprimirá algo assim:

Você acertou e fez 100 pontos!

Basicamente, o código é utilizado para exibir uma mensagem de sucesso junto com o valor da variável pontos de uma forma formatada na saída.







O método format() é usado para formatar strings em Python, permitindo que você crie strings dinâmicas onde pode inserir valores variáveis. Ele substitui os espaços reservados {} em uma string por valores que você passa como argumentos.

Aqui está como o método format() funciona:

    A string contém espaços reservados onde os valores serão inseridos. Esses espaços reservados são indicados por chaves {}.

    Você chama o método format() na string e passa os valores que deseja inserir nos espaços reservados como argumentos para o método.

    O método format() substitui os espaços reservados pelos valores fornecidos e retorna a string formatada resultante.

Por exemplo:

~~~~python

nome = "Alice"
idade = 30

mensagem = "Olá, meu nome é {} e tenho {} anos.".format(nome, idade)
print(mensagem)
~~~~

Neste exemplo, o método format() substituirá os espaços reservados {} na string pela variável nome (que contém "Alice") e pela variável idade (que contém 30), resultando na seguinte saída:

    Olá, meu nome é Alice e tenho 30 anos.

O método format() oferece muita flexibilidade para formatar strings de maneira complexa, incluindo formatação numérica, alinhamento de texto e especificação de precisão decimal, entre outras coisas. Ele é uma ferramenta poderosa para criar mensagens e saídas personalizadas em Python.



- Exemplo:

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/007-Nivel-e-pontuacao/002-metodo-format.py
Olá, meu nome é Alice e tenho 30 anos.
fernando@debian10x64:~$

~~~~










- Código final do jogo com pontuação:

~~~~python

import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
#A variável será inicializada com 0, e faremos um if para verificar o nível escolhido, se o ele for fácil, o usuário terá 20 tentativas, se for médio terá 10, e se for difícil terá 5 tentativas
total_de_tentativas = 0

pontos = 1000

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
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")
~~~~





- Testando o jogo com pontuação:

~~~~bash


fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/007-Nivel-e-pontuacao/002-jogo-com-pontuacao.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Defina o nível: 1
Tentativa 1 de 20
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi maior que o número secreto.
Tentativa 2 de 20
Digite o seu número: 22
Você digitou:  22
Você errou! O seu chute foi maior que o número secreto.
Tentativa 3 de 20
Digite o seu número: 11
Você digitou:  11
Você errou! O seu chute foi maior que o número secreto.
Tentativa 4 de 20
Digite o seu número: 4
Você digitou:  4
Você errou! O seu chute foi menor que o número secreto.
Tentativa 5 de 20
Digite o seu número: 8
Você digitou:  8
Você errou! O seu chute foi maior que o número secreto.
Tentativa 6 de 20
Digite o seu número: 7
Você digitou:  7
Você errou! O seu chute foi maior que o número secreto.
Tentativa 7 de 20
Digite o seu número: 6
Você digitou:  6
Você acertou e fez 947 pontos!
Fim do jogo
fernando@debian10x64:~$
fernando@debian10x64:~$ date
Sat 26 Aug 2023 11:03:07 PM -03
fernando@debian10x64:~$

~~~~