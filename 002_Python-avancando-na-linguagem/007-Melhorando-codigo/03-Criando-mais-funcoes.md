
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 7 - 03 Criando mais funções."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Criando mais funções

## Transcrição

Vamos continuar com a refatoração do nosso código, criando funções.

### Função para pedir o chute do jogador

Criaremos a função pede_chute(), que ficará com o código que pede o chute do usuário, remove os espaços antes e depois, e o coloca em caixa alta. Não podemos nos esquecer de retornar o chute:

~~~~python
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

    # restante do código omitido

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute
~~~~


### Função para colocar o chute do usuário na posição correta da lista

Ainda temos o código que coloca o chute na posição correta, dentro da lista. Vamos colocá-lo dentro da função marca_chute_correto():

~~~~python
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto()
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")

def marca_chute_correto():
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
~~~~

Mas a função marca_chute_correto() precisa ter acesso a três valores: palavra_secreta, chute e letras_acertadas. Então vamos passar esses valores por parâmetro:

~~~~python
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
~~~~

Função para imprimir as mensagens de vencedor e perdedor do jogo

Por fim, vamos remover a mensagem de fim de jogo e exportar os códigos que imprimem as mensagens de vencedor e perdedor do jogo:

~~~~python
import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

    print("Fim do jogo")

def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")
~~~~

Agora o nosso código está muito mais organizado e legível.














# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Criando mais funções

Criaremos a função pede_chute(), que ficará com o código que pede o chute do usuário, remove os espaços antes e depois, e o coloca em caixa alta. Não podemos nos esquecer de retornar o chute:

~~~~python
def jogar():
    while (not acertou and not enforcou):
        chute = pede_chute()
    # restante do código omitido

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute
~~~~




Ainda temos o código que coloca o chute na posição correta, dentro da lista. Vamos colocá-lo dentro da função marca_chute_correto():

~~~~python
def jogar():
    # restante do código omitido
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto()
        else:
            erros += 1
    # restante do código omitido
def marca_chute_correto():
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
~~~~

Mas a função marca_chute_correto() precisa ter acesso a três valores: palavra_secreta, chute e letras_acertadas. Então vamos passar esses valores por parâmetro:

~~~~python
def jogar():
    # restante do código omitido
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
    # restante do código omitido
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
~~~~






# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESUMO

### Pontos importantes

- Sempre deixar o init ao final do arquivo
if(__name__ == "__main__")


- Passar todos os parametros para a função, que no caso são as variáveis que a função vai precisar neste caso, pois estão fora do seu escopo:
Mas a função marca_chute_correto() precisa ter acesso a três valores: palavra_secreta, chute e letras_acertadas. Então vamos passar esses valores por parâmetro:

~~~~python
def jogar():
    # restante do código omitido
    while (not acertou and not enforcou):
        chute = pede_chute()
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
    # restante do código omitido

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
~~~~