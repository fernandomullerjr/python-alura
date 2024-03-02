
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 3 - aula 06 Guardando as letras acertadas."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 06 Guardando as letras acertadas

## Transcrição

Agora que já conhecemos um pouco como a lista funciona, chegou a hora de utilizá-la no nosso jogo. Existem diversas formas de implementar essa funcionalidade, mas aqui faremos da seguinte forma: como queremos exibir os espaços vazios primeiro, criaremos uma lista com eles, na mesma quantidade de letras da palavra secreta:

~~~~python
palavra_secreta = "banana"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]
~~~~

Atualmente isso tudo está fixo, caso queiramos mudar a palavra secreta, teremos que mudar os espaços vazios. Mas não se preocupe, tornaremos isso dinâmico mais à frente.
Adicionando as letras acertadas à lista

Já temos a posição da letra, que chamamos de index. Logo, caso o chute seja correto, basta guardar a letra dentro da lista, na sua posição correta:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print("Jogando...")
~~~~


E após adicionar a letra, após o for, imprimimos a nossa lista:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print(letras_acertadas)
~~~~


Podemos executar o jogo, ao acertar uma letra, a palavra é exibida com a mesma preenchida:

~~~~python
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? b
['b', '_', '_', '_', '_', '_']
Qual letra? a
['b', 'a', '_', 'a', '_', 'a']
~~~~

A saída ainda não está visualmente agradável, mas melhoraremos isso. Para ficar ainda melhor, vamos exibir a lista no início do jogo também:

~~~~python
print(letras_acertadas)

while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print(letras_acertadas)
~~~~

Com isso, avançamos mais ainda na implementação do nosso jogo!