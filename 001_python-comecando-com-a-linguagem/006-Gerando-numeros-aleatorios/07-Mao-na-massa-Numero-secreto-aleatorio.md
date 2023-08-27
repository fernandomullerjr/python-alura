

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 6 - aula 07 Mão na massa: Número secreto aleatório."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  07 Mão na massa: Número secreto aleatório


Neste capítulo, vamos fazer com que o nosso número secreto seja gerado de modo aleatório, ao invés de ser o número 42 fixo, que era até agora.

Importando a biblioteca random
Como vimos, se queremos ter acesso às funções de geração de números aleatórios, precisamos utilizar as funções da biblioteca random do Python. Então nosso primeiro passo é importá-la logo no começo do nosso arquivo:

~~~~python
import random

print("********************")
...
## Resto do código
~~~~

Gerando um número aleatório
Agora que temos acesso às funções de número aleatório, podemos pedir um número que atenda ao nosso pré-requisito, que é ser um número que está no intervalo de 1 até 100. Para isso, já conhecemos diversos modos, como por exemplo utilizar a função random.random() e depois multiplicar o valor por 100.

Mas nós também vimos a função random.randrange(), que é uma função que facilita a nossa vida, pois ela aceita como primeiro parâmetro o menor número que queremos gerar, no nosso caso o número 1** e como segundo parâmetro até qual número queremos que o nosso intervalo de números gerados alcance, sem incluí-lo. Como queremos que o maior número seja o **100, vamos substituir a atribuição da nossa variável numero_secreto pela chamada da função, deste modo:

~~~~python
numero_secreto = random.randrange(1,101)
~~~~


## Testando a aleatoriedade
Podemos colocar um pequeno print abaixo, apenas para testar se o nosso número está sendo calculado mesmo:

~~~~python
numero_secreto = random.randrange(1,101)
print(numero_secreto)
~~~~

Faça alguns testes e verifique se está tudo correto! Não esqueça depois de remover o print de teste, se não nosso usuário irá conseguir descobrir o número muito facilmente!








