
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 8 - aula 01 Importando arquivos dentro de outros."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Importando arquivos dentro de outros

## Transcrição

Se conseguimos executar o jogo dentro do PyCharm, também conseguimos rodar o jogo na linha de comando, no terminal. Dentro do diretório do projeto jogos, basta executar:

python3 adivinhacao.py

No próximo treinamento, criaremos mais um jogo, a forca. Então já vamos deixar o seu arquivo preparado, criando o forca.py, também dentro do projeto jogos. Dentro desse arquivo, vamos deixar as mensagens de início e fim de jogo, semelhante ao jogo de adivinhação:

~~~~python
print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

print("Fim do jogo")
~~~~


Oferecendo todos os jogos ao usuário
Vamos oferecer os dois jogos ao usuário, ou seja, devemos perguntar ao usuário qual jogo ele quer executar, jogar. Mas onde vamos colocar essa funcionalidade? A ideia é não misturar os jogos, deixar cada um em um arquivo separado. Então vamos criar um novo arquivo com essa funcionalidade, o arquivo jogos.py, perguntando qual jogo ele quer escolher jogar:

~~~~python
print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")
~~~~


Agora vamos capturar a opção do usuário e verificar qual jogo ele escolheu:

~~~~python
print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
elif (jogo == 2):
    print("Jogando adivinhação")
~~~~


Importando arquivos
Ótimo, mas se queremos chamar um arquivo dentro de outro, precisamos importá-lo, algo parecido com o que fizemos com o módulo random:

~~~~python
import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
elif (jogo == 2):
    print("Jogando adivinhação")
~~~~


O problema do import
Podemos executar para ver como está ficando:

*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Fim do jogo
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Defina o nível:


Ué, o que aconteceu? Quando importamos um arquivo no Python, ele o executa! Podemos reparar que ele executou o arquivo forca.py e logo depois o adivinhacao.py. Mas obviamente não queremos isso, só queremos executar o arquivo quando nós quisermos! E é isso que faremos no próximo vídeo.







# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Importando arquivos dentro de outros


- Criando arquivo do jogo de Forca apenas:

python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/007-Nivel-e-pontuacao/001-jogo-com-niveis.py


~~~~python

import random

print("*********************************")
print("Bem vindo ao jogo de Forca!")
print("*********************************")



print("Fim do jogo")
~~~~




- Criando arquivo que vai ter todos os jogos
/home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/008-Organizando-ainda-melhor-o-nosso-codigo/001-jogos.py

~~~~python
import forca
import adivinhacao


print("*********************************")
print("Escolha o seu jogo!")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
elif (jogo == 2):
    print("Jogando adivinhação")
~~~~



- Testando

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/008-Organizando-ainda-melhor-o-nosso-codigo/001-jogos.py
*********************************
Bem vindo ao jogo de Forca!
*********************************
Fim do jogo
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Defina o nível: 1
Tentativa 1 de 20
Digite o seu número: 55
Você digitou:  55
Você errou! O seu chute foi menor que o número secreto.
Tentativa 2 de 20
Digite o seu número: 88
Você digitou:  88
Você errou! O seu chute foi menor que o número secreto.
Tentativa 3 de 20
Digite o seu número: 99
Você digitou:  99
Você acertou!
Fim do jogo
*********************************
Escolha o seu jogo!
*********************************
(1) Forca (2) Adivinhação
Qual jogo? 1
Jogando forca
fernando@debian10x64:~$
fernando@debian10x64:~$ date
Sat 16 Sep 2023 10:51:36 PM -03
fernando@debian10x64:~$

~~~~



Ué, o que aconteceu? Quando importamos um arquivo no Python, ele o executa! Podemos reparar que ele executou o arquivo forca.py e logo depois o adivinhacao.py. Mas obviamente não queremos isso, só queremos executar o arquivo quando nós quisermos! E é isso que faremos no próximo vídeo.
