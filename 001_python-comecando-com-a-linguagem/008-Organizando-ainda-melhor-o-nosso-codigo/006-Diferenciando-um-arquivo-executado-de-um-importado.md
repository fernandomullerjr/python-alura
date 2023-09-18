
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 8 - aula 06 Diferenciando um arquivo executado de um importado."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 06 Diferenciando um arquivo executado de um importado

## Transcrição

Não conseguimos mais jogar diretamente cada jogo porque o seu próprio arquivo não chama a sua função jogar(). Então, depois da função, vamos chamá-la:

~~~~python
# adivinhacao.py

import random

def jogar():
    # código omitido

jogar()
~~~~

Isso resolve o problema de jogar o jogo diretamente mas voltamos ao problema do vídeo anterior! Ao executarmos o arquivo jogos.py, como o próprio arquivo adivinhacao.py chama a função jogar(), ela será executada sem que queiramos isso.

Precisamos dar um jeito para que, quando executarmos o jogo de adivinhação diretamente, a função jogar() deve ser chamada, mas quando só o importamos, não queremos que a função seja chamada.

Programa principal vs Programa importado
Quando rodamos diretamente um arquivo no Python, ele internamente cria uma variável e a preenche. E através dessa variável podemos fazer uma consulta, pois se ela estiver preenchida, significa que o arquivo foi executado diretamente, mas se a variável não estiver preenchida, então significa que o arquivo só foi importado.

Essa variável é a __name__, e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente. Vamos então fazer if para verificar se ela está preenchida ou não:

~~~~python
# adivinhacao.py

import random

def jogar():
    # código omitido

if (__name__ == "__main__"):
    jogar()
~~~~


Podemos agora testar os dois casos, executar o arquivo diretamente e executar o arquivo jogos.py. Os dois estão funcionando, exatamente como queríamos. Falta fazermos a mesma coisa com o jogo da forca:

~~~~python
# forca.py

def jogar():
    # código omitido

if (__name__ == "__main__"):
    jogar()
~~~~


E com o arquivo jogos.py, colocando o seu código dentro da função escolhe_jogo() e chamando-a caso o programa seja o programa principal:

~~~~python
import forca
import adivinhacao

def escolhe_jogo():
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

if (__name__ == "__main__"):
    escolhe_jogo()
~~~~

Com isso vimos como diferenciar se o programa é o principal ou não, se ele está sendo executado diretamente ou só sendo importado. Na hora de importar um arquivo, ele lê o código da função, mas não o executa, pois ele não é o arquivo principal






# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 06 Diferenciando um arquivo executado de um importado


- Criado novo arquivo para o jogo de adivinhação:
/home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/008-Organizando-ainda-melhor-o-nosso-codigo/006-adivinhacao.py

adicionado ao final dele uma chamada para a função jogar:
jogar()


- Testando

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/008-Organizando-ainda-melhor-o-nosso-codigo/006-adivinhacao.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Defina o nível: 1
Tentativa 1 de 20
Digite o seu número: 55
Você digitou:  55
Você errou! O seu chute foi maior que o número secreto.
Tentativa 2 de 20
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Tentativa 3 de 20
Digite o seu número: 44
Você digitou:  44
Você errou! O seu chute foi menor que o número secreto.
Tentativa 4 de 20
Digite o seu número: 48
Você digitou:  48
Você acertou!
Fim do jogo
fernando@debian10x64:~$
fernando@debian10x64:~$ date
Sun 17 Sep 2023 10:56:35 PM -03
fernando@debian10x64:~$

~~~~