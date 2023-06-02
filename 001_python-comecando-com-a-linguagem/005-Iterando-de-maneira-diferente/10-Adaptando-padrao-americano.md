



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