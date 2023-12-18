
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 2 - aula 06 Grandes poderes trazem grandes responsabilidades."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 07 Mãos na massa

Chegou a hora de colocarmos em prática o que aprendemos neste capítulo. Em linhas gerais, dentro do loop, devemos perguntar ao jogador o seu chute da palavra secreta. Por enquanto, exibiremos apenas se o chute foi encontrado ou não, inclusive sua posição na string.

Todas as alterações acontecem dentro do arquivo forca.py.

1) Dentro de um loop while, nosso famoso game loop, vamos perguntar qual a letra do chute. Só não esqueça de usar a função .strip() para remover espaços em branco à direita e à esquerda da letra digitada:

~~~~python
while (not acertou and not enforcou):
    chute = input("Qual letra? ")
    chute = chute.strip()
~~~~

2) Agora que já temos o chute do jogador, podemos compará-lo com cada letra de palavra_secreta. Lembre-se que uma string pode ser iterada através de for. Para evitarmos diferenças entre maiúsculas e minúsculas, faça com que a comparação considere tanto o chute quanto a letra iterada em maiúscula. Por fim, crie a variável index para guardar a posição da letra encontrada, pois no final queremos exibir essa informação para o usuário:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1
    print("Jogando...")
~~~~

3) Rode e teste o seu código. Ainda estamos executando um loop infinito e por isso é preciso terminar cada execução do jogo explicitamente pelo PyCharm.

Na opinião do instrutor você encontrará o código completo.





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
#