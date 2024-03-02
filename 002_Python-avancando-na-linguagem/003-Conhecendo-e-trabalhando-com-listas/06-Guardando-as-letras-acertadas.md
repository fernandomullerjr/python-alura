
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









# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 06 Guardando as letras acertadas


- Novo código do jogo de forca:

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip()           ### Função  str.strip([chars])   Remove por padrão, quando não é passado um parametro, apenas espaços em branco.

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

~~~~



Nesse código, a parte letras_acertadas[index] = letra é responsável por atualizar a lista letras_acertadas com a letra correta que o jogador acertou. Aqui está o que acontece:

    O jogo começa com a palavra secreta "banana" e uma lista de letras acertadas contendo seis sublinhados, indicando que nenhuma letra foi adivinhada ainda.

    O jogador faz um chute, digitando uma letra.

    O código percorre cada letra da palavra secreta usando um loop for.

    Para cada letra na palavra secreta, ele verifica se o chute do jogador corresponde à letra atual.

    Se a letra do chute corresponder à letra atual da palavra secreta (ignorando maiúsculas e minúsculas com chute.upper() == letra.upper()), a letra correta é colocada na posição correta na lista letras_acertadas. Isso é feito atribuindo letra à posição index na lista letras_acertadas.

    O index é incrementado em cada iteração do loop, garantindo que a letra correta seja atribuída à posição correta na lista letras_acertadas.

    Após o loop, a lista letras_acertadas é impressa para que o jogador veja quais letras ele acertou até agora.

Esse processo continua até que o jogador tenha adivinhado todas as letras corretamente ou até que ele tenha cometido erros suficientes para "enforcar" o boneco da forca.





O índice (index) é incrementado em cada iteração do loop para garantir que a letra correta seja atribuída à posição correta na lista letras_acertadas.

Aqui está o motivo pelo qual o índice é incrementado:

    No início do loop, o índice é definido como 0 (index = 0).

    À medida que o loop percorre cada letra na palavra secreta, o índice é usado para determinar a posição atual na lista letras_acertadas onde a letra correta deve ser atribuída.

    Depois que a letra correta é atribuída à posição index na lista letras_acertadas, o índice é incrementado em 1 (index = index + 1). Isso garante que na próxima iteração do loop, a próxima posição na lista letras_acertadas seja usada para a próxima letra da palavra secreta.

    Esse processo continua até que todas as letras da palavra secreta sejam verificadas.

Então, o incremento do índice permite que o código associe cada letra da palavra secreta à sua posição correspondente na lista letras_acertadas.




Vamos explorar com mais detalhes por que o índice (index) é incrementado em cada iteração do loop.

    Controle de posição na lista: A lista letras_acertadas é uma representação das letras que o jogador já acertou na palavra secreta. O objetivo é preencher essa lista com as letras corretas à medida que o jogador as acerta.

    Associação entre letra e posição na lista: O loop for letra in palavra_secreta: itera sobre cada letra na palavra secreta. Durante cada iteração, precisamos associar a letra atual à posição correta na lista letras_acertadas.

    Posição inicial na lista: No início do loop, o índice (index) é definido como 0 (index = 0). Isso significa que começamos a associar letras da palavra secreta à primeira posição na lista letras_acertadas.

    Atribuição da letra à posição correta: Quando encontramos uma letra na palavra secreta que corresponde ao chute do jogador, precisamos atribuir essa letra à posição correta na lista letras_acertadas. Para fazer isso, usamos o índice atual. Por exemplo, se encontramos a letra "a" na segunda posição da palavra secreta, precisamos atribuir "a" à segunda posição na lista letras_acertadas.

    Incremento do índice: Após atribuir a letra à posição correta na lista letras_acertadas, incrementamos o índice em 1 (index = index + 1). Isso nos prepara para a próxima iteração do loop, onde vamos associar a próxima letra da palavra secreta à próxima posição na lista letras_acertadas.

    Iteração sobre todas as letras da palavra secreta: Esse processo de associação letra-posição se repete para cada letra na palavra secreta até que todas as letras tenham sido verificadas.

Resumindo, o incremento do índice nos permite associar cada letra da palavra secreta à sua posição correspondente na lista letras_acertadas, garantindo que as letras corretas sejam atribuídas às posições corretas na lista.




O código entende que não precisa mais incrementar o índice quando o loop for termina de percorrer todas as letras da palavra secreta.

No Python, um loop for itera sobre todos os elementos de uma sequência até que não haja mais elementos para iterar. No caso deste código, o loop for letra in palavra_secreta: itera sobre cada letra na palavra secreta.

Quando o loop chega ao final da palavra secreta, não há mais letras para iterar, então ele simplesmente termina. Nesse momento, o índice index já terá sido incrementado até o valor da última posição na lista letras_acertadas.

Por exemplo, se a palavra secreta tiver 6 letras, após a última iteração do loop for, o índice index será igual a 5 (já que as posições na lista começam do zero). Assim, quando o loop terminar, o código não entrará novamente no loop, pois ele já percorreu todas as letras da palavra secreta. Isso é o que faz o código entender que não precisa mais incrementar o índice.






- Testando

python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/003-Conhecendo-e-trabalhando-com-listas/06-forca__v2.py

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/003-Conhecendo-e-trabalhando-com-listas/06-forca__v2.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
['_', '_', '_', '_', '_', '_']
Qual letra? a
['_', 'a', '_', 'a', '_', 'a']
Qual letra? G
['_', 'a', '_', 'a', '_', 'a']
Qual letra? N
['_', 'a', 'n', 'a', 'n', 'a']
Qual letra? v
['_', 'a', 'n', 'a', 'n', 'a']
Qual letra? w
['_', 'a', 'n', 'a', 'n', 'a']
Qual letra? y
['_', 'a', 'n', 'a', 'n', 'a']
Qual letra? J
['_', 'a', 'n', 'a', 'n', 'a']
Qual letra? B
['b', 'a', 'n', 'a', 'n', 'a']
Qual letra? Ç
['b', 'a', 'n', 'a', 'n', 'a']

~~~~