
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
