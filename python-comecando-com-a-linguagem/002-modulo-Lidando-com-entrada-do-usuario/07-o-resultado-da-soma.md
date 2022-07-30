
# Aula 07 - O resultado da soma é...

- Temos o seguinte código:

~~~~python
idade1 = 10
idade2 = "20"
print(idade1 + idade2)
~~~~

Qual das opções abaixo possui o resultado do código? Fique à vontade de testar esse código no console do Python.

Alternativa correta
O código não funciona!
Correto!

O código na verdade não funciona, e exibe a seguinte mensagem de erro no console:
    unsupported operand type(s) for +: 'int' and 'str'


D:\OneDrive\Documents\Dev\Python\Alura\Python-comecando-com-a-linguagem\002-modulo\venv\Scripts\python.exe D:/OneDrive/Documents/Dev/Python/Alura/Python-comecando-com-a-linguagem/002-modulo/07-resultado-da-soma-errado.py
Traceback (most recent call last):
  File "D:\OneDrive\Documents\Dev\Python\Alura\Python-comecando-com-a-linguagem\002-modulo\07-resultado-da-soma-errado.py", line 3, in <module>
    print(idade1 + idade2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Process finished with exit code 1


Isso acontece porque não podemos realizar uma operação de soma envolvendo uma string. Para resolvermos o problema, podemos apelar para a função int(), que converte uma string que contém um número, em um número inteiro:

~~~~python
idade1 = 10
idade2 = int("20")
print(idade1 + idade2)
~~~~


- Testando o corrigido:
D:\OneDrive\Documents\Dev\Python\Alura\Python-comecando-com-a-linguagem\002-modulo\venv\Scripts\python.exe D:/OneDrive/Documents/Dev/Python/Alura/Python-comecando-com-a-linguagem/002-modulo/07-resultado-da-soma-corrigido.py
30

Process finished with exit code 0
