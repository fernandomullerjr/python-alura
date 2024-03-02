
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 3 - aula 07 Para saber mais: Variável index."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 07 Para saber mais: Variável index

Em programação é muito comum acessar e manipular elementos individuais de uma coleção de dados, como um array ou uma string. Para facilitar essa tarefa, o uso de uma variável de índice é bastante útil. Vamos entender melhor a utilização de uma variável de índice e como ela pode ser útil no controle da posição de elementos em arrays e strings em Python.
O que é uma Variável de índice?

Uma variável de índice é uma variável que armazena a posição de um elemento em uma coleção de dados, como um array ou uma string. O índice é geralmente um número inteiro que representa a posição do elemento dentro da coleção. Ao utilizar uma variável de índice, é possível acessar, atualizar ou manipular elementos específicos de forma individual.
Uso de Variável de índice em Arrays

Em Python, um array é uma estrutura de dados que armazena uma coleção de elementos do mesmo tipo. Para acessar elementos em um array, a variável de índice é utilizada para indicar a posição do elemento desejado.

Vejamos um exemplo simples:

~~~~python
numeros = [10, 20, 30, 40, 50]

for i in range(len(numeros)):
    print("O elemento na posição", i, "é", numeros[i])
~~~~

No exemplo anterior, a variável i é a variável de índice utilizada para percorrer o array numeros. No loop for, a função range(len(numeros)) retorna uma sequência de números que representa os índices válidos para o array numeros. A cada iteração do loop, o valor atual da variável i é usado para acessar o elemento correspondente no array através da expressão numeros[i].

A função len é utilizada para obter o comprimento do array, ou seja, o número total de elementos presentes nele. Essa função retorna um valor inteiro representando o tamanho do array e no exemplo de código anterior essa informação foi utilizada como argumento para a função range, que retorna uma sequência de números que representa os índices válidos para o array.
Uso de Variável de índice em Strings

Uma string nada mais é do que uma sequência de caracteres. Assim como nos arrays, a variável de índice pode ser usada para acessar caracteres individuais dentro de uma string.

Considere o seguinte exemplo de código:

~~~~python
frase = "Olá, mundo!"

for i in range(len(frase)):
    print("O caractere na posição", i, "é", frase[i])
~~~~

No exemplo anterior, a variável i atua como a variável de índice e percorre os índices válidos para a string frase. A cada iteração do loop, o valor atual de i é utilizado para acessar o caractere correspondente na variável frase, com a utilização da expressão frase[i].

Perceba como o uso de uma variável de índice em arrays e strings é algo simples e fundamental para acessar e manipular elementos individuais. Por meio de uma variável de índice, é possível controlar a posição dos elementos e realizar operações específicas em cada um deles.








- Testando

~~~~
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/003-Conhecendo-e-trabalhando-com-listas/07-variavel-index-array.py
O elemento na posição 0 é 10
O elemento na posição 1 é 20
O elemento na posição 2 é 30
O elemento na posição 3 é 40
O elemento na posição 4 é 50
fernando@debian10x64:~$
fernando@debian10x64:~$ date
Sat 02 Mar 2024 07:53:08 PM -03
fernando@debian10x64:~$


fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/003-Conhecendo-e-trabalhando-com-listas/07-variavel-index-string.py
O caractere na posição 0 é O
O caractere na posição 1 é l
O caractere na posição 2 é á
O caractere na posição 3 é ,
O caractere na posição 4 é
O caractere na posição 5 é m
O caractere na posição 6 é u
O caractere na posição 7 é n
O caractere na posição 8 é d
O caractere na posição 9 é o
O caractere na posição 10 é !
fernando@debian10x64:~$
fernando@debian10x64:~$

~~~~