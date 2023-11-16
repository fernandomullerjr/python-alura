
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 2 - aula 03 Iterando em uma palavra."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  04 Recordando...

Vamos recordar um exemplo de formatação de strings em Python:

~~~~python
a = "Cavalo"
b = "Calopsita"
print("{} e {}".format(b, a))
~~~~

O que será exibido no terminal?

Selecione uma alternativa

'Calopsita Cavalo'


'Cavalo e Calopsita'


'Calopsita e Cavalo'






# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

'Calopsita e Cavalo'


Correto! Nossa string possui duas lacunas definidas com {}. Os parâmetros passados para a função format são passados na mesma ordem para preencherem a lacuna.