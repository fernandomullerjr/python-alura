


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 01 - Laço com while."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Laço com While

# Transcrição

Queremos dar mais de uma oportunidade para o usuário tentar acertar o número secreto, já que é um jogo de adivinhação. A primeira ideia é repetir o código, desde a função input até o bloco do elif. Ou seja, para cada nova tentativa que quisermos dar ao usuário, copiaríamos esse código novamente.

Só que copiar código sempre é uma má prática, queremos escrever o nosso código apenas uma vez, e repeti-lo. Se queremos repetir o código, faremos um laço, ou um loop. O laço que queremos fazer é:

enquanto ainda há tentativas:

~~~~python
chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)
acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto
if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
~~~~




- Exemplo de código em Python onde os blocos de if são repetidos algumas vezes, mas não é algo prático:

~~~~python
# Neste código, para ter um efeito parecido com o laço do while, precisamos repetir o bloco de código várias vezes.
# Isto não é algo prático!

# 1º tentativa
numero_secreto = 42
chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto
if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
print("Fim do jogo")

# 2º tentativa
numero_secreto = 42
chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto
if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
print("Fim do jogo")
~~~~



- RESULTADO REPETINDO O CÓDIGO ALGUMAS VEZES:

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/01-forma-errada-repetindo-blocos-para-ter-repeticao.py
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Fim do jogo
Digite o seu número: 55
Você digitou:  55
Você errou! O seu chute foi maior que o número secreto.
Fim do jogo
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$
~~~~



git status
git add .
git commit -m "Modulo 4 - aula 01 - Laço com while. pt2"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status 


Só que o Python não entende português, então vamos traduzi-lo. A palavra tentativas será uma variável, chamaremos-a de total_de_tentativas:

~~~~python
total_de_tentativas = 3

enquanto ainda há total_de_tentativas:
    executa o código
~~~~




Resta agora a expressão ainda há. A ideia é que o usuário tenha 3 tentativas, representada no código pela variável total_de_tentativas. A cada rodada subtraímos 1 do valor dessa variável, até o valor chegar a 0, que é quando devemos sair do while, logo vamos executá-lo enquanto a variável total_de_tentativas for maior que 0*:

~~~~python
total_de_tentativas = 3

while (total_de_tentativas > 0):
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
~~~~



- O código acima funciona, porém não termina o laço, fica se repetindo:

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/01-laco-while-correto.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Digite o seu número: 34
Você digitou:  34
Você errou! O seu chute foi menor que o número secreto.
Digite o seu número: 56
Você digitou:  56
Você errou! O seu chute foi maior que o número secreto.
Digite o seu número: 57
Você digitou:  57
Você errou! O seu chute foi maior que o número secreto.
Digite o seu número: 58
Você digitou:  58
Você errou! O seu chute foi maior que o número secreto.
Digite o seu número:
~~~~




- A condição está perfeita, falta, dentro do laço, subtrairmos 1 da variável total_de_tentativas:

~~~~python
total_de_tentativas = 3

while (total_de_tentativas > 0):
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    total_de_tentativas = total_de_tentativas - 1

print("Fim do jogo")
~~~~





- Adicionando um print que traz o valor em que está a tentativa atual, para ter uma noção do valor:
    print("Tentativa:", total_de_tentativas)

- Testando:

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/01-laco-while-correto.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa: 3
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Tentativa: 2
Digite o seu número: 44
Você digitou:  44
Você errou! O seu chute foi maior que o número secreto.
Tentativa: 1
Digite o seu número: 57
Você digitou:  57
Você errou! O seu chute foi maior que o número secreto.
Fim do jogo
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$
~~~~



- Testamos o código e ótimo, ele funciona! Mas pode ficar ainda melhor.

# Representando a rodada
Vamos imprimir para o usuário qual o número da rodada que ele está jogando, para deixar claro quantas tentativas ele tem. Para isso vamos criar a variável rodada, que começa com o valor 1:

~~~~python
total_de_tentativas = 3
rodada = 1
~~~~


E vamos imprimi-la antes do usuário digitar o seu chute:

~~~~python
total_de_tentativas = 3
rodada = 1

while (total_de_tentativas > 0):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_str = input("Digite o seu número: ")

    # restante do código comentado
~~~~




- E para a variável total_de_tentativas continuar com o valor 3, não vamos mais subtrair 1 do seu valor, e sim adicionar 1 ao valor da variável rodada:

~~~~python
total_de_tentativas = 3
rodada = 1

while (total_de_tentativas > 0):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")
~~~~


- Testando:
python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/01-laco-while-correto_v2.py

- Resultado:

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/01-laco-while-correto_v2.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite o seu número: 14
Você digitou:  14
Você errou! O seu chute foi menor que o número secreto.
Tentativa 2 de 3
Digite o seu número: 87
Você digitou:  87
Você errou! O seu chute foi maior que o número secreto.
Tentativa 3 de 3
Digite o seu número: 99
Você digitou:  99
Você errou! O seu chute foi maior que o número secreto.
Tentativa 4 de 3
Digite o seu número: 999
Você digitou:  999
Você errou! O seu chute foi maior que o número secreto.
Tentativa 5 de 3
Digite o seu número: 876
Você digitou:  876
Você errou! O seu chute foi maior que o número secreto.
Tentativa 6 de 3
Digite o seu número:
~~~~


- Temos 1 problema no código:
o número de rodadas é incrementado corretamente, porém o laço não entende que as tentativas esgotaram.
é necessário um ajuste para que as rodadas ocorram conforme o número total de tentativas disponíveis.


- Por fim, precisamos modificar a condição, como o total_de_tentativas permanecerá com o valor 3, o código precisa ficar executando enquanto o valor da rodada for menor ou igual ao total de tentativas:

~~~~python
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_str = input("Digite o seu número: ")

    # restante do código comentado
~~~~

- Testando:
python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/01-laco-while-correto_v3.py

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/01-laco-while-correto_v3.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Tentativa 2 de 3
Digite o seu número: 87
Você digitou:  87
Você errou! O seu chute foi maior que o número secreto.
Tentativa 3 de 3
Digite o seu número: 999
Você digitou:  999
Você errou! O seu chute foi maior que o número secreto.
Fim do jogo
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$
~~~~


Agora conseguimos imprimir para o usuário quantas tentativas restantes ele possui!
Agora conseguimos imprimir para o usuário quantas tentativas restantes ele possui!
Agora conseguimos imprimir para o usuário quantas tentativas restantes ele possui!




git status
git add .
git commit -m "Modulo 4 - aula 01 - Laço com while. pt3 . Códigos corrigidos e versão final"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status