

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 1 - aula 09 Para saber mais: built-in"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  09 Para saber mais: built-in

No curso anterior, falamos bastante sobre as funções built-in, como type(..), int() ou input(..). Lembrando que funções built-in são aquelas que você não precisa importar explicitamente, pois elas estão disponíveis para seu uso automaticamente.

Existe uma função relacionado com o tipo bool, com o mesmo nome. Veja o código abaixo:

>>> bool(0)
False
>>> bool("")
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(-100)
True
>>> bool(13.5)
True
>>> bool("teste")
True
>>> bool(True)
True

Repare que os valores vazios ou zeros são considerado False, do contrário são considerados True.

A função executa por baixo dos panos algo que se chama de "Truth Value Testing". Isto é, decidir quando um valor é considerado True ou False.