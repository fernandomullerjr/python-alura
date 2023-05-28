
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 03 - If e while."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 if e while

O que o if e while tem em comum?

Alternativa correta
Ambos possuem uma condição de entrada.
    Correto!


Ambos servem para testar uma condição e executar um bloco uma única vez.
    Errado! Isso serve apenas para o if.


Ambos possuem uma condição de saída.
    Errado! O Python não possui um laço com uma condição de saída, que também é chamado de do-while.


Ambos servem para testar uma condição e executar um bloco enquanto a condição for verdadeira.
    Errado! Isso serve apenas para o while.



Ambos, if e while, possuem uma condição de entrada. A diferença é que o if executa o bloco apenas uma vez, mas o while repete o bloco enquanto a condição for verdadeira.
O interessante é que o Python não possui um laço com uma condição de saída, que outras linguagens chamam de do-while.