
# Aula 04 - Impossível acertar o número

- Romário, seguindo o que foi aprendido neste curso, resolveu testar o código que compara o chute digitado pelo usuário com um número secreto definido no programa.

~~~~python
numero_secreto = 42
chute = input("Digite seu número")
print("Você digitou ", chute)
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")
~~~~


Com base no código de Romário, temos as seguintes afirmações:

a) Sempre exibirá a mensagem Você errou, independentemente se o chute for igual ao número secreto
b) Todo valor retornado pela função input é um número.
c) É necessário converter o retorno de input para um número, no caso, um inteiro.

Sobre as afirmações anteriores, podemos dizer que:

Alternativa correta
Apenas B é falsa.

Correto!



# Explicando de forma detalhada
Não importa o número digitado, a comparação com == envolvendo tipos diferentes resultará em falso. Isso porque a função input sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro, para que a comparação com outro inteiro, no caso o numero_secreto, seja possível. Realizamos essa conversão através da função int.

Corrigindo o código:

~~~~python
numero_secreto = 42
chute_str = input("Digite seu número")
chute = int(chute_str)
print("Você digitou ", chute)
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")
~~~~

No lugar de criarmos outra variável, usamos a mesma para receber o valor da sua conversão.

