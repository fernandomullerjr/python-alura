
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 6 - 07 Lendo um arquivo por completo."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  07 Lendo um arquivo por completo

Dado um arquivo como o seguinte: frutas.txt

Banana
Maçã
Pera
Uva
Jamelão

Que foi aberto deste modo:

~~~~PYTHON
arquivo = open('frutas.txt','r')
~~~~

E quando executamos os comandos:

~~~~PYTHON
linha = arquivo.readline()
print(linha)
linha = arquivo.readline()
print(linha)
~~~~

É exibido corretamente as linhas:

Banana

Maçã

Mas quando abrimos o arquivo e usamos os comandos:

~~~~PYTHON
arquivo = open('frutas.txt','r')
conteudo = arquivo.read()
print(conteudo)
conteudo = arquivo.read()
print(conteudo)
~~~~

A primeira vez é exibida corretamente o conteudo, porém na segunda não é exibido nada. Por quê?
Selecione uma alternativa

    Se desejamos ler duas vezes o arquivo inteiro, temos que utilizar o modificador de acesso r+. O modificador de acesso r perde o efeito de leitura após a função read ser executada pela primeira vez.

    Pois o comando read() lê o arquivo inteiro de uma vez, colocando o ponteiro de leitura no final do mesmo. Se chamarmos a função read() novamente, como o ponteiro de leitura está no final, nada será lido.

    Pois como abrimos o comando com o modificador de acesso r, fica implícito que só tentaremos ler uma vez com a função read(), quando tentamos pela segunda vez obtemos um erro e a leitura é abortada.




# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  RESPOSTA

Pois o comando read() lê o arquivo inteiro de uma vez, colocando o ponteiro de leitura no final do mesmo. Se chamarmos a função read() novamente, como o ponteiro de leitura está no final, nada será lido.

Correto! Se desejarmos ler o arquivo novamente, devemos fechá-lo com o comando .close(), reabri-lo com o comando .open() e ai sim conseguiremos lê-lo por inteiro novamente.