
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 3 - aula 01 Estrutura de dados: List."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  01 Estrutura de dados: List

## Transcrição

Atualmente, já dizemos ao usuário em que posição a letra que ele chutou está na palavra secreta, caso a letra exista na palavra. Mas em um jogo real de forca, o jogador vê quantas letras há na palavra secreta. Algo como:

Qual letra? _ _ _ _ _ _

E se ele encontrar alguma letra, a mesma tem a sua lacuna preenchida. Ao digitar a letra "a", ficaria:

_ a _ a _ a

Muito mais intuitivo, não? Vamos implementar essa funcionalidade.
Conhecendo uma nova estrutura de dados: lista

Para exibir as letras dessa forma, precisamos guardar os chutes certos do usuário, mas como fazer isso?

Para tal, o Python nos oferece uma estrutura de dados que nos permite guardar valores. Essa estrutura é a lista. Para criar uma lista, utilizamos colchetes ([]):

>>> valores = []
>>> type(valores)
<class 'list'>

Assim como a string, list também é uma sequência de dados. Então podemos ver a sua documentação. Nela, podemos ver o que podemos fazer com uma lista, podemos verificar o seu valor mínimo com o min e o seu valor máximo com o max. Mas a nossa lista ainda tá vazia, certo? Podemos, já no momento de sua inicialização, passar valores para guardar nessa lista:

>>> valores = [0,1,2,3,4]

Agora podemos verificar seu menor e seu maior valor:

>>> valores = [0,1,2,3,4]
>>> min(valores)
0
>>> max(valores)
4

Para acessar um valor específico, podemos acessá-lo através do seu índice. O primeiro elemento da lista possui o índice 0, o segundo possui o índice 1 e assim por diante:

>>> valores = [0,1,2,3,4]
>>> valores[2]
2

Podemos também saber o tamanho da lista com o len e verificar se determinado valor está guardado nela:

>>> valores = [0,1,2,3,4]
>>> 0 in valores
True
>>> 8 in valores
False

Além disso, existem funções específicas da lista, que podem ser vistas aqui. Podemos adicionar elementos ao final da lista com o append, exibir e remover um elemento de determinada posição com o pop, entre diversas outras funcionalidades.

Agora que sabemos como guardar valores em uma lista, podemos voltar ao nosso jogo e guardar os acertos do usuário. Faremos isso no próximo vídeo :)





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 

>>> valores = []
>>>
>>> type(valores)
<class 'list'>
>>>

Sequence Types — list, tuple, range
<https://docs.python.org/3.7/library/stdtypes.html#sequence-types-list-tuple-range>



>>> valores = [0,1,2,3,"x"]
>>>
>>> 6 in valores
False
>>>
>>> 3 in valores
True
>>>
>>>

>>>
>>> "a" in "banana"
True
>>>

>>> valores[0]
0
>>>
>>>
>>>
>>> valores[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>

>>>
>>> valores[4]
'x'
>>>


- Deu erro, porque os números estão com uma string misturada:

>>> min(valores)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>>


- Resetando a lista, colocando apenas inteiros:

>>> valores = [0,1,2,3]
>>>

>>>
>>> min(valores)
0
>>>
>>>
>>> max(valores)
3
>>>
>>> len(valores)
4
>>>

>>> valores.append(7)
>>>
>>> valores
[0, 1, 2, 3, 7]
>>>




A função len() sempre retorna um valor inteiro que representa o número de elementos no objeto.

Outras funções úteis para trabalhar com listas:

    list.append(): Adiciona um novo item ao final da lista.
    list.insert(): Insere um novo item em uma posição específica da lista.
    list.remove(): Remove um item da lista pelo valor.
    list.pop(): Remove um item da lista pela posição.
    list.sort(): Ordena os elementos da lista.
    list.reverse(): Inverte a ordem dos elementos da lista.




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESUMO

- Arrays e Listas são parecidos, mas não são iguais.


