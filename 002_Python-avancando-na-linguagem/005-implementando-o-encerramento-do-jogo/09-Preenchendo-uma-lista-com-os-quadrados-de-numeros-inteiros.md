
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 08 Loop relativo à List Comprehension"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#   09 Preenchendo uma lista com os quadrados de números inteiros

Suponha que tenhamos uma lista com os seguintes inteiros:

~~~~python
inteiros = [1,3,4,5,7,8]
~~~~

Podemos preencher uma nova lista com o quadrado de cada número da lista anterior, através do recurso List Comprehension. Considerando que, para calcular o quadrado de um número, fazemos x*x, qual seria o código para obter a lista de quadrados?
Selecione uma alternativa

~~~~python
    quadrados = [2 for n in inteiros]
~~~~

    Não é possível inicializar uma lista de números inteiros, apenas caracteres.

~~~~python
    quadrados = [n*n for n in inteiros]
~~~~






# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

~~~~python
quadrados = [n*n for n in inteiros]
~~~~

Correto!
