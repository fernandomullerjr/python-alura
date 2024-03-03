
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 03 Funções importantes"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Funções importantes

Veja o código:

valores = ("a","b","c","d","e")
#AQUI

Dentre as funções abaixo, quais podem ser inseridas e executadas corretamente no lugar de #AQUI?
Selecione 3 alternativas

    len(valores)

    max(valores)

    del(valores[0])

    min(valores)



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

len
max
min


Importante saber que existem algumas funções que funcionam com todos os tipos de sequências como os built-ins: len, min e max.

O del também é uma função built-in, mas só funciona para sequências mutáveis como listas. Como o tuple é imutável, não podemos remover seus elementos, e logo o código dá erro.

Veja o mesmo exemplo correto usando uma lista:

~~~~python
valores = ["a","b","c","d","e"]
del(valores[0]) #funciona pois é lista
~~~~