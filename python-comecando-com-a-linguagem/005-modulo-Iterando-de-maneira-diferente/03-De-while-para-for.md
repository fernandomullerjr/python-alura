

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 5 - aula 03 - De while para for."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 - De while para for #2
De while para for #2

Temos o seguinte código:

~~~~python
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3
~~~~

Que imprime:

1
4
7
10



# Pergunta

- Como você poderia substituir o código acima usando o laço for .. range?


Alternativa correta

~~~~python
for contador in range(1,11,3):
    print(contador)
~~~~

Correto! Utilizando o range com um step 3.


# Explicação

A função range possui os seguintes parâmetros:
range(start, stop, [step])

Onde o step é opcional. Como queremos "pular" de 3 em 3, começando com 1 (start) até 10 (stop), podemos escrever:

~~~~python
for contador in range(1,11,3):
    print(contador)
~~~~




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Range examples:
>>>
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]

