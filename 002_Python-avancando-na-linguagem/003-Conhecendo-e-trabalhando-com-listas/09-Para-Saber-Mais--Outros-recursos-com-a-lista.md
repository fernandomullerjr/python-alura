
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 3 - aula 09 Para Saber Mais: Outros recursos com a lista."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 09 Para Saber Mais: Outros recursos com a lista

Além das funções min(), max() e len() que vimos neste capítulo, as listas do Python tem outros recursos que facilitam nossa vida. Vamos conhecer alguns deles:

## A função .count()

Um jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista é a função .count() das listas, veja:

~~~~python
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))
~~~~

O código acima nos retorna 3, pois em nossa lista encontramos 3 vezes o número zero nela.

Utilizando a função .count() podemos por exemplo, detectar quantas letras ainda faltam para o nosso usuário preencher:

~~~~python
letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
~~~~


## A função .index()

Uma outra função que pode ser bastante útil é a função .index(), que nos retorna o índice da primeira ocorrência de um determinado elemento em uma lista, veja:

~~~~python
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))
~~~~

O código acima nos retorna 3, pois é o índice da primeira ocorrência do elemento 'Uva' na lista frutas (lembre-se nas listas começamos a contar do índice 0).

Só tome cuidado quando utilizar a função .index(), pois a mesma pode retornar um erro caso você tente buscar pelo índice de um elemento que não existe. Veja o caso abaixo:

~~~~python
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Melancia'))
~~~~

Ao tentar buscar pela fruta 'Melancia', obteremos o erro "ValueError: 'Melancia' is not in list" no console, já que é impossível buscar o índice de algo que não está na lista. Por isto, é sempre uma boa prática verificar se o elemento está na lista com o operador in antes de obter o seu índice. Um código ideal que faz uso da função index() é demonstrado abaixo:

~~~~python
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))
~~~~

Assim temos certeza que a fruta_buscada está dentro da lista antes de perguntarmos o seu índice, evitando assim de receber um erro no console.


## Opinião do instrutor

Estes são só mais dois recursos desta incrível linguagem Python. Não deixe de explorar a documentação para aprender ainda mais sobre as funções das Listas. E claro, vamos falar ainda mais sobre listas e sequências em geral nesse curso!










- Testando

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/003-Conhecendo-e-trabalhando-com-listas/09-funcao-count.py
3
fernando@debian10x64:~$



fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/003-Conhecendo-e-trabalhando-com-listas/09-forca-com-letras-faltando.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
['_', '_', '_', '_', '_', '_']
Qual letra? B
['b', '_', '_', '_', '_', '_']
Ainda faltam acertar 5 letras
Qual letra? g
['b', '_', '_', '_', '_', '_']
Ainda faltam acertar 5 letras
Qual letra? a
['b', 'a', '_', 'a', '_', 'a']
Ainda faltam acertar 2 letras
Qual letra? x
['b', 'a', '_', 'a', '_', 'a']
Ainda faltam acertar 2 letras
Qual letra? w
['b', 'a', '_', 'a', '_', 'a']
Ainda faltam acertar 2 letras
Qual letra? y
['b', 'a', '_', 'a', '_', 'a']
Ainda faltam acertar 2 letras
Qual letra? n
['b', 'a', 'n', 'a', 'n', 'a']
Ainda faltam acertar 0 letras
Qual letra?




fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/003-Conhecendo-e-trabalhando-com-listas/09-fruta-buscada-inexistente.py
Desculpe, a Melancia não está na lista frutas
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/003-Conhecendo-e-trabalhando-com-listas/09-fruta-buscada-existe.py
3
fernando@debian10x64:~$

~~~~