

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 6 - aula 03 Definindo um intervalo para a geração de números aleatórios."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Definindo um intervalo para a geração de números aleatórios

Transcrição
Para gerar um número aleatório no nosso jogo, a primeira coisa que devemos fazer é importar o seu módulo, no início do programa:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

# restante do código comentado
~~~~

Com o módulo importado, vamos remover o valor fixo da variável numero_secreto e substituir por um valor aleatório que será gerado pela função random():

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.random()
total_de_tentativas = 3

# restante do código comentado
~~~~


Mas não podemos nos esquecer de multiplicar esse número por 100 e arredondá-lo:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.random() * 100)
total_de_tentativas = 3

# restante do código comentado
~~~~


Perfeito, conseguimos aplicar a mudança ao nosso código. Agora fica mais difícil de acertar o número secreto, até para nós, os desenvolvedores do jogo :)

Gerando um número aleatório dentro de um intervalo
A ideia de multiplicar o número por 100 parece funcionar, mas podemos lembrar que o número gerado é entre 0.0 e 1.0, que quando multiplicado por 100 fica entre 0 e 100. Só que o nosso jogo não aceita o 0!

O ideal seria que pudéssemos definir um intervalo, dizer que queremos que o número gerado esteja entre 1 e 100. Como o random é um módulo, ele possui mais de uma função e a função randrange() serve exatamente para esse nosso problema. Se passarmos um parâmetro para ela, ela irá gerar um número inteiro de 0 até o valor desse parâmetro menos 1. Se passarmos dois parâmetros para ela, ela irá gerar um número inteiro do valor do primeiro parâmetro até o valor do segundo parâmetro menos 1, exatamente o que queremos!

Vamos, passando o intervalo que queremos para a função randrange(), lembrando que como queremos que o número gerado esteja entre 1 e 100 (inclusive), precisamos passar o número 101 como segundo parâmetro para a função:

~~~~python
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

# restante do código comentado
~~~~

Ótimo, problema resolvido!

No próximo capítulo vamos focar na dificuldade do jogo. Um jogo mais fácil terá um número de tentativas maior, e um mais difícil terá um número de tentativas menor. Até lá!




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Definindo um intervalo para a geração de números aleatórios


## Examples

Basic examples:
>>>

random()                             # Random float:  0.0 <= x < 1.0
0.37444887175646646

uniform(2.5, 10.0)                   # Random float:  2.5 <= x <= 10.0
3.1800146073117523

expovariate(1 / 5)                   # Interval between arrivals averaging 5 seconds
5.148957571865031

randrange(10)                        # Integer from 0 to 9 inclusive
7

randrange(0, 101, 2)                 # Even integer from 0 to 100 inclusive
26

choice(['win', 'lose', 'draw'])      # Single random element from a sequence
'draw'

deck = 'ace two three four'.split()

shuffle(deck)                        # Shuffle a list

deck
['four', 'two', 'ace', 'three']

sample([10, 20, 30, 40, 50], k=4)    # Four samples without replacement
[40, 10, 50, 30]

Simulations:
>>>

# Six roulette wheel spins (weighted sampling with replacement)

choices(['red', 'black', 'green'], [18, 18, 2], k=6)
['red', 'green', 'black', 'black', 'red', 'black']

# Deal 20 cards without replacement from a deck

# of 52 playing cards, and determine the proportion of cards

# with a ten-value:  ten, jack, queen, or king.

dealt = sample(['tens', 'low cards'], counts=[16, 36], k=20)

dealt.count('tens') / 20
0.15

# Estimate the probability of getting 5 or more heads from 7 spins

# of a biased coin that settles on heads 60% of the time.

def trial():

    return choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5


sum(trial() for i in range(10_000)) / 10_000
0.4169

# Probability of the median of 5 samples being in middle two quartiles

def trial():

    return 2_500 <= sorted(choices(range(10_000), k=5))[2] < 7_500


sum(trial() for i in range(10_000)) / 10_000
0.7958








randrange(0, 101, 2) # Número inteiro par de 0 a 100 inclusive
26




Continua em
5:32