
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 11  Mãos na massa: encerrando o jogo"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  11  Mãos na massa: encerrando o jogo

No jogo da forca, implemente a lógica para que o jogo dê apenas 6 chances para o jogador tentar acertar a palavra. Primeiro, crie uma variável chamada erros fora do loop e inicialize-a com zero.

~~~~python
erros = 0
~~~~

Em seguida, coloque uma condição dentro do loop para verificar se o jogador acertou a letra. Ela deve englobar a inicialização da variável index e o loop for. Crie um else para incrementar a variável erros.

~~~~python
if(chute in palavra_secreta):
     index = 0
     for letra in palavra_secreta:
         if(chute == letra):
             letras_acertadas[index] = letra
         index = index + 1
else:
     erros = erros + 1
~~~~

No final do loop, atualize a variável enforcou para que ela se torne verdadeira quando a quantidade de erros for 6. Teste o jogo colocando 6 letras erradas e verifique que o jogo termina!

~~~~python
enforcou = erros == 6
~~~~

Agora implemente a lógica para que o jogo termine quando o jogador acertar a palavra. Crie mais uma linha no final do loop para atualizar a variável acertou com a verificação se o caracter underscore não existe em letras_acertadas. Teste a aplicação e coloque as letras da palavra secreta. Confirme que o jogo termina.

~~~~python
acertou = "_" not in letras_acertadas
~~~~

Apesar do jogo encerrar, o jogador ainda não sabe se acertou ou foi enforcado. Após o loop e antes da impressão da mensagem Fim do jogo, coloque um if para imprimir Você ganhou!! caso ele tenha vencido a forca e Você perdeu! caso contrário. Teste novamente sua aplicação.

~~~~python
if(acertou):
     print("Você ganhou!!")
else:
     print("Você perdeu!!")
~~~~

Inicialize a variável letras_acertadas dinamicamente a partir de qualquer palavra secreta. Utilize o recurso List Comprehension para criar um laço dentro da inicialização da lista.

~~~~python
letras_acertadas = ["_" for letra in palavra_secreta]
~~~~


## Opinião do instrutor

Seu código deverá ficar parecido com o abaixo:

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
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






