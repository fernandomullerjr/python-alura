
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 05 Opcional: quantas tentativas faltam?"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Opcional: quantas tentativas faltam?

Sempre é importante dar feedback ao usuário quando ele realiza alguma ação no sistema. No caso da forca, quando o jogador errar uma letra, queremos indicar isso, juntamente com quantas tentativas faltam. Em outras palavras queremos mostrar para o jogador quantas rodadas ele ainda pode jogar antes ser enforcado.

Que código poderíamos escrever para dar esse feedback ao jogador?



##  Opinião do instrutor

Uma possibilidade de código seria colocar uma chamada à função print dentro do else onde a variável erros é incrementada. Para concatenar o total de tentativas à string, usamos a função format.

~~~~python
else:
    erros += 1
    print("Ops, você errou! Faltam {} tentativas.".format(6-erros))
~~~~




- Jogo original:

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/005-implementando-o-encerramento-do-jogo/01-forca.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
['_', '_', '_', '_', '_', '_']
Qual letra? n
['_', '_', 'N', '_', 'N', '_']
Qual letra? x
['_', '_', 'N', '_', 'N', '_']
Qual letra? y
['_', '_', 'N', '_', 'N', '_']
Qual letra? b
['B', '_', 'N', '_', 'N', '_']
Qual letra? a
['B', 'A', 'N', 'A', 'N', 'A']
Você ganhou!
Fim do jogo
fernando@debian10x64:~$
fernando@debian10x64:~$
~~~~



- Jogo ajustado, contendo o status da quantidade de tentativas sendo impresso:

~~~~bash

fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/005-implementando-o-encerramento-do-jogo/05-forca-com-status-tentativas.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
['_', '_', '_', '_', '_', '_']
Qual letra? n
['_', '_', 'N', '_', 'N', '_']
Qual letra? x
Ops, você errou! Faltam 5 tentativas.
['_', '_', 'N', '_', 'N', '_']
Qual letra? y
Ops, você errou! Faltam 4 tentativas.
['_', '_', 'N', '_', 'N', '_']
Qual letra? b
['B', '_', 'N', '_', 'N', '_']
Qual letra? ç
Ops, você errou! Faltam 3 tentativas.
['B', '_', 'N', '_', 'N', '_']
Qual letra? t
Ops, você errou! Faltam 2 tentativas.
['B', '_', 'N', '_', 'N', '_']
Qual letra? q
Ops, você errou! Faltam 1 tentativas.
['B', '_', 'N', '_', 'N', '_']
Qual letra? z
Ops, você errou! Faltam 0 tentativas.
['B', '_', 'N', '_', 'N', '_']
Você perdeu!
Fim do jogo
fernando@debian10x64:~$
fernando@debian10x64:~$ date
Sun 28 Apr 2024 09:54:05 PM -03
fernando@debian10x64:~$
~~~~