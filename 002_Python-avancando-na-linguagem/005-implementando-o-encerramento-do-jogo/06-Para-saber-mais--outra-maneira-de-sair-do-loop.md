
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 06 Para saber mais: outra maneira de sair do loop"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  06 Para saber mais: outra maneira de sair do loop

Vimos nesse capítulo que as variáveis acertou e enforcou foram usadas para controlar a saída do loop. Enquanto elas não forem verdadeiras, o código dentro do loop será executado. Para que o loop seja encerrado, criamos atribuições para essas variáveis.

~~~~python
enforcou = erros == 6
acertou = "_" not in letras_acertadas
~~~~

Contudo, essa não é única maneira de sair de um loop. Podemos usar também a palavra reservada break que, quando executada, irá encerrar o loop naquele ponto. Como podemos alterar nosso código da forca para utilizar o break e sair do while?

