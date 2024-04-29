
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

~~~~python
frutas = ["maçã", "banana", "laranja", "melancia"]
~~~~

Agora ele precisa criar uma nova lista com as mesmas frutas, mas tudo escrito em letras maiúsculas. Ele escreveu o laço abaixo:

~~~~python
lista = []
for fruta in frutas:
    lista.append(fruta.upper())
~~~~

O código funciona, mas será que você pode mostrar para ele como usar as List Comprehensions? Qual solução abaixo é relativa ao laço?
Selecione uma alternativa

~~~~python
    lista = [for fruta.upper() in frutas]

    lista = [fruta.upper() for fruta in frutas]

    lista = [for fruta in frutas fruta.upper() ]
~~~~





# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  RESPOSTA

- ERRADA:

lista = [for fruta in frutas fruta.upper() ]

    Errado! Primeiro devemos chamar a função fruta.upper() e depois usar o laço for.

O código com List Comprehension, que inicializaria a lista acima, seria:

frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]

Repare que é muito mais enxuto e, uma vez acostumado com a sintaxe, é até mais fácil de entender.



- CORRETA

lista = [fruta.upper() for fruta in frutas]

Correto! Criamos uma nova lista [] e dentro dos colchetes usamos a List Comprehension.

Código corrigido:

~~~~python
frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]
~~~~