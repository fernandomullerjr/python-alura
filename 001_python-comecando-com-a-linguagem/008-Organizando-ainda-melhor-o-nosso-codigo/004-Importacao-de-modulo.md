
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 8 - aula 04 Importação de módulo."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04 Importação de módulo

Marlon criou dois arquivos chamados a.py e b.py. Segue conteúdo de cada um:

~~~~python
# arquivo a.py
print('executando a')
# arquivo b.py
print('executando b')
~~~~


Ele ainda criou um terceiro arquivo chamado principal.py. Para testar se aprendeu corretamente a importar um módulo criado por ele mesmo, ele fez o seguinte em principal.py

~~~~python
# principal.py

import a
import b
~~~~

O que acontecerá quando Marlon executar através do terminal o programa principal.py?

Selecione uma alternativa

Será exibido os textos:

executando a
executando b

Será exibido apenas

executando b

Nada será exibido


Será exibido apenas

executando a




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

Será exibido os textos:

executando a
executando b

Correto!