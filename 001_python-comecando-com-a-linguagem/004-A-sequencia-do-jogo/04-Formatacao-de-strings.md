
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 04 - Formatação de strings."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04 - Formatação de strings

# Transcrição

Com a lógica de tentativas implementada, vamos focar na impressão do número de tentativas para o usuário. Atualmente ela está assim:

~~~~python
print("Tentativa", rodada, "de", total_de_tentativas)
~~~~

Desse jeito a frase é impressa do jeito que queremos, mas tem uma forma mais elegante de imprimir essa frase. Podemos deixar a string toda no código, dizendo onde que ela eventualmente pode mudar, no nosso caso é nos números. Onde a string pode mudar, colocamos chaves ({}):

~~~~python
print("Tentativa {} de {}")
~~~~


As chaves significam que o Python deve substituí-las pelos valores das variáveis, então vamos passá-las:

~~~~python
print("Tentativa {} de {}", rodada, total_de_tentativas)
~~~~


Se executarmos o programa, a seguinte frase é impressa:

Tentativa {} de {} 1 3



Não é exatamente isso que queremos, as primeiras chaves devem receber o valor da rodada, e as segundas o total de tentativas. Para isso funcionar, devemos chamar uma função baseada nessa string, a função format, passando para ela as variáveis que devem ficar no lugar das chaves:

~~~~python
print("Tentativa {} de {}".format(rodada, total_de_tentativas))
~~~~

Podemos testar e ver que agora está tudo funcionando como antes! O que acabamos de fazer se chama interpolação de strings(String Interpolation), muito comum nas linguagens e que nos oferece recursos da string para fazermos essas substituições.

Assim o nosso código fica um pouco mais elegante, já que nele vemos a string inteira, sabendo exatamente onde ela será alterada.



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Código ajustado

- Arquivo
/home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/04-while-string-interpolation.py

~~~~python
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
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


- Validando:

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/04-while-string-interpolation.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Tentativa 1 de 3
Digite o seu número: 3
Você digitou:  3
Você errou! O seu chute foi menor que o número secreto.
Tentativa 2 de 3
Digite o seu número: 99
Você digitou:  99
Você errou! O seu chute foi maior que o número secreto.
Tentativa 3 de 3
Digite o seu número: 88
Você digitou:  88
Você errou! O seu chute foi maior que o número secreto.
Fim do jogo
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$
~~~~




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Exemplos adicionais


- Fonte:
<https://www.geeksforgeeks.org/python-string-interpolation/>

~~~~python
n1 = 'Hello'
n2 = 'GeeksforGeeks'

# for single substitution
print('{}, {}'.format(n1, n2))
~~~~


- Exemplo:

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/04-exemplo-string-interpolation-1.py
Hello, GeeksforGeeks
fernando@debian10x64:~/cursos/python/python-alura/python-comecando-com-a-linguagem$ ^C
~~~~





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Material adicional

<https://docs.python.org/pt-br/3/tutorial/inputoutput.html>
<https://acervolima.com/funcao-format-em-python/>
<https://www.programiz.com/python-programming/string-interpolation>




git status
git add .
git commit -m "Modulo 4 - aula 04 - Formatação de strings. Conclusão da aula"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status