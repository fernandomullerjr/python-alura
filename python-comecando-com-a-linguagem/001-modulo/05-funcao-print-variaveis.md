

# Aula 05 - Função print e variáveis

- Existem 2 versões do Python instaladas na máquina:

~~~~bash
fernando@debian10x64:~/cursos$ python -V
Python 2.7.16
fernando@debian10x64:~/cursos$ python3 -V
Python 3.7.3
fernando@debian10x64:~/cursos$
~~~~

- Entrando no prompt do Python:
python3

- Escrevendo a palavra help e abrindo e fechando parenteses, é possível chamar a função de ajuda do Python:
>>> help()

- Isto vai fazer com que mude o prompt:
help> 
help> print


- Ao digitar o nome da função "print", dentro do prompt do help, ele traz informações sobre a função print:

        Help on built-in function print in module builtins:

        print(...)
            print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

            Prints the values to a stream, or to sys.stdout by default.
            Optional keyword arguments:
            file:  a file-like object (stream); defaults to the current sys.stdout.
            sep:   string inserted between values, default a space.
            end:   string appended after the last value, default a newline.
            flush: whether to forcibly flush the stream.
        (END)

- Os 3 pontinhos ... indicam que podem ser passados vários valores de uma vez só.


- O print também é uma função do Python.


- Testando o print com o sep
>>> print("Brasil ganhou 5 titulos mundiais", sep=" ")
Brasil ganhou 5 titulos mundiais
>>>


- Testando de outra maneira, separando os valores por aspas.
- Colocando um hifen como o valor a ser inserido entre os valores do print.
print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")

>>> print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")
Brasil-ganhou-5-titulos mundiais
>>>




- Removendo o hifen como o valor a ser inserido entre os valores do print, não definindo um separador.
print("Brasil", "ganhou", 5, "titulos mundiais", sep="")

>>> print("Brasil", "ganhou", 5, "titulos mundiais", sep="")
Brasilganhou5titulos mundiais
>>>


- Usando o end
print("Brasil", "ganhou", 5, "titulos mundiais", end="\n")

>>> print("Brasil", "ganhou", 5, "titulos mundiais", end="\n")
Brasil ganhou 5 titulos mundiais
>>>



- Usando o end, sem definir a quebra de linha.
- Dessa forma ele não quebra uma linha ao final:
print("Brasil", "ganhou", 5, "titulos mundiais", end="")

>>> print("Brasil", "ganhou", 5, "titulos mundiais", end="")
Brasil ganhou 5 titulos mundiais>>>



- Fazendo que o end defina uma palavra ao final e não quebre linha:
print("Brasil", "ganhou", 5, "titulos mundiais", end="FIM_DA_LINHA")

>>> print("Brasil", "ganhou", 5, "titulos mundiais", end="FIM_DA_LINHA")
Brasil ganhou 5 titulos mundiaisFIM_DA_LINHA>>>



- Definindo uma variável:
pais = "Italia"

- Com a função type, é possível obter o tipo do valor:
type(pais)

- Neste caso o pais é uma string:
>>> type(pais)
<class 'str'>
>>>



- Definindo outra variável:
quantidade = 4

- Verificando o tipo da variavel quantidade:
type(quantidade)

- Retorna que a variável é do tipo inteiro:
>>> type(quantidade)
<class 'int'>
>>>



- Imprimindo os valores das variaveis com os textos fixos:
print(pais, "ganhou", quantidade, "titulos mundiais")

>>> print(pais, "ganhou", quantidade, "titulos mundiais")
Italia ganhou 4 titulos mundiais
>>>
