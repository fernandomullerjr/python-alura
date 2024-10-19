
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 7 - 07 Mãos na Massa: Exportando o código para funções."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 07 Mãos na Massa: Exportando o código para funções

Neste capítulo, vamos organizar o nosso código para que ele fique mais fácil de manter e para que sigamos as boas práticas.

1 - Crie a função imprime_mensagem_abertura(), para imprimir a mensagem inicial do jogo:

~~~~python
def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
~~~~

2 - Crie a função carrega_palavra_secreta(), que será responsável pela leitura do arquivo e inicialização da palavra secreta. Lembre-se que, como a função irá inicializar a palavra secreta, ela deve retorná-la, assim teremos acesso à palavra fora da função:

~~~~python
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
~~~~

Na hora de chamar a função, como ela retorna a palavra secreta, você pode guardá-la em uma variável!

3 - Crie a função inicializa_letras_acertadas(), que será responsável por inicializar a lista de letras acertadas com o caractere _. Como ela precisa acessar a palavra secreta, que não existe dentro da função, não esqueça de passar a palavra por parâmetro:

~~~~python
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]
~~~~

4 - Agora, crie a função pede_chute(), responsável por pedir o chute do usuário e guardá-lo na variável chute. Não se esqueça de, ao final da função, retornar o chute do usuário:

~~~~python
def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute
~~~~

5 - Para o código que coloca o chute do usuário na posição correta, dentro da lista, crie a função marca_chute_correto(). Ela precisa ter acesso a três valores: palavra_secreta, chute e letras_acertadas, então passe-os por parâmetro para a função:

~~~~python
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
~~~~

6 - Exporte os códigos que imprimem as mensagens de vencedor e perdedor do jogo para as funções imprime_mensagem_vencedor() e imprime_mensagem_perdedor(), respectivamente:

~~~~python
def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")
~~~~

Por fim, chame todas essas funções dentro da função jogar(), você irá perceber que ela ficará bem mais enxuta e legível.





## Opinião do instrutor

Ao chamar todas a funções dentro da função jogar(), ela ficará assim:

~~~~python
def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
~~~~