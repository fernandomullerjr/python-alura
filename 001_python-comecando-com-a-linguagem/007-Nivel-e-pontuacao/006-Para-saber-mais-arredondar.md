
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
# 06 Para saber mais: arredondar no Python 2 e no Python 3

Nos exercícios, perguntamos como arredondar valores. Olhando nas funções built-in do Python, encontramos a função round, por exemplo:

>>> round(3.5)
4

O interessante é que a função round também mudou entre Python 2 e Python 3!

Por exemplo, executando round(3.5) no Python 3 dará o valor 4 (tipo inteiro), e com Python 2 dará o valor 4.0 (tipo decimal).

round

Ou seja, o Python 3 sempre devolve um valor do tipo int, enquanto o Python 2 devolve o tipo float.

Além disso, arredondando o valor 4.5 com Python 2, dará o valor 5.0 e no Python 3 dará o valor 4! Veja a imagem abaixo comparando Python 2 com Python 3:

round

O Python 3 usa uma forma de arredondar, que também é chamado de Banker's rounding. Nessa forma, os valores são arredondados para o número que for mais próximo, por exemplo: 2.4 seria arredondado para 2, todavia 2.6 já seria arredondado para 3. Quando um valor é igualmente próximo de dois números, por exemplo 2.5, que possui 0.5 de diferença tanto para o número 2 quanto para o número 3, esse é arredondado para o valor par mais próximo, que, nesse caso, seria o número 2. Vale lembrar que somente os números x.5 recebem o tratamento "especial" do arredondamento para o valor par mais próximo, nos demais, o arredondamento ocorre conforme esperado.

Mais informações se encontram na documentação do Python 3: https://docs.python.org/3.5/library/functions.html#round



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Round

Detalhes sobre o funcionamento do arredondamento, usando a função round

https://docs.python.org/3.5/library/functions.html#round
<https://docs.python.org/3.5/library/functions.html#round>

round(número[, dígitos])

     Retorna o número arredondado para precisão de dígitos após a vírgula decimal. Se ndigits for omitido ou for None, ele retornará o número inteiro mais próximo de sua entrada.

     Para os tipos integrados que suportam round(), os valores são arredondados para o múltiplo mais próximo de 10 elevado à potência menos dígitos; se dois múltiplos forem igualmente próximos, o arredondamento será feito para a escolha par (assim, por exemplo, tanto round(0,5) quanto round(-0,5) são 0, e round(1,5) é 2). Qualquer valor inteiro é válido para dígitos (positivo, zero ou negativo). O valor de retorno é um número inteiro se chamado com um argumento, caso contrário, é do mesmo tipo que número.

     Para um número geral de objeto Python, round(number, ndigits) delega para number.__round__(ndigits).




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESUMO

- Executando round(3.5) no Python 3 dará o valor 4 (tipo inteiro), e com Python 2 dará o valor 4.0 (tipo decimal).
- Python 3 sempre devolve um valor do tipo int, enquanto o Python 2 devolve o tipo float.
- Arredondando o valor 4.5 com Python 2, dará o valor 5.0 e no Python 3 dará o valor 4.
- O Python 3 usa uma forma de arredondar, que também é chamado de Banker's rounding. 