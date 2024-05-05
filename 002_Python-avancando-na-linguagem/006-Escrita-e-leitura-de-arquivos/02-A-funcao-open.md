


02
A função open
Próxima Atividade

Se desejamos trabalhar com arquivos, precisamos primeiro abrí-lo utilizando a função open(). A função open() recebe um ou mais parâmetros. Em uma determinada ordem, quais são eles?
Selecione uma alternativa

    O nome do arquivo e o modificador de acesso.

    O modificador de acesso primário e o modificador de acesso secundário.

    O modificador de acesso e o nome de arquivo.




## RESPOSTA

O nome do arquivo e o modificador de acesso.

Correto! Precisamos informar qual é o nome do arquivo que queremos abrir, e podemos também informar qual modificador de acesso válido.


Importante é que não precisamos passar o modificador de acesso, pois o segundo parâmetro é opcional:

~~~~python
arquivo = open("entrada.txt")
~~~~

Nesse caso será utilizado o modo de leitura (r) por padrão.