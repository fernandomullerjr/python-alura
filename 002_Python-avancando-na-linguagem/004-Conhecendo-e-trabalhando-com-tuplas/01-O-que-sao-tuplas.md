
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 01 O que são tuplas?"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 O que são tuplas?

## Transcrição

No capítulo anterior, vimos que strings e listas são tipos de sequências. Além dessas sequências, também há o range, que vimos no curso anterior, e a tupla, que veremos agora.
Conhecendo mais uma sequência, a tupla

Nós gostaríamos de definir os dias da semana, então podemos defini-los em uma lista:

>>> dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

Faz sentido apagar um dia da semana? Provavelmente não, já que a semana sempre possui sete dias. Assim como também não faz sentido criarmos um novo dia da semana, mas nada nos impede de criarmos um:

>>> dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
>>> dias.append("Sábado2")
>>> dias
['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Sábado2']

Portanto, essa lista deveria ser fixa, inalterável. Para isso existe o tuple, que é uma lista imutável.
Criando uma tupla

Para criar uma tupla, é bem simples. É do mesmo jeito que criamos uma lista, mas ao invés de usar colchetes, usamos parênteses:

>>> dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
>>> type(dias)
<class 'tuple'>

Agora não conseguimos adicionar, nem remover elementos. Por exemplo:

>>> dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
>>> dias.append("Sábado2")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'