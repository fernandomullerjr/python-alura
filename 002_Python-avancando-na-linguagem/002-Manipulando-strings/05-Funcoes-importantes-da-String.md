
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 2 - aula 05 Funções importantes da String"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 Funções importantes da String

## Transcrição
Ao procurar por uma letra maiúscula, a mesma não é encontrada na palavra, por exemplo:

~~~~bash
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? N
Jogando...
~~~~

Não queremos que essa distinção entre letras minúsculas e maiúsculas seja feita.

## Alterando a caixa da string

Já vimos algumas funções que a string possui, como a format e find, mas há diversas outras, como podemos ver na documentação do Python 3. Por exemplo, existe a função capitalize, que retorna a string com a primeira letra em maiúsculo e o restante em minúsculo.

Existe também a função lower, que retorna a string com todas as letras em minúsculo:

>>> palavra = "BANANA"
>>> palavra.lower()
'banana'

Antagonicamente, existe a função upper, que retorna a string com todas as letras em maiúsculo:

>>> palavra = "banana"
>>> palavra.upper()
'BANANA'

Então, ao compararmos o chute do usuário com a letra da palavra secreta, podemos comparar as duas strings em letras maiúsculas, assim não haverá distinção na hora da comparação:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1

    print("Jogando...")
~~~~

Problema resolvido! Mas o que acontece se, ao digitar o chute, o usuário digitar espaços em branco no início ou no fim da letra?


## Removendo espaços em branco no início e no fim de uma string

Ao digitar a letra com espaços em branco no seu início, vejamos o que acontece:

~~~~bash
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra?         n
Jogando...
~~~~

A letra não é reconhecida! Então precisamos remover todos os espaços no início e no fim do chute do usuário. E para isso existe a função strip, que faz exatamente isso:

>>> palavra = "  banana   "
>>> palavra.strip()
'banana'

Logo, após capturar o chute do usuário, vamos chamar essa função, atribuindo o seu retorno à variável chute:

~~~~python
while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1

    print("Jogando...")
~~~~

Podemos executar o programa novamente, e digitar uma letra com alguns espaços em branco no seu início:

~~~~bash
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra?         N
Encontrei a letra n na posição 2
Encontrei a letra n na posição 4
Jogando...
~~~~

Agora a letra é encontrada na palavra, mesmo com os espaços a mais!







# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 Funções importantes da String

Não queremos que essa distinção entre letras minúsculas e maiúsculas seja feita.



- Documentação sobre "Text Sequence Type":

<https://docs.python.org/3.8/library/stdtypes.html#text-sequence-type-str>



- Testando

 str.capitalize()

    Return a copy of the string with its first character capitalized and the rest lowercased.



palavra.capitalize()


>>> palavra = "banana"
>>>
>>> palavra.capitalize()
'Banana'
>>>






str.endswith(suffix[, start[, end]])

    Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.


palavra.endswith("na")

>>> palavra.endswith("na")
True
>>>







str.lower()

    Return a copy of the string with all the cased characters 4 converted to lowercase.

    The lowercasing algorithm used is described in section 3.13 of the Unicode Standard.

palavra2 = palavra.capitalize()
palavra2
palavra2.lower()

>>> palavra2 = palavra.capitalize()
>>>
>>> palavra2
'Banana'
>>>
>>>
>>> palavra2.lower()
'banana'
>>>







## PENDENTE
- CONTINUA EM 06:25
- Doc:
<https://docs.python.org/3.8/library/stdtypes.html#text-sequence-type-str>





- Função lower

>>> "ABC".lower()
'abc'
>>>




## UPPER

 str.upper()

    Return a copy of the string with all the cased characters 4 converted to uppercase. Note that s.upper().isupper() might be False if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. “Lt” (Letter, titlecase).

>>> palavra2
'Banana'
>>>
>>>
>>> palavra2.lower()
'banana'
>>>
>>>
>>>
>>> palavra2.upper()
'BANANA'
>>>










str.strip([chars])

    Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:
    >>>

    >>> '   spacious   '.strip()
    'spacious'
    >>> 'www.example.com'.strip('cmowz.')
    'example'

    The outermost leading and trailing chars argument values are stripped from the string. Characters are removed from the leading end until reaching a string character that is not contained in the set of characters in chars. A similar action takes place on the trailing end. For example:
    >>>

    >>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
    >>> comment_string.strip('.#! ')
    'Section 3.2.1 Issue #32'

>>> palavra = "   abcd   "
>>>
>>>
>>> palavra.strip()
'abcd'
>>>










- Testando

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/05-forca.py
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra?    u
Jogando...
Qual letra?    N
Encontrei a letra n na posição 2
Encontrei a letra n na posição 4
Jogando...
Qual letra?    a
Encontrei a letra a na posição 1
Encontrei a letra a na posição 3
Encontrei a letra a na posição 5
Jogando...
Qual letra? B
Encontrei a letra b na posição 0
Jogando...
Qual letra?      n
Encontrei a letra n na posição 2
Encontrei a letra n na posição 4
Jogando...
Qual letra? ^CTraceback (most recent call last):
  File "/home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/05-forca.py", line 27, in <module>
    jogar()
  File "/home/fernando/cursos/python/python-alura/002_Python-avancando-na-linguagem/002-Manipulando-strings/05-forca.py", line 13, in jogar
    chute = input("Qual letra? ")
KeyboardInterrupt

fernando@debian10x64:~$
~~~~










- Código do jogo com o if usando upper:

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

~~~~


Nesse código, o método upper() está sendo utilizado para converter tanto a letra da palavra secreta quanto a letra fornecida pelo usuário para maiúsculas antes de compará-las. Isso é feito para garantir que o jogo seja insensível a maiúsculas e minúsculas, ou seja, não importa se o usuário digita uma letra em maiúscula, minúscula ou uma combinação de ambas, o programa considerará como correta.

A linha em questão é esta:

python

if (chute.upper() == letra.upper()):

A função upper() converte uma string para maiúsculas. Portanto, ao comparar chute.upper() com letra.upper(), você está garantindo que a comparação seja feita de forma case-insensitive.

Então, mesmo que a palavra secreta seja "banana" e o usuário insira "B" ou "b", o programa ainda detectará a letra correta e informará ao usuário que a letra foi encontrada na posição correta.