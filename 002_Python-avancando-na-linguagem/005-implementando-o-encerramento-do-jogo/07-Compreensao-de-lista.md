
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 07 Compreensão de lista"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#   07 Compreensão de lista

## Transcrição

Atualmente, a nossa palavra secreta é banana, que possui seis letras. Por isso a lista de palavras acertadas possui seis _. Mas se trocarmos a palavra secreta? Precisamos alterar a quantidade de _ na lista, de acordo com o número de letras da nova palavra.

Meio trabalhoso, né? Então vamos tornar isso mais dinâmico.


## Inicializando a lista de acordo com o número de letras da palavra

Queremos que a inicialização da lista de palavras acertadas seja dinâmica, baseada na quantidade de letras que houver na palavra secreta. Já sabemos implementar isso, podemos criar a lista vazia, e para cada letra na palavra secreta, adicionamos um _ à ela:

~~~~python
palavra_secreta = "banana".upper()
letras_acertadas = []

for letra in palavra_secreta:
    letras_acertadas.append("_")
~~~~

Perfeito, está funcionando! Mas há uma forma mais interessante de fazer isso.


## Realizando um laço dentro da inicialização da lista

Quando inicializamos a lista, queremos inicializá-la com um caractere _ para cada letra na palavra secreta. Só que com Python, podemos fazer isso diretamente, dentro da inicialização da lista:

~~~~python
palavra_secreta = "banana".upper()
letras_acertadas = ["_" for letra in palavra_secreta]
~~~~

Essa funcionalidade do Python se chama List Comprehension, em português, Compreensão de lista.




# ###################################################################################################################################################################
# ###################################################################################################################################################################
#   07 Compreensão de lista

- Criando o v2
/home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/005-implementando-o-encerramento-do-jogo/07-forca__v2.py


~~~~python
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
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

if(__name__ == "__main__"):
    jogar()
~~~~












# ###################################################################################################################################################################
# ###################################################################################################################################################################
#   RESUMO