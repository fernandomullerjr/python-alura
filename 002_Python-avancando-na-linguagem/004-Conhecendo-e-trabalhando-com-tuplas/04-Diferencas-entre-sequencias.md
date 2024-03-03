
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 04 Diferenças entre sequências"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04 Diferenças entre sequências

Quais são as principais diferenças entre as sequências do tipo list e tuple?
Selecione 2 alternativas

    list usa colchetes [] para inicialização, tuple usa parênteses ()

    list possui um índice, tuple não

    list é mutável, tuple é imutável

    list não pode ser usado no laço for, tuple sim

    list tem um limite de valores, tuple não


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

Uma diferença que encontramos entre list e tuple é na hora de criá-las, em que usamos [] ou ():

>>> lista = [4,3,2,1]
>>> tuple = (4,3,2,1)

Outra diferença é a questão de podermos alterar a sequência ou não. Listas podem ser alteradas, podendo adicionar ou remover elementos. Tuples, uma vez criadas, não podem ser alteradas. Tuples são imutáveis .