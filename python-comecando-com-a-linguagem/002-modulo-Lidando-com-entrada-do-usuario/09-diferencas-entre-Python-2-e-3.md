
# Aula 9 - Diferenças entre o Python 2 e 3

- Transcrição
Nesse vídeo veremos um pouco das diferenças entre o Python 3 e o Python 2, porque o Python 2 ainda é muito utilizado. Para esse vídeo, não é necessário instalar o Python 2, já que aqui só veremos as diferenças, a menos que você queira utilizá-lo.

A função print
A primeira diferença que podemos ver é que no Python 2, não precisamos colocar os parênteses na função print, eles são opcionais:

~~~~python
print "python2"
print("python2")
~~~~

- Resultado
python2
python2


- Já no Python 3, os parênteses são obrigatórios. Ainda na função print, no Python 2 não há os parâmetros sep e end, ao contrário do Python 3, e quando a função recebe mais de um valor, sua saída é diferente:

print("python", "2")

- Resultado:
('python', '2')



# A função input
Outra diferença que podemos ver é na função input. Sabemos que no Python 3, essa função sempre retornará uma string. Já no Python 2, ela automaticamente converte o tipo da variável. Por exemplo:

~~~~python
chute = input("Digite o seu número: ")
type(chute)
~~~~

- Resultado:
<type 'int'>


Isso foi considerado má prática, porque pode ou não ser a intenção do desenvolvedor converter o tipo da variável. Por isso é bem comum encontrar a função raw_input sendo utilizada no Python 2:

~~~~python
chute = raw_input("Digite o seu número: ")
type(chute)
~~~~

- Resultado:
<type 'str'>


O retorno dessa função será sempre uma string, equivalente à função input do Python 3, mas ela não existe nessa versão.
Ao longo do treinamento veremos mais diferenças entre as versões!





# Efetuando testes na console do Python nas versões 2 e 3

- No python2 temos a função raw_input.
- No Python2 os parenteses não são necessários.
- No Python2 NÃO temos opções de separador e end no print.

fernando@debian10x64:~$ python2
Python 2.7.16 (default, Oct 10 2019, 22:02:15)
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print "python2"
python2
>>> print("ola", "mundo")
('ola', 'mundo')
>>>
>>> print("ola", "mundo", sep="x")
  File "<stdin>", line 1
    print("ola", "mundo", sep="x")
                             ^
SyntaxError: invalid syntax
>>>
>>>
>>> chute_str = raw_input("Digite ")
Digite 32
>>> type(chute_str)
<type 'str'>
>>>



- No python3 não temos a função raw_input.
- No Python3 os parenteses são necessários.
- No Python 3 temos opções de separador e end no print.

fernando@debian10x64:~$ python3
Python 3.7.3 (default, Jan 22 2021, 20:04:44)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("python3")
python3
>>> print "python3"
  File "<stdin>", line 1
    print "python3"
                  ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("python3")?
>>>
>>>
>>> print("ola", "mundo")
ola mundo
>>>
>>>
>>> chute_str = raw_input("Digite ")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'raw_input' is not defined
>>>

