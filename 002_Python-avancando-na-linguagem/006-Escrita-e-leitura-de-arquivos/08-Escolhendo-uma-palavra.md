
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 6 - 08 Escolhendo uma palavra."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  08 Escolhendo uma palavra

### Transcrição

Agora que já sabemos ler de um arquivo, podemos implementar a funcionalidade de escolher aleatoriamente a palavra secreta de um arquivo.
Lendo e guardando as linhas do arquivo

A primeira coisa que devemos fazer é abrir o arquivo, e como já sabemos, vamos fechá-lo:

~~~~python
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")



    arquivo.close()
~~~~

Agora, vamos criar uma lista e fazer um laço, acessando cada linha e guardando-as nessa lista:

~~~~python
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha)

    arquivo.close()
~~~~

Mas precisamos remover o \n ao final da linha, fazendo um strip nela:

~~~~python
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
~~~~

Agora já temos todas as palavras na lista, mas como selecionar uma delas aleatoriamente?


### Gerando um número aleatório

Sabemos que cada elemento da lista possui uma posição, e vimos no treinamento anterior como gerar um número aleatório, vamos relembrar?

A biblioteca que sabe gerar um número aleatório é a random. Vamos testá-la no terminal do Python 3, primeiro importando-a:

>>> import random

Para gerar o número aleatório, utilizamos a biblioteca e chamamos a função randrange, que recebe o intervalo de valores que o número aleatório deve estar. Então vamos passar o valor 0 (equivalente à primeira posição da nossa lista) e 4 (lembrando que o número é exclusivo, ou seja, o número aleatório será entre 0 e 3, equivalente à última posição da nossa lista):

>>> import random
>>> random.randrange(0, 4)
0
>>> random.randrange(0, 4)
1
>>> random.randrange(0, 4)
3
>>> random.randrange(0, 4)
1
>>> random.randrange(0, 4)
3

Sabendo disso, vamos implementar esse código no nosso jogo.


### Selecionando a palavra

Primeiramente, devemos importar a biblioteca. Vamos gerar um número de 0 até a quantidade de palavras da nossa lista, ou seja, vamos utilizar a função len, para saber o tamanho da lista:

~~~~python
import random

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
~~~~

Agora que temos o número aleatório, vamos utilizá-lo como índice para acessar a lista e atribuir essa palavra à variável palavra_secreta:

~~~~python
import random

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
~~~~


Podemos executar o jogo agora, e perceber que a palavra é selecionada aleatoriamente!

Mas agora o nosso arquivo, a nossa função cresceu bastante, com várias funcionalidades e responsabilidades. Então, no próximo capítulo, organizaremos melhor o nosso código, separando-o em funções e deixando-o mais fácil de entender.








# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  08 Escolhendo uma palavra


- ANTES

~~~~PYTHON
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
~~~~



- Ajustando
adicionando import:
import random

e o código

~~~~python
import random

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
~~~~


e removendo o trecho:
    palavra_secreta = "maça".upper()


- DEPOIS

~~~~PYTHON
import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
~~~~


- Testando
/home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos/08-forca.py

~~~~bash
fernando@debian10x64:~$ cd /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos
fernando@debian10x64:~/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos$
fernando@debian10x64:~/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos$
fernando@debian10x64:~/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos$
fernando@debian10x64:~/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos$
fernando@debian10x64:~/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos$
fernando@debian10x64:~/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos/08-forca.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
['_', '_', '_', '_', '_', '_', '_', '_']
Qual letra? m
['M', '_', '_', '_', '_', '_', '_', '_']
Qual letra? o
['M', '_', '_', '_', '_', '_', '_', '_']
Qual letra? e
['M', 'E', '_', '_', '_', '_', '_', '_']
Qual letra? l
['M', 'E', 'L', '_', '_', '_', '_', '_']
Qual letra? a
['M', 'E', 'L', 'A', '_', '_', '_', 'A']
Qual letra? n
['M', 'E', 'L', 'A', 'N', '_', '_', 'A']
Qual letra? c
['M', 'E', 'L', 'A', 'N', 'C', '_', 'A']
Qual letra? i
['M', 'E', 'L', 'A', 'N', 'C', 'I', 'A']
Você ganhou!!
Fim do jogo
fernando@debian10x64:~/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos$ date
Sun 07 Jul 2024 01:33:56 AM -03
fernando@debian10x64:~/cursos/python/python-alura/002_Python-avancando-na-linguagem/006-Escrita-e-leitura-de-arquivos$
~~~~






