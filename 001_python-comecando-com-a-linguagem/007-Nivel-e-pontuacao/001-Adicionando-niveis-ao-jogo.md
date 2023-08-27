

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 7 - aula 01 Adicionando níveis ao jogo."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Adicionando níveis ao jogo

## Transcrição
Vamos adicionar níveis ao nosso jogo, e conforme o nível vai ficando mais difícil, menos tentativas o usuário terá.


Começaremos perguntando ao usuário qual nível de dificuldade ele quer:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

# resto do código comentado
~~~~



E capturaremos o que ele digitar, já convertendo o valor para inteiro e guardando em uma variável:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

# resto do código comentado
~~~~


Agora falta mudar o total de tentativas baseado no nível que o usuário escolher. A variável será inicializada com 0, e faremos um if para verificar o nível escolhido, se o ele for fácil, o usuário terá 20 tentativas, se for médio terá 10, e se for difícil terá 5 tentativas:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# resto do código comentado
~~~~

Com isso conseguimos definir os níveis de dificuldade no nosso jogo. No próximo vídeos definiremos pontuação!




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Adicionando níveis ao jogo




Começaremos perguntando ao usuário qual nível de dificuldade ele quer:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

# resto do código comentado
~~~~




E capturaremos o que ele digitar, já convertendo o valor para inteiro e guardando em uma variável:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

# resto do código comentado
~~~~



## OBSERVAÇÃO
Este input carrega um valor em string.
É necessário converter ele para inteiro.





- Convertendo o input para inteiro.
- Agora falta mudar o total de tentativas baseado no nível que o usuário escolher. A variável será inicializada com 0, e faremos um if para verificar o nível escolhido, se o ele for fácil, o usuário terá 20 tentativas, se for médio terá 10, e se for difícil terá 5 tentativas:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# resto do código comentado
~~~~











- Testando o jogo com níveis:

~~~~bash

fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/007-Nivel-e-pontuacao/001-jogo-com-niveis.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Defina o nível: 1
Tentativa 1 de 20
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Tentativa 2 de 20
Digite o seu número: 44
Você digitou:  44
Você acertou!
Fim do jogo
fernando@debian10x64:~$ date
Sat 26 Aug 2023 09:52:40 PM -03
fernando@debian10x64:~$



fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/007-Nivel-e-pontuacao/001-jogo-com-niveis.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Defina o nível: 2
Tentativa 1 de 10
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Tentativa 2 de 10
Digite o seu número: 44
Você digitou:  44
Você errou! O seu chute foi maior que o número secreto.
Tentativa 3 de 10
Digite o seu número: 42
Você digitou:  42
Você errou! O seu chute foi maior que o número secreto.
Tentativa 4 de 10
Digite o seu número: 37
Você digitou:  37
Você errou! O seu chute foi menor que o número secreto.
Tentativa 5 de 10
Digite o seu número: 38
Você digitou:  38
Você errou! O seu chute foi menor que o número secreto.
Tentativa 6 de 10
Digite o seu número: 39
Você digitou:  39
Você errou! O seu chute foi menor que o número secreto.
Tentativa 7 de 10
Digite o seu número: 40
Você digitou:  40
Você errou! O seu chute foi menor que o número secreto.
Tentativa 8 de 10
Digite o seu número: 41
Você digitou:  41
Você acertou!
Fim do jogo
fernando@debian10x64:~$ date
Sat 26 Aug 2023 09:56:32 PM -03
fernando@debian10x64:~$

~~~~