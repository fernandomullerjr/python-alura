
# Aula 05 - Onde foi que ela errou?

- Fernanda, colocando em prática o que aprendeu neste capítulo, escreveu o seguinte código para testar se realmente aprendeu a criar uma condição if em seu código:

~~~~python
minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado)
    print('temos idades iguais')
else:
    print('temos idades diferentes')
~~~~


O problema é que o código dela não funciona. Consegue enxergar onde está o problema? Para quem está começando com Python, pode ser bem sutil. Descobriu? Clique em Ver Opinião do Instrutor, que você verá a resposta do instrutor.




# Opinião do instrutor

O problema é que para indicar o início do bloco if, é necessário utilizar dois pontos (:). Veja que no código dele faltou os dois pontos. O código corrigido ficará assim:

~~~~python
minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado):
    print('temos idades iguais')
else:
    print('temos idades diferentes')
~~~~

Importante também é sempre usar a indentação correta. Ou seja, depois da linha com o if, devemos usar 4 espaços ou pressionar a tecla tab para começar o novo bloco de código.