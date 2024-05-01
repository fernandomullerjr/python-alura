Raw Strings

A raw string literal is preceded by r or R, which specifies that escape sequences in the associated string are not translated. The backslash character is left in the string:

>>> print('foo\nbar')
foo
bar
>>> print(r'foo\nbar')
foo\nbar

>>> print('foo\\bar')
foo\bar
>>> print(R'foo\\bar')
foo\\bar



## RESUMO

- As letras "r" ou "R" no inicio de uma string, fazem o Escapes não serem traduzidos.