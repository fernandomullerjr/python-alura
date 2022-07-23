
# Aula 09 - Tipagem do Python

- Ainda no console do Python, vimos no vídeo anterior que uma variável sempre terá um tipo associado:

pais = "Brasil"
type(pais)

Resultado

<class 'str'>


- Mas em nenhum local definimos explicitamente que a variável pais receberá valores do tipo string. Talvez você já tenha visto isso em outras linguagens, como C, C++, Java, em que definimos o tipo da variável na hora da sua declaração, algo como:

str pais = "Brasil"



- Mas isso em Python não funciona. Ou seja, no mundo Python não somos obrigados a definir explicitamente o tipo da variável. Podemos até passar outros tipos de valores para a variável:

- Primeiro teste:

pais = "Brasil"
type(pais)

Resultado

<class 'str'>



- Segundo teste:

pais = 644
type(pais)

Resultado

<class 'int'>



# Tipagem dinâmica
- Além de funcionar, o tipo da variável também muda! O tipo da variável mudou dinamicamente, de acordo com o valor que é atribuído a ela, logo, o tipo da variável é definido de acordo com o valor que ela guarda, isso faz parte da tipagem dinâmica do Python.
Agora temos tudo para começar o nosso projeto no próximo capítulo!


- Novo teste:

pais = 7.9
type(pais)

>>> pais = 7.9
>>> type(pais)
<class 'float'>
>>>
