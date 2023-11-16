
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 2 - aula 01 Encontrando letras."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Encontrando letras

## Transcrição

Já temos o laço do jogo pronto, enquanto o usuário não acertou a palavra secreta e não se enforcou, ele continua jogando. Agora falta implementar a lógica do jogo.

## Capturando a entrada do usuário

Ao jogar, o usuário deve digitar uma letra, então devemos pedi-la para ele. Já fizemos isso no treinamento anterior, basta utilizar a função input para capturar a entrada do usuário:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")

    print("Jogando...")
~~~~

Com o chute do usuário em mãos, devemos procurar se essa letra existe dentro da palavra secreta. Mas como fazer isso?



## Encontrando a posição de uma letra em uma string

A palavra secreta é uma string, tipo str, e nesse tipo há uma função em que podemos procurar algo dentro da string. Essa função é a find, ao passar o chute do usuário para ela, a mesma retorna a posição na palavra em que a letra se encontra, começando da posição 0 (que representa a primeira letra). Por exemplo:

>>> palavra = "banana"
>>> palavra.find("b")
0
>>> palavra.find("n")
2

Caso a letra não exista na string, nos é retornado o número -1:

>>> palavra = "banana"
>>> palavra.find("z")
-1
Mas podemos reparar em um problema da função, pois ao pesquisar pela letra n, foi retornado o número 2, mas a letra n também existe na posição 4 da palavra, porém a função não faz isso, ela só retorna uma única posição, a primeira que ela encontrar. Por isso não vamos utilizar essa função. Então o que faremos?



## Iterando sobre a palavra

Resolveremos isso iterando sobre a palavra secreta. Faremos um laço em cima de cada letra, no nosso caso, na primeira iteração teremos a letra b, na segunda teremos a letra a, depois a n e assim até terminar a palavra. Com a letra em mãos, basta comparar com o chute do usuário.

Mas aí entramos em outra questão: como fazemos um laço em cima de uma palavra?

A palavra é uma sequência de letras, logo podemos utilizar o laço for! Por exemplo:

>>> palavra = "banana"
>>> for letra in palavra:
...     print(letra)
... 
b
a
n
a
n
a

Faremos isso no nosso jogo. Para cada letra da palavra, comparamos com o chute do usuário, e se o chute for igual à letra, podemos imprimi-lo:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")

    for letra in palavra_secreta:
        if (chute == letra):
            print(chute)

    print("Jogando...")
~~~~

Agora, ao executar o programa e procurar pela letra a, vemos o seguinte resultado:

~~~~bash
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? a
a
a
a
Jogando...
~~~~


Podemos melhorar ainda mais, exibindo a posição do chute na palavra, assim como a função find fazia.



## Exibindo a posição da letra

Temos que fazer isso na mão, então, fora do for, vamos criar a variável index, com o valor 0. E dentro do for, vamos incrementar essa variável a cada iteração:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")

    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            print(chute)
        index = index + 1

    print("Jogando...")
~~~~

Com a letra e a posição em mãos, vamos imprimi-los, utilizando a interpolação de strings:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")

    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1

    print("Jogando...")
~~~~

Ao executar novamente o nosso jogo:

~~~~bash
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? n
Encontrei a letra n na posição 2
Encontrei a letra n na posição 4
Jogando...
~~~~


Mas se digitarmos uma letra em maiúsculo, por exemplo a letra A, a mesma não é encontrada na palavra. O ideal é não fazermos essa diferenciação entre letras minúsculas e maiúsculas. Vamos resolver esse problema no próximo capítulo :)









# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Encontrando letras

fernando@debian10x64:~$ python3
Python 3.8.3 (default, Jun  4 2023, 19:15:23)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> palavra = "banana"
>>>
>>> type(palavra)
<class 'str'>
>>>
>>> palavra.find("b")
0
>>>
>>> palavra.find("n")
2
>>>
>>> palavra.find("w")
-1
>>>
>>>
>>> palavra.find("n")
2
>>> for letra in palavra:
...      print(letra)
...
b
a
n
a
n
a
>>>



Nessa saída, você primeiro criou uma variável chamada palavra e atribuiu a ela o valor "banana". Em seguida, você usou o método find() para encontrar a posição da letra "b" na palavra, que é 0 (pois a indexação em Python começa do zero). Em seguida, você encontrou a posição da letra "n", que é 2, e a posição da letra "w", que não existe na palavra, então o método find() retornou -1.

Finalmente, você usou um loop for para iterar sobre cada letra na palavra e imprimiu letra por letra. O loop for percorre a string palavra e, a cada iteração, a variável letra contém uma única letra da palavra. Então, o comando print(letra) imprime cada letra em uma nova linha, resultando na saída letra por letra:

b
a
n
a
n
a

User
como a variável "letra" é iterada? como o Python sabe que deve percorrer cada letra?

ChatGPT

