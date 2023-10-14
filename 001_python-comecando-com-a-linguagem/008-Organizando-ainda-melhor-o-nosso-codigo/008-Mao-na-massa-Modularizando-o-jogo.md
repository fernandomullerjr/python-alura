
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 8 - aula  08 Mão na massa: Modularizando o jogo"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 08 Mão na massa: Modularizando o jogo

## Preparando adivinhacao.py
Vamos transformar o nosso arquivo adivinhacao.py em um verdadeiro módulo, que pode ser importado ou executado diretamente.

Para tal, coloque todo o código, menos o import, dentro de uma função com o nome jogar:

~~~~python
# adivinhacao.py

import random

def jogar():
    # código omitido
~~~~


No fim do arquivo, adicione o if que garante a execução como programa principal:

~~~~python
if(__name__ == "__main__"):
    jogar()
~~~~

Pronto, o adivinhacao.py já foi modularizado!

Preparando o jogo de Forca
Para podermos testar corretamente a importação, vamos preparar o arquivo forca.py. No PyCharm, dentro do seu projeto jogos, crie um novo arquivo forca.py.

Nele, adicione a função jogar e o if que testa a variável __name__:

~~~~python
# forca.py

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
~~~~


Escolha do jogo
Para podermos escolher entre o jogo de forca e o jogo de adivinhação, crie mais um arquivo dentro do projeto jogos. Chame o arquivo de jogos.py.

Adicione o código abaixo no arquivo, para importar os módulos (forca e adivinhacao) e implementar a lógica de escolher o jogo:

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
    forca.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
Repare que chamamos a função jogar de cada módulo.
~~~~


Executando o jogo
Dentro do PyCharm, rode o arquivo jogos.py. Fique atento para pegar possíveis erros de sintaxe.