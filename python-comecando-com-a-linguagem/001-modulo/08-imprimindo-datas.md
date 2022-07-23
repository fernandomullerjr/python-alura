
# Aula 08 - Imprimindo datas

- Para representar uma data, temos as variáveis dia, mes e ano:

dia = 15
mes = 10
ano = 2015

- Sem alterar as variáveis e sem passar nenhuma string adicional à função print(), como faríamos para ter como resultado da impressão, uma data formatada:
15/10/2015


- Podemos alterar o separador entre os valores que a função print() recebe, utilizando o parâmetro sep, que por padrão é um espaço em branco. Basta utilizá-lo, dizendo que seu valor será uma barra (/):

dia = 15
mes = 10
ano = 2015
print(dia, mes, ano, sep="/")

>>> dia = 15
>>> mes = 10
>>> ano = 2015
>>> print(dia, mes, ano, sep="/")
15/10/2015
>>>
