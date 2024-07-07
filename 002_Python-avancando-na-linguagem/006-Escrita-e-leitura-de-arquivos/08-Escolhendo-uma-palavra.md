
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
Gerando um número aleatório

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
Selecionando a palavra

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