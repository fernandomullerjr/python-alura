

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


