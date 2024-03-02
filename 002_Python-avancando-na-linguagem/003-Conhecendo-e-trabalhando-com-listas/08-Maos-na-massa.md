
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 3 - aula 08 Mãos na massa."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 08 Mãos na massa

Vamos aproveitar o nosso novo conhecimento em listas para fazer com que a nossa forca se lembre das letras acertadas pelo nosso jogador.

1- De início crie uma nova lista chamada letras_acertadas abaixo da variável palavra_secreta. Aproveite e inicie esta lista com 6 elementos do caractere "_", para representar uma letra faltando. Por enquanto estamos fazendo com um número fixo de letras, mas em breve melhoraremos isto também.

letras_acertadas = ["_", "_", "_", "_", "_", "_"]

2- Já sabemos quando um usuário acerta uma letra, afinal fazemos isto no if que já temos:

if(chute.upper() == letra.upper()):
    print("Encontrei a letra {} na posição {}".format(chute, index))

Mas agora, em vez de apenas imprimirmos uma mensagem ao acertar, vamos substituir no nosso array de letras faltando. Como já temos o índice da letra, basta substituir naquela posição do array pela letra que acertamos:

if (chute.upper() == letra.upper()):
    letras_acertadas[index] = letra

3- Para que o jogador acompanhe o resultado a cada chute que ele der, após o laço for imprima também a lista de letras_acertadas para que ele veja como ele está indo no jogo:

for letra in palavra_secreta:
    ...
    ...
print(letras_acertadas)

4- E claro, para dar uma dica ao nosso jogador de quantas letras a palavra tem, vamos colocar acima do while um print inicial para que ele veja de início qual o tamanho da palavra:

print(letras_acertadas)

while (not acertou and not enforcou):
...

Faça o teste e veja na resposta se seu código está batendo com o do instrutor.
Opinião do instrutor

O seu código final deve estar parecido com este:

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()