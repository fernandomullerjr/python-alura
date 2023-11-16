
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 2 - aula 02 Buscando um caracter em uma string."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  02 Buscando um caracter em uma string

Temos a seguinte variável declarada, que armazena uma string:

~~~~python
palavra = "aluracursos"
~~~~

Com base na variável declarada anteriormente, marque somente as verdadeiras:

Selecione 2 alternativas

palavra.find('s') # resultado é 9

palavra.find("l") # resultado é 1

palavra.find("a") # resultado é 4

palavra.find("b") # resultado é -1






# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

Com base na variável declarada anteriormente, marque somente as verdadeiras:

Alternativa correta
palavra.find('s') # resultado é 9

Alternativa correta
palavra.find("l") # resultado é 1

Correto! Lembrando que as posições começam de 0 até o tamanho da string menos um. A posição 1 é a segunda letra, logo "l".

Alternativa correta
palavra.find("a") # resultado é 4

Alternativa correta
palavra.find("b") # resultado é -1

Correto! Quando a busca nada encontra, o resultado é sempre -1.

A função find encontra a primeira ocorrência do texto que estamos procurando e devolve o índice. Lembrando também que o índice começa com 0.

O find também aceita um segundo parâmetro, que define a partir de qual posição gostaríamos de começar, por exemplo:

>>> palavra = "aluracursos"
>>> palavra.find("a",1) #procurando "a" a partir da segunda posição 
4