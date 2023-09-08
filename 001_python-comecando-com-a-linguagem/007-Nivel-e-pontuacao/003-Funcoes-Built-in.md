
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 7 - aula 03 Funções built-in."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Funções built-in

Já vimos algumas funções built-in nesse curso!

O que sabemos sobre essas funções built-in? Assinale a afirmação correta!

Selecione uma alternativa

Fazem parte da biblioteca padrão do Python, mas não podem ser chamadas em qualquer lugar.


Fazem parte da biblioteca padrão do Python, mas precisam ser importadas.


Estão automaticamente disponíveis e podem ser chamadas em todo lugar do nosso código.


São apenas as funções: print(..) type(..), abs(), input(..) e int.






# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Funções built-in

## RESPOSTA

Estão automaticamente disponíveis e podem ser chamadas em todo lugar do nosso código.

Correto!



As funções built-in podem ser chamadas a qualquer momento, em todos os lugares. Exemplo de funções são type(..), abs(), input(..) ou int.

Segue também o link da documentação (em inglês): https://docs.python.org/3/library/functions.html