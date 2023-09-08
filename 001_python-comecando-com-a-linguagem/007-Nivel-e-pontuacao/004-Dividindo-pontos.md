



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 7 - aula 04  Dividindo pontos."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04  Dividindo pontos

Vimos no vídeo como calcular a pontuação do jogador. O cálculo foi simples e usamos a função abs(). Vale lembrar que a ordem da operação dentro da função abs() não irá interferir no resultado, pois, o objetivo dessa função é retornar o número desconsiderando o seu sinal:

~~~~python
pontos_perdidos = abs(chute - numero_secreto)   #pontos perdidos da rodada
pontos = pontos - pontos_perdidos               #subtraindo os pontos perdidos da pontuação total 
~~~~


Vamos mudar um pouco esse cálculo dos pontos perdidos. Agora não basta apenas calcular o valor absoluto, devemos também dividir esse valor por 3.

~~~~python
pontos_perdidos = abs(chute - numero_secreto) / 3     #dividindo por três
~~~~


Nada complicado aqui, mas pode surgir uma outra questão. Imagine que o chute é 21 e o número secreto é 32. Isso daria a seguinte conta:

~~~~python
pontos_perdidos = abs(21 - 32) / 3     #dividindo por três
~~~~

Que é:

~~~~python
pontos_perdidos = 11 / 3  
~~~~

Será que o Python consegue dividir 11 por 3? Se sim, qual será o tipo da variável pontos_perdidos? Faça o teste!

Selecione uma alternativa

Não consegue e dá erro.

Alternativa correta
Consegue sim e o tipo será int.


Alternativa correta
Consegue sim e o tipo será number.


Alternativa correta
Consegue sim e o tipo será float.





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04  Dividindo pontos

## RESPOSTA

Consegue sim e o tipo será float.


Correto!

Você pode testar isso facilmente no console do Python3:

>>> pontos_perdidos = 11 / 3
>>> type(pontos_perdidos)
<class 'float'>
Agora temos um outro problema. Ao imprimir esse cálculo, percebemos muitas casas decimais:

>>> print(pontos_perdidos)
3.6666666666666665

Bom, já aprendemos a formatar números decimais (lembre-se do {:7.2f}), mas nesse caso não é uma questão de formatação! Gostaríamos de arredondar o número, ou seja o valor decimal 3.66666 deve ser transformado para o valor 4.

Será que você se lembra da função built-in para o arredondamento?



- Testando no meu ambiente, no Debian:

~~~~bash

fernando@debian10x64:~$ python3
Python 3.8.3 (default, Jun  4 2023, 19:15:23)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> pontos_perdidos = 11 / 3
>>>
>>> type(pontos_perdidos)
<class 'float'>
>>>
>>> print(pontos_perdidos)
3.6666666666666665
>>>


~~~~