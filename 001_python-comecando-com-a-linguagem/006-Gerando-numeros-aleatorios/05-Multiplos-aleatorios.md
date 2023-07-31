





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 6 - aula 05 Múltiplos aleatórios."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 Múltiplos aleatórios

PRÓXIMA ATIVIDADE

Selecione todas as opções abaixo que são uma instrução do Python capaz de gerar um número inteiro aleatório entre 0 e 100 (incluindo 100, ou seja [0,100]):





int(random.random() * 101);

Correto! A função random.random() sempre nos retorna um número entre 0.0 e algum valor menor 1.0, multiplicando por 101 obteremos um número entre 0.0 e algum valor menor de 100.0. A função int() faz o trabalho de cortar as partes decimais deste número e obtemos o que queremos!




round(random.random() * 100);

Correto! A função random.random() sempre nos retornar um número entre 0.0 e algum valor menor de 1.0, multiplicando por 100 obteremos um número entre 0.0 e algum valor menor de 100.0. A função round() faz arredondamento deste número e obtemos o que queremos!




random.randrange(0,101)

Correto! A função random.randrange() vai retornar um número inteiro do primeiro parâmetro passado até o segundo. A diferença é que o segundo parâmetro não é inclusivo, ou seja , o número 101 nunca será sorteado, ela vai apenas até o 100.






Apesar da função random.randrange() já resolver bem os nossos problemas, é sempre bom conhecer diferentes modos de resolvê-los. Isto nos torna desenvolvedores criativos e capazes de encarar qualquer código que encontrarmos por aí!











# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Explicação adicional - int(random.random() * 101);

O código fornecido, int(random.random() * 101), pode, de fato, gerar um valor igual a 101 ou maior. Vamos esclarecer como funciona:

O código usa a função random.random() do módulo random, que retorna um número de ponto flutuante no intervalo semi-aberto [0.0, 1.0). Em seguida, ele multiplica esse valor por 101 e usa a função int() para converter o resultado em um número inteiro.

O ponto importante é que o número retornado por random.random() pode incluir o valor 1.0, mas ele não inclui o valor 0.0. Isso significa que o intervalo do produto random.random() * 101 será semi-aberto à esquerda e fechado à direita, ou seja, [0.0, 101.0).

Agora, ao converter esse valor em um inteiro usando int(), ele será truncado para o valor inteiro mais próximo. O truncamento sempre removerá a parte decimal, e o maior valor possível de random.random() * 101 que pode ser truncado para um número inteiro é 100.999... que é arredondado para 100. Portanto, o resultado final será um número inteiro entre 0 e 100.

Para gerar um valor inteiro entre 0 e 101 (inclusive), você precisa fazer algo diferente. Por exemplo, você pode usar random.randint() do módulo random, que gera um número inteiro entre os dois valores especificados, inclusive. Veja o código abaixo:

~~~~python

import random

numero = random.randint(0, 101)
print(numero)
~~~~

Esse código gerará um valor inteiro aleatório entre 0 e 101, incluindo ambos os extremos (0 e 101).





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Truncamento

Vamos explicar melhor o conceito de truncamento em Python.

O truncamento é uma operação que remove a parte decimal de um número, resultando em um número inteiro. Em Python, você pode realizar o truncamento de um número de ponto flutuante para um inteiro usando a função int().

Quando você usa a função int() para converter um número de ponto flutuante em Python, ela simplesmente corta (trunca) a parte decimal do número, mantendo apenas a parte inteira. Não há arredondamento envolvido na operação de truncamento, ou seja, o número não é arredondado para o número inteiro mais próximo; apenas a parte decimal é descartada.

Vamos considerar um exemplo para entender melhor:

~~~~python

num_float = 10.999
num_int = int(num_float)
print(num_int)
~~~~

A saída será:

10

Neste exemplo, o valor de num_float é 10.999, e ao aplicar int() a esse valor, a parte decimal é removida, e o valor resultante é 10.

Agora, voltando ao código original int(random.random() * 101), a expressão random.random() * 101 pode gerar valores de 0.0 (incluindo) até 101.0 (excluindo). No entanto, quando você usa int() para converter esse valor em um inteiro, ele simplesmente corta a parte decimal, resultando em valores inteiros entre 0 e 100 (inclusive).

Em resumo, o truncamento descarta a parte decimal de um número de ponto flutuante ao convertê-lo em um inteiro. Por causa disso, o código original não pode gerar o número 101, apenas valores entre 0 e 100 (ambos os extremos incluídos). Para incluir o número 101, você precisaria usar outras abordagens, como a função random.randint() que mencionei anteriormente.