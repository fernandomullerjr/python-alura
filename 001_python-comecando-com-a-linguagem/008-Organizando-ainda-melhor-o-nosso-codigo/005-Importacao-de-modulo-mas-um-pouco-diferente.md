
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 8 - aula 05 Importação de módulo, mas um pouco diferente."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 Importação de módulo, mas um pouco diferente

Fernanda, assim como seu amigo Marlon, criou dois arquivos chamados a.py e b.py. Segue o conteúdo de cada um:

~~~~python
# arquivo a.py
def executa():
    print("Executando a")
~~~~

~~~~python
# arquivo b.py
def executa():
    print("Executando b")
~~~~


Ela criou também aquele terceiro arquivo chamado principal.py. Para testar se aprendeu corretamente a importar um módulo criado por ela mesmo, ela fez o seguinte em principal.py

~~~~python
# principal.py

import a
import b
~~~~

Agora qual é a saída ao executar o arquivo principal.py?

Selecione uma alternativa

Um erro acontecerá.


Será exibido os textos:

executando a
executando b

Nada será exibido.







# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

Nada será exibido.


Correto!

Como os códigos dos arquivo a.py e b.py foram definidos dentro de uma função, sendo assim, a importação de a e b por principal não executa automaticamente o código contido neles. Para isso, precisamos explicitar que queremos executar esses código em principal. Vejamos:

~~~~python
# principal.py

import a
import b

a.executa()
b.executa()
~~~~




