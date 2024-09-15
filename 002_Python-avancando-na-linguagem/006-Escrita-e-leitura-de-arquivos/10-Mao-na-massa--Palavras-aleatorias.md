Agora que já sabemos ler um arquivo, podemos implementar a funcionalidade de escolher aleatoriamente a palavra secreta de um arquivo.

1 - De início devemos abrir o arquivo, e como já sabemos é uma boa prática fechá-lo ao final:

def jogar():

    arquivo = open("palavras.txt", "r")

    arquivo.close()

2 - Depois temos que criar uma lista e percorrer o arquivo. Cada linha do arquivo deve ser guardada nessa lista:

def jogar():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha)

    arquivo.close()

3 - Precisamos remover o \n ao final da linha, fazendo um strip nela:

def jogar():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

4 - Agora que já temos todas as palavras na lista devemos acessá-las aleatoriamente. Para isso, vamos importar a biblioteca random?

import random

5 - Com a biblioteca já disponível temos que acessar uma das palavras incluídas na nossa lista. Para isso será necessário gerar um número com a posição aleatória. O número gerado deveria ser apenas de índices válidos na lista: 0 até o tamanho da lista:

    numero = random.randrange(0, len(palavras))

6 - Com o número gerado basta agora pegarmos a palavra secreta correspondente a essa posição:

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()











## 
Opinião do instrutor

O seu código final deveria estar como o seguinte:

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

    numero = random.randrange(0,len(palavras))
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