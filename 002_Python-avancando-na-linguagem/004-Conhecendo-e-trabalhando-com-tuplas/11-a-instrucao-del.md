
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "5.2. A instrução del"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 5.2. A instrução del

Existe uma maneira de remover um item de uma lista usando seu índice no lugar do seu valor: a instrução del. Ele difere do método pop() que devolve um valor. A instrução del pode também ser utilizada para remover fatias de uma lista ou limpar a lista inteira (que fizemos antes atribuindo uma lista vazia à fatia a[:]). Por exemplo:
>>>

>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]

del também pode ser usado para remover totalmente uma variável:
>>>

>>> del a

Referenciar a variável a depois de sua remoção constitui erro (pelo menos até que seja feita uma nova atribuição para ela). Encontraremos outros usos para a instrução del mais tarde.