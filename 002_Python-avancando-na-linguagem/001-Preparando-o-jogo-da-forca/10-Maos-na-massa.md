
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 1 - aula 10 Mãos na massa."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  10 Mãos na massa

Chegou a hora de colocarmos em prática o que aprendemos neste capítulo. Em linhas gerais, precisamos de uma palavra secreta e vamos começar a criar o game loop, para verificar se o usuário já se enforcou ou acertou.

Para tal, abra o arquivo forca.py:

1) Dentro da função jogar, declare uma nova variável, que guarda a palavra secreta:

palavra_secreta = "banana"


2) Depois crie mais duas, para guardar o status enforcou e acertou, inicializando-as com False:

~~~~python
enforcou = False
acertou = False
~~~~

3) Para o loop, use um laço com condição de entrada, verificando se o usuário não enforcou e nem acertou:

~~~~python
while (not acertou and not enforcou):
    print("Jogando...")
~~~~


4) Rode o código no PyCharm e fique atento a possíveis erros. Ao rodar, o jogo fica em um loop infinito.

Na opinião do instrutor você encontrará o código completo.





Opinião do instrutor

Segue uma possível implementação, ainda bem simples:

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        print("Jogando...")

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
~~~~

No próximo capítulo, vamos capturar e tratar a entrada do usuário. Pronto para continuar?