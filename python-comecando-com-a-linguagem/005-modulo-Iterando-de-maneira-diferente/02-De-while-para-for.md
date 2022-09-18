
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 5 - aula 02 - De while para for."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 02 - De while para for

Temos o seguinte loop usando while:

~~~~python
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 1
~~~~


Qual das opções abaixo possui o mesmo resultado usando for .. range?

Selecione uma alternativa

- A
~~~~python
for contador in range(1, 10):
    print(contador)
~~~~

- B
~~~~python
for contador in range(1, 11):
    print(contador)
~~~~

- C
~~~~python
for contador range in(1, 11):
    print(contador)
~~~~





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

- B
~~~~python
for contador in range(1, 11):
    print(contador)
~~~~

Correto!

Muito cuidado com o for .. range. A posição final é não-inclusiva, por isso que para imprimirmos de 1 até 10, usamos 11 como posição final!