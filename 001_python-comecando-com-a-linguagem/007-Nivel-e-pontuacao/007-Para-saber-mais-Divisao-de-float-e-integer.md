


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 7 - aula  06 Para saber mais: arredondar no Python 2 e no Python 3."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 07 Para saber mais: Divisão de float e integer

Nos exercícios falamos sobre a divisão entre dois inteiros. Para ilustrar, execute no console:

>>>  3 / 2
1.5
Repare que recebemos o valor float 1.5 como resposta. O operador / sempre traz um float, mesmo se não for necessário, por isso ele também é chamado de float division:

>>>  2 / 2
1.0
No entanto, existe um outro operador bem parecido, o //. Tente executar:

>>>  3 // 2
Qual foi o resultado?

Selecione uma alternativa

1


2


1.5




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

O resultado é 1, um valor inteiro (int).

O operador // também é chamado integer division e sempre devolve o valor inteiro (sem arredondar).

Para realmente concluir o tópico, saiba que o Python 2 só tem integer division, mesmo tendo os dois operadores / e // ! No Python 2 não existe diferença entre os dois operadores,