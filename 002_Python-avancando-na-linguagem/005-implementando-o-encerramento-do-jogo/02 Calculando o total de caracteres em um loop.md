
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 02 Calculando o total de caracteres em um loop"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 02 Calculando o total de caracteres em um loop

Carlos criou um loop para calcular a quantidade de caracteres em uma palavra através do seguinte código:

~~~~PYTHON
total = 0
palavra = "python rocks!"
acabou = False
while (not acabou):
    #AQUI 
    total = total + 1
print(total - 1)
~~~~

O que Carlos precisa colocar dentro do while no lugar de #AQUI para que se encerre e consiga imprimir o total de caracteres da palavra?
Selecione uma alternativa

    acabou = True

    acabou = ( total == len(palavra) )

    acabou = ( total == 11 )




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA


acabou = ( total == len(palavra) )

    Correto! Carlos poderia ter simplesmente usado a própria função len, mas esse código definirá True para a variável acabou apenas quando total for igual ao tamanho da palavra.
