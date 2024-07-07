
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 6 - 06 Lendo a primeira linha."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  06 Lendo a primeira linha

Dado o arquivo abaixo chamado de pessoas.txt, onde estão separados os nomes e a idade de um grupo de pessoas:

Romário 37
Junior 32
Daniel 28
Izzy 38

Se quisermos ler apenas a primeira linha do arquivo, quais comandos abaixo realizam este feito?
Selecione uma alternativa

~~~~PYTHON
    arquivo = open('pessoas.txt', 'r')
    linha = arquivo.read()
    print(linha)
~~~~

~~~~PYTHON
    arquivo = open('pessoas.txt', 'r')
    linha = arquivo.firstline()
    print(linha)
~~~~

~~~~PYTHON
    arquivo = open('pessoas.txt', 'r')
    linha = arquivo.readline()
    print(linha)
~~~~




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

~~~~PYTHON
arquivo = open('pessoas.txt', 'r')
linha = arquivo.readline()
print(linha)
~~~~


    Correto! A função readline lê apenas uma linha do arquivo.

Se desejamos ler linha a linha de nosso arquivo, podemos utilizar a função readline(). Ela nos retorna uma linha por vez, e faz com que a nossa leitura seja feita de modo mais controlado. Também existe a função read() que por sua vez lê o arquivo inteiro.