Em Python, quando você utiliza um loop for para iterar sobre uma sequência de dados, como uma string, lista ou tupla, o Python automaticamente percorre os elementos dessa sequência um por um. No seu exemplo, a variável letra é uma variável de iteração que assume o valor de cada elemento na sequência, que, no seu caso, é a string "banana".

Quando você escreve:

~~~~python

for letra in palavra:
    print(letra)
~~~~

O Python entende que você deseja percorrer cada caractere na string palavra. Durante cada iteração do loop, a variável letra assume o valor do próximo caractere na string, começando do primeiro caractere até o último. O loop continua até que todos os caracteres na string tenham sido percorridos.

O Python "sabe" que deve percorrer cada letra da string porque você expressou explicitamente essa intenção ao usar o loop for com a variável de iteração letra e a string palavra. O loop for é uma estrutura de controle que permite percorrer sequências de dados sem a necessidade de indexação manual. O Python cuida da iteração internamente, garantindo que cada elemento na sequência seja acessado e processado conforme necessário.



- Testando

python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? j
Jogando...
Qual letra? n
n
n
Jogando...
Qual letra? a
a
a
a
Jogando...
Qual letra? ^CTraceback (most recent call last):
  File "/home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py", line 24, in <module>
    jogar()
  File "/home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py", line 13, in jogar
    chute = input("Qual letra? ")
KeyboardInterrupt

fernando@debian10x64:~$

~~~~



- Editando o código, adicionando o index e a interpolação:

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        
        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

~~~~


- Testando novamente:

python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py

~~~~bash

fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? a
Encontrei a letra a na posição 1
Encontrei a letra a na posição 3
Encontrei a letra a na posição 5
Jogando...
Qual letra? n
Encontrei a letra n na posição 2
Encontrei a letra n na posição 4
Jogando...

~~~~

Nesse código, o Python utiliza um loop for para percorrer cada letra na palavra secreta ("banana") e um contador index para acompanhar a posição da letra na string. O código compara a letra inserida pelo usuário (chute) com cada letra na palavra_secreta. Se houver uma correspondência, o Python imprime a letra e a posição (índice) na qual foi encontrada na palavra secreta.

Aqui está uma explicação passo a passo do trecho relevante do código:

    O usuário insere uma letra como chute (chute = input("Qual letra? ")).

    O loop for letra in palavra_secreta: percorre cada letra na string palavra_secreta.

    Para cada letra na palavra_secreta, o código compara chute com letra usando a condição if (chute == letra):.

    Se a letra inserida pelo usuário (chute) for igual à letra atual sendo verificada no loop, o Python imprime a letra (letra) e a posição (index) na qual foi encontrada na palavra secreta. O índice é atualizado a cada iteração do loop (index = index + 1), então ele representa a posição da letra na palavra secreta.

    O loop continua até que todas as letras na palavra_secreta tenham sido verificadas ou até que o usuário acerte a letra e decida sair do loop.

Por exemplo, se o usuário inserir "a" como chute, o Python imprimirá algo semelhante a:

css

Encontrei a letra a na posição 1
Encontrei a letra a na posição 3

Isso indica que a letra "a" foi encontrada nas posições 1 e 3 na palavra secreta "banana".


como ele entendeu que o valor é 3?
ChatGPT

No código fornecido, o valor da posição (ou índice) é rastreado usando a variável index. A variável index começa com o valor 0 antes de entrar no loop for. A cada iteração do loop, ela é incrementada em 1 usando a linha de código index = index + 1. Como a indexação em Python começa em 0, a primeira letra da palavra secreta ("banana") está na posição 0, a segunda letra está na posição 1, a terceira letra está na posição 2 e assim por diante.

Quando o código encontra uma correspondência entre a letra inserida pelo usuário (chute) e a letra atual na palavra secreta (letra), ele imprime a letra (letra) e o valor atual da variável index. Como index é incrementado a cada iteração, ele representa a posição atual da letra na palavra secreta.

Por exemplo, se o código já passou por duas letras na palavra secreta ("banana") e encontrou duas correspondências antes de encontrar a terceira correspondência, o valor de index será 2. Assim, o código imprimirá:

css

Encontrei a letra a na posição 2

Isso indica que a letra "a" foi encontrada na terceira posição (índice 2) na palavra secreta "banana".











## Testando

- Dia 15/11/2023

- Verificando o funcionamento e a posição que o jogo informa:

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? a
Encontrei a letra a na posição 1
Encontrei a letra a na posição 3
Encontrei a letra a na posição 5
Jogando...
Qual letra? b
Encontrei a letra b na posição 0
Jogando...
Qual letra? ^CTraceback (most recent call last):
  File "/home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py", line 26, in <module>
    jogar()
  File "/home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/01-forca.py", line 13, in jogar
    chute = input("Qual letra? ")
KeyboardInterrupt

fernando@debian10x64:~$


~~~~