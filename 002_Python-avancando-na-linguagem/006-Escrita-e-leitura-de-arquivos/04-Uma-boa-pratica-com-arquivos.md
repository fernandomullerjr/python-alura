
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 6 - 04 Uma boa prática com arquivos."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  04 Uma boa prática com arquivos

É uma boa prática fecharmos o arquivo depois de utilizá-lo para escrita ou leitura, assim outros programas ou processos podem ter acesso ao arquivo e ele não fica preso apenas ao nosso script Python.

Qual das funções abaixo é utilizada para fechar um arquivo que foi aberto desse jeito:

arquivo = open('nome.txt', 'w')

Selecione uma alternativa

    arquivo.flush()

    arquivo.close()

    arquivo.clear()

    arquivo.end()




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

arquivo.close()

Correto! A função close é responsável por fechar o arquivo.


