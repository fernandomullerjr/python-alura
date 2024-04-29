
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 08 Loop relativo à List Comprehension"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#    08 Loop relativo à List Comprehension

João criou a seguinte lista:

frutas = ["maçã", "banana", "laranja", "melancia"]

Agora ele precisa criar uma nova lista com as mesmas frutas, mas tudo escrito em letras maiúsculas. Ele escreveu o laço abaixo:

lista = []
for fruta in frutas:
    lista.append(fruta.upper())

O código funciona, mas será que você pode mostrar para ele como usar as List Comprehensions? Qual solução abaixo é relativa ao laço?
Selecione uma alternativa

    lista = [for fruta.upper() in frutas]

    lista = [fruta.upper() for fruta in frutas]

    lista = [for fruta in frutas fruta.upper() ]

