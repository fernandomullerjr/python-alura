



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 6 - aula 01 Gerando e arredondando um número aleatório."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Gerando e arredondando um número aleatório

Transcrição
A lógica principal do nosso jogo já está funcionando, mas ainda há um detalhe, o número secreto não é tão secreto assim, pois ele está fixo! Então vamos alterar isso, para que ele passe a ser um número aleatório, coisa que veremos nesse capítulo.

Gerando um número aleatório
A ideia é que o próprio jogo, toda vez que for executado, gere esse número, ele que decide isso, não nós. E para gerar um número aleatório, o Python 3 possui a função random(), que gera um número no intervalo entre 0.0 e 1.0. Mas ao contrário das funções built-in do Python, como as funções input(), int(), print() e range(), que são funções embutidas do Python (que já vem com o mesmo), a função random não vem, pois está em um módulo separado, e esse módulo precisa ser importado.

Podemos ir ao console do Python e testar isso. Primeiro importando o módulo:

>>> import random
E a partir desse módulo, chamamos a função random():

>>> import random
>>> random.random()
0.6022965518496559
Arredondando um número
Só que, como podemos perceber, o número gerado tem muitas casas decimais e está no intervalo entre 0.0 e 1.0, mas no nosso jogo precisamos de um número entre 1 e 100. O que podemos fazer é multiplicar o número gerado por 100:

>>> import random
>>> random.random() * 100
58.30742817094118
Já conseguimos chegar a um número mais próximo do ideal, falta agora removermos as casas decimais. Podemos utilizar a já conhecida função int, que irá converter o número aleatório, que é um float, em um número inteiro:

>>> int(random.random() * 100)
91
Mas reparem no exemplo abaixo:

>>> numero_random = random.random() * 100
>>> numero_random
18.895629671768187
>>> int(numero_random)
18
A função int nada mais faz do que remover as casas decimais do número flutuante. Mas o número gerado acima está mais próximo de 19 do que de 18, correto? Será que temos uma função que arredonda esse número para nós? Sim! Temos mais uma função built-in, a round:

>>> numero_random = random.random() * 100
>>> numero_random
18.895629671768187
>>> int(numero_random)
18
>>> round(numero_random)
19
Conhecendo isso, podemos aplicar ao nosso jogo. Faremos isso no próximo vídeo, até lá!




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Gerando e arredondando um número aleatório


- Pegando o código do jogo deste arquivo Python, como base para a aula:

/home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/005-Iterando-de-maneira-diferente/04-codigo-comentado.py

~~~~python
numero_secreto = 42
total_de_tentativas = 3

# O bloco de código dentro do loop for será executado por cada rodada do jogo. 
# O loop é controlado pela variável rodada, que começa com o valor 1 e vai até o valor de total_de_tentativas + 1.
for rodada in range(1, total_de_tentativas + 1):
    # Os valores de rodada e total_de_tentativas são inseridos nos espaços reservados {} da string de formato usando o método format().
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    #   Nessa linha, estamos comparando se o valor da variável numero_secreto é igual ao valor da variável chute. 
    #  O operador == verifica a igualdade entre os dois valores. Se forem iguais, a variável acertou receberá o valor booleano True, indicando que o jogador 
    #  acertou o número secreto. Caso contrário, receberá o valor False.
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
~~~~




- Gerando novo arquivo:
/home/fernando/cursos/python/python-alura/006-Gerando-numeros-aleatorios/01-jogo.py



- Verificando a documentação do random:
<https://docs.python.org/3/library/random.html>




- Testando

>>> print("teste")
teste
>>>
>>> random()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'random' is not defined
>>>


- O random não funciona direto que nem o print e outras funções, porque ele não é uma Built-in.
- Listagem das
<https://docs.python.org/3/library/functions.html>


Built-in Functions

The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.

Built-in Functions
A
abs()
aiter()
all()
any()
anext()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
callable()
chr()
classmethod()
compile()
complex()

D
delattr()
dict()
dir()
divmod()

	
E
enumerate()
eval()
exec()

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()

I
id()
input()
int()
isinstance()
issubclass()
iter()
	
L
len()
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open()
ord()

P
pow()
print()
property()




	
R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()

T
tuple()
type()

V
vars()

Z
zip()

_
__import__()











>>>  random.random()
  File "<stdin>", line 1
    random.random()
    ^
IndentationError: unexpected indent
>>>



- Esse nome que vem a frente na documentação, antes do ponto, é conhecido como biblioteca ou módulo no Python.


- Neste caso é necessário usar o import, então ele passa a gerar os números aleatórios:

>>> import random
>>>
>>> random.random()
0.4413279822277377
>>>
>>>
>>>




random.random()

    Return the next random floating point number in the range 0.0 <= X < 1.0





>>> random.random() * 100
5.740263620076047
>>>
>>>
>>> random.random() * 100
55.39283415658392
>>>
>>> random.random() * 100
1.13590870013196
>>>
>>>
>>> random.random() * 100
18.858163667988347
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> random.random() * 100
35.357098543216296
>>>




- Continua em
6:35