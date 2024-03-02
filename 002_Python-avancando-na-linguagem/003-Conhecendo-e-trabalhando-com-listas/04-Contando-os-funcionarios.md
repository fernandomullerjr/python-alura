
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 3 - aula 04  Contando os funcionários."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04  Contando os funcionários

Marina precisava gerar um relatório sobre o último ano fiscal de sua empresa. Ela solicitou à equipe de TI que gerasse uma lista com todos os nomes dos funcionários da empresa.

Ela recebeu a lista, que era como a lista abaixo:

funcionarios = ['Astrid', 'Flavia', 'Talia', ... ,'Mauricio', 'Waldemar', 'Marina']

Marina estava acabando o relatório 10 minutos antes do prazo final de envio quando notou que além do nome de todos os funcionários, ela também precisava do total de funcionários! Como ela tinha pouco tempo e não conseguiria contar manualmente, precisou recorrer aos seus conhecimentos de Python para contar o número de itens da lista.

Qual comando abaixo retorna o número de funcionários corretos da empresa de Marina?
Selecione uma alternativa

    print(length(funcionarios))

    print(funcionarios.length)

    print(funcionarios.len())

    print(len(funcionarios))



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

print(len(funcionarios))

Correto! A função len() retorna a quantidade de itens das listas




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# maiores detalhes

A função do Python que retorna o número de itens em uma lista é len(). Você pode usá-la da seguinte forma:

~~~~python
minha_lista = [1, 2, 3, 4, 5]
tamanho_da_lista = len(minha_lista)
print(tamanho_da_lista)  # Isso imprimirá 5
~~~~
