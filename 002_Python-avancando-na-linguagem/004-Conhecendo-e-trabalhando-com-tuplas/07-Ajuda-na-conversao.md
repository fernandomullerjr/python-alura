
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 07 Ajuda na conversão"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 07 Ajuda na conversão

O Pedro é um desenvolvedor Python Junior e precisa corrigir o código abaixo que está dando erro:

nomes = ("Nico", "Douglas", "Flavio", "Daniel")
#AQUI
nomes.append("Fabio") 

Quais alternativas ele pode usar no lugar de #AQUI para o código funcionar, independente do resultado?
Selecione 2 alternativas

    nomes = tuple(nomes)

    nomes = (nomes)

    nomes = nomes[0]

    nomes = []

    nomes = list(nomes)




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

nomes = []

Correto! Nomes será uma lista vazia.
Alternativa correta

nomes = list(nomes)

    Correto! Estamos usando a função list para criar uma lista baseando-se nos valores da tuple nomes.

Lembrando que para transformar um tuple em uma lista, temos a função list(..). Se queremos transformar de list para tuple devemos usar tuple(..) Ambas são funções built-in.
