

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 02 - Resultado do programa."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 02 - Resultado do programa

- Temos o seguinte código:

~~~~python
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2
~~~~

Apenas olhando este código, sem executá-lo, qual será a saída no console?

Alternativa incorreta
1
3
5
7
9

Errado! Número 5 não será impresso por causa do if.



1
2
3
4
6
7
8
9



1
3
7
9
11



1
3
7
9
Correto!


Se você achou que o 5 seria impresso, errou. Isto porque no if(contador == 5), adicionamos novamente 2 ao contador.