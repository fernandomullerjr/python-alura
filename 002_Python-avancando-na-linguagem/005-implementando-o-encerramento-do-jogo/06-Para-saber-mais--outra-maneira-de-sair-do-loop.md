
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 06 Para saber mais: outra maneira de sair do loop"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  06 Para saber mais: outra maneira de sair do loop

Vimos nesse capítulo que as variáveis acertou e enforcou foram usadas para controlar a saída do loop. Enquanto elas não forem verdadeiras, o código dentro do loop será executado. Para que o loop seja encerrado, criamos atribuições para essas variáveis.

~~~~python
enforcou = erros == 6
acertou = "_" not in letras_acertadas
~~~~

Contudo, essa não é única maneira de sair de um loop. Podemos usar também a palavra reservada break que, quando executada, irá encerrar o loop naquele ponto. Como podemos alterar nosso código da forca para utilizar o break e sair do while?



## Opinião do instrutor

Uma possível solução seria o código abaixo. Repare que usamos um loop infinito (while(true)) e por isso temos que usar o comando break para interromper o laço:

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_", "_", "_", "_"]


    erros = 0
    print(len(palavra_secreta))
    print(letras_acertadas)

    while(True):

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

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)


    if("_" not in letras_acertadas):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")
~~~~




- Testand o jogo:

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/005-implementando-o-encerramento-do-jogo/06-forca.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
4
['_', '_', '_', '_']
Qual letra? m
['M', '_', '_', '_']
Qual letra? t
['M', '_', '_', '_']
Qual letra? y
['M', '_', '_', '_']
Qual letra? a
['M', 'A', '_', 'A']
Qual letra? c
['M', 'A', '_', 'A']
Qual letra? ç
Você ganhou!!
Fim do jogo
fernando@debian10x64:~$ date
Sun 28 Apr 2024 10:01:21 PM -03
fernando@debian10x64:~$
~~~~