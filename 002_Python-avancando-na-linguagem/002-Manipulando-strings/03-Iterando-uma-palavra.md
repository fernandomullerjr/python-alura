
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 2 - aula 03 Iterando em uma palavra."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  03 Iterando em uma palavra

Uma palavra nada mais é do que uma sequência de caracteres. Tanto isso é verdade, que podemos usar o laço for para iterar. Nesse contexto, iterar significa receber a cada iteração uma letra da palavra.

Sabendo disso, qual das opções abaixo itera corretamente através da palavra Alura?

Alternativa correta
palavra = "Alura"
for letra in palavra:
    if(letra == "l"):
    print("Achou!")

Alternativa correta
palavra = "Alura"
for letra in palavra:
    if(letra == "l"):
        print("Achou!")

Correto! Respeita a indentação do Python.

Alternativa correta
palavra = "Alura"
for palavra in letra:
    if(letra == "l"):
        print("Achou!")

Nesse curso vamos falar ainda muito mais sobre sequências, mas já saiba que uma string não é a única sequência no mundo Python!