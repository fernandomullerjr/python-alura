


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 1 - aula  08 Tipo Booleano"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 08 Tipo Booleano

Qual é o tipo que representa verdadeiro ou falso no mundo Python?

Selecione uma alternativa

bool


int


bool()


boolean








# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA


boolean


Errado!

Devemos utilizar o tipo bool para representar verdadeiro (True) e falso (False), por exemplo:

>>> existe = True
>>> type(existe)
<class 'bool'>

Dica: Nesse tipo de perguntas, sinta-se sempre à vontade de usar a documentação do Python. Aliás, aconselhamos a usar a documentação para se acostumar. É um documento bastante técnico e menos didático, mas ajuda tirar dúvidas pontuais: https://docs.python.org/3.5/index.html