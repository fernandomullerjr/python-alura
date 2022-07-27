
# Aula 07 - Personalizando a saída

- Veja o código a seguir:

~~~~python
subst = "Python"
verbo = "é"
adjetivo = "fantástico"
print(subst, verbo, adjetivo, sep="_", end="!\n")
~~~~


- Saída do script:
/home/fernando/cursos/python/alura/python-comecando-com-a-linguagem/001-modulo/07-personalizando-saida.py

fernando@debian10x64:~/cursos/python/alura/python-comecando-com-a-linguagem/001-modulo$ python3 07-personalizando-saida.py
Python_é_fantástico!
fernando@debian10x64:~/cursos/python/alura/python-comecando-com-a-linguagem/001-modulo$


- Repare que usamos o parâmetro sep="_" para definir um _ entre cada valor, por isso é impresso:
Python_é_fantástico

- Além disso, definimos através do end para definir o que deve ser impresso ao final da saída, neste caso imprimir uma exclamação (!), seguida pelo \n:
end="!\n"

- Lembrando que o \n é um caractere especial, que faz com que o novo prompt comece em uma nova linha.
Com isso recebemos a saída:
Python_é_fantástico!
>>>