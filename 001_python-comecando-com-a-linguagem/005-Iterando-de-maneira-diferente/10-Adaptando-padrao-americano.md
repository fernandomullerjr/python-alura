



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 5 - aula 10 Adaptando o Padrão Americano."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# ## 10 Adaptando o Padrão Americano


Um desenvolvedor Python está tendo que adaptar um sistema americano de cadastro de clientes americanos para os clientes brasileiros. Ele está esbarrando em um problema, pois lá as pessoas têm o costume de se referir pelo sobrenome antes do primeiro nome, por exemplo: Smith, John .

Ele deseja adaptar as mensagens do sistema para o padrão brasileiro, mas sem alterar a estrutura de dados que ele recebe do banco de dados.

Digamos que ele queira exibir a seguinte mensagem: "Ola Sr. Leonardo Cordeiro", como ele pode formatar a string para obter o resultado desejado?

Selecione uma alternativa

print("Ola Sr.{-1} {1}".format("Cordeiro","Leonardo"))

print("Ola Sr.{2} {1}".format("Cordeiro","Leonardo"))

print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))

print("Ola Sr.{0} {1}".format("Cordeiro","Leonardo"))






# Solucionando

Um desenvolvedor Python está tendo que adaptar um sistema americano de cadastro de clientes americanos para os clientes brasileiros. Ele está esbarrando em um problema, pois lá as pessoas têm o costume de se referir pelo sobrenome antes do primeiro nome, por exemplo: Smith, John .

Ele deseja adaptar as mensagens do sistema para o padrão brasileiro, mas sem alterar a estrutura de dados que ele recebe do banco de dados.

Digamos que ele queira exibir a seguinte mensagem: "Ola Sr. Leonardo Cordeiro", como ele pode formatar a string para obter o resultado desejado?

Alternativa correta
print("Ola Sr.{-1} {1}".format("Cordeiro","Leonardo"))

Alternativa correta
print("Ola Sr.{2} {1}".format("Cordeiro","Leonardo"))

Alternativa correta
~~~~PYTHON
print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))
~~~~
Correto!

Alternativa correta
print("Ola Sr.{0} {1}".format("Cordeiro","Leonardo"))

Com o .format(), podemos especificar a ordem em que os parâmetros aparecem na string, basta apenas colocar entre as chaves ({}) da string formatada qual parâmetro você quer exibir. É válido lembrar também, que o primeiro parâmetro é o zero, pois tradicionalmente na computação começamos contando de zero, ou seja, no nosso caso:

print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))COPIAR CÓDIGO
O primeiro parâmetro, representado pelo 0** é Cordeiro, e o segundo, que é o **1, é o Leonardo. Assim, formatando a string, na hora de imprimir será exibido:

"Ola Sr. Leonardo Cordeiro"