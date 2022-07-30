
# Aula 08 - E o resultado agora?

- Temos o seguinte trecho de código:

~~~~python
nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)
~~~~

O resultado da operação é:

Alternativa correta
Não é possível concatenar as duas variáveis.
Errado!

Alternativa correta
Nico Steppat
Errado!

Alternativa correta
NicoSteppat
Correto!

A resposta correta é NicoSteppat.
O caractere + aqui não tem o significado de somar e sim de concatenar. Estamos concatenando (juntando) duas strings!
Repare também que não há espaço entre as palavras. Para que haja, basta fazer assim:

~~~~python
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)
~~~~


Lembrando que a função print automaticamente aplica um separador entre os valores. O separador é um espaço por padrão, mas pode ser reconfigurado pelo parâmetro sep:

~~~~python
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")
~~~~




# Testes

- Usando o sinal de + para concatenar:

D:\OneDrive\Documents\Dev\Python\Alura\Python-comecando-com-a-linguagem\002-modulo\venv\Scripts\python.exe D:/OneDrive/Documents/Dev/Python/Alura/Python-comecando-com-a-linguagem/002-modulo/08-concatenando-junto.py
NicoSteppat

Process finished with exit code 0



- Usando o separador "_" para concatenar:

D:\OneDrive\Documents\Dev\Python\Alura\Python-comecando-com-a-linguagem\002-modulo\venv\Scripts\python.exe D:/OneDrive/Documents/Dev/Python/Alura/Python-comecando-com-a-linguagem/002-modulo/08-concatenando-com-separador-diferente.py
Nico_Steppat

Process finished with exit code 0


- Usando a virgula para separar as strings/concatenar, fazendo que haja um espaço entre elas:

D:\OneDrive\Documents\Dev\Python\Alura\Python-comecando-com-a-linguagem\002-modulo\venv\Scripts\python.exe D:/OneDrive/Documents/Dev/Python/Alura/Python-comecando-com-a-linguagem/002-modulo/08-concatenando-com-espaco.py
Nico Steppat

Process finished with exit code 0
