



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 6 - aula 04 O menor e o maior."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04 O menor e o maior

Qual é o menor e o maior número possível que o script abaixo consegue imprimir ?

~~~~python
import random

aleatorio = random.randrange(10)
print(aleatorio)
~~~~


- RESPOSTA CORRETA:
Menor: 0 e Maior: 9




## Explicação detalhada

A função random.randrange() quando só possuí um parâmetro supõe que você quer dizer de zero até número passado -1, ou seja, neste caso, o menor número possível quando fazemos:

random.randrange(10)

É o zero e o maior número possível é o 9.