



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 5 - aula 11 O resultado da interpolação."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# O resultado da interpolação
 

Temos as seguintes instruções:

~~~~PYTHON
"R$ {:7.1f}".format(1000.12)
"R$ {:07.2f}".format(4.11)
~~~~

Será impresso respectivamente no console:

Alternativa correta
R$  1000.1
R$ 0004.11

Correto.

Alternativa correta
R$ 1000.12
R$    4.1

Alternativa correta
R$ 1000.12
R$ 0004.11

A resposta correta é:

R$  1000.1
R$ 0004.11
Vejamos:

~~~~PYTHON
"R$ {:7.1f}".format(1000.12)
~~~~

No exemplo acima, queremos um número com 7 casas inteiras, sendo uma delas decimal, resultado é:
R$  1000.1


Agora, veja outro trecho:
~~~~PYTHON
"R$ {:07.2f}".format(4.11)
~~~~

Neste exemplo, queremos um número com 7 casas inteiras, sendo duas delas decimais, resultado é R$ 0004.11. Como colocamos um número de casas inteiras superior a quantidade de casas inteiras do número, o Python coloca 0 (zeros) à esquerda, conforme especificado no primeiro parâmetro entre as chaves, logo após os dois pontos, o 0 (zero). Interessante também é que a função format até arredonda, por exemplo:

~~~~PYTHON
"R$ {:7.1f}".format(1000.16)
~~~~

Retorna:
R$  1000.2








# GPT

- Explicação mais detalhada.

USANDO isto, o que ocorre no Python?

~~~~PYTHON
"R$ {:7.1f}".format(1000.12)
"R$ {:07.2f}".format(4.11)
~~~~

ChatGPT

No Python, o código apresentado seria usado para formatar valores numéricos como strings formatadas. Vejamos o que acontece com cada linha de código:

    "R$ {:7.1f}".format(1000.12):
        Essa linha formata o valor 1000.12 como uma string formatada, com um espaço reservado para um número de ponto flutuante com uma casa decimal.
        A string formatada terá um total de 7 caracteres, incluindo o caractere de prefixo "R$" e o espaço reservado para o número.
        O resultado será a string 'R$ 1000.1'.

    "R$ {:07.2f}".format(4.11):
        Essa linha formata o valor 4.11 como uma string formatada, com um espaço reservado para um número de ponto flutuante com duas casas decimais.
        A string formatada terá um total de 7 caracteres, incluindo o caractere de prefixo "R$" e o espaço reservado para o número.
        O resultado será a string 'R$ 004.11'.

Essas operações de formatação de string são úteis para exibir valores numéricos de maneira específica, como adicionar um prefixo, definir o número de casas decimais e controlar a largura total da string formatada. O método format() é usado para aplicar a formatação desejada aos valores numéricos.