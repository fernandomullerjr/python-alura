
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 3 - aula  02 Sistema para as frutas."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  02 Sistema para as frutas

Mariana montou o seguinte código Python para controlar se a sua barraca de frutas possui determinadas frutas solicitadas pelos seus clientes:

# coding: utf-8
frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

if(#####):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')

Qual código deve substituir o hasheado (#####) para que o programa funcione de modo esperado ?
Selecione uma alternativa

    frutas contains frutaPedida

    frutaPedida not in frutas

    frutas has frutaPedida

    fruta_pedida in frutas





# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  RESPOSTA

fruta_pedida in frutas

    Correto! Assim como nas Strings, podemos utilizar o operador in para verificar se um determinado elemento está dentro de uma lista.

Para verificar se um determinado elemento existe em uma Lista, podemos utilizar o operador in.Ele nos retorna True ou False caso o elemento esteja ou não dentro da lista verificada, tornado este processo de verificação bem simples!

O Python é uma linguagem de programação que nos facilita muito para trabalhar com estruturas de dados, pois ele já tem diversas funções e operadores que auxiliam as tarefas mais comuns em trabalhar com Listas e Strings , nos tornando programadores muito produtivos.



- Código corrigido:

~~~~python
# coding: utf-8
frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

if(fruta_pedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')
~~~~