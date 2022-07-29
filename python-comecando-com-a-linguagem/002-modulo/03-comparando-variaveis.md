
# Aula 03 - Comparando variáveis

# Transcrição
A ideia do nosso jogo é termos que acertar um número secreto. Quando o programa estiver rodando, teremos que digitar um número e o programa dirá se acertamos ou erramos o número, com várias tentativas e níveis.

Vamos começar definindo esse número secreto (mais à frente vamos ver como gerar um número aleatório):

~~~~python
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
~~~~


# Capturando a entrada do usuário
Agora, para que o usuário possa digitar o número, vamos utilizar a função input, ela trava o programa até que o usuário digite algo e tecle ENTER. Ela recebe por parâmetro a mensagem que será exibida no console e nos retorna o que o usuário digitou, logo vamos guardar esse resultado em uma variável, que chamaremos de chute:

~~~~python
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")
~~~~


Para testar, vamos ao final do programa imprimir o conteúdo da variável chute, para mostrar realmente que o seu conteúdo será o que o usuário digitou:

~~~~python
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")
print("Você digitou: ", chute)
~~~~

Podemos rodar o programa e ver que realmente é impresso o valor que digitarmos.





# Comparando valores
Agora que conseguimos capturar o que o usuário digitou, precisamos comparar esse valor com o número secreto, para poder dizer ao usuário se ele digitou o número correto ou não. Bom, já sabemos o número secreto que o chute do usuário, então vamos comparar os dois, algo como:

se numero_secreto igual chute
    print("Você acertou!")
senão
    print("Você errou!")

Só que as palavras se, senão e igual não funcionam no mundo Python, temos que respeitar a sua sintaxe. O se em Python é if, o igual é a comparação == e o senão é else. Então, resumindo a sintaxe do Python é:

~~~~python
if (condição):
    executa código caso a condição seja verdadeira
else:
    executa código caso a condição seja falsa
~~~~

Mas precisamos prestar atenção a alguns detalhes. É uma recomendação que a condição fique dentro de parênteses (apesar de também funcionar sem); para marcar o fim da instrução e início de um bloco (o código que será executado caso a condição seja verdadeira ou falsa), é utilizado dois pontos (:), e esse bloco obrigatoriamente deve estar 4 espaços (ou um TAB) mais à direita. Então o código ficará assim:

~~~~python
if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")
~~~~

Podemos rodar o programa e verificar que mesmo se digitarmos o número certo, recebemos a mensagem Você errou. Porque?

- Resultado:

D:\OneDrive\Documents\Dev\Python\Alura\Python-comecando-com-a-linguagem\002-modulo\venv\Scripts\python.exe D:/OneDrive/Documents/Dev/Python/Alura/Python-comecando-com-a-linguagem/002-modulo/03-comparando-variaveis.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Digite o seu número: 42
Você digitou:  42
Você errou!

Process finished with exit code 0






# Convertendo uma string para número inteiro
Isso acontece porque a função input nos retorna uma string, pois qualquer coisa pode ser digitada, não é garantido que o usuário irá digitar um número. Como não há essa garantia, o retorno é uma string.

Já a variável numero_secreto é um número! Logo, do tipo inteiro. Então estamos testando a igualdade de um inteiro com uma string, logo essa comparação sempre será falsa, apesar da string representar um número inteiro. Para resolver isso precisamos mudar o tipo da variável, convertendo uma string em número inteiro.

Para isso, o Python possui a função int, que recebe um valor e o converte para inteiro, justamente o que queremos. Logo, vamos utilizá-la no nosso código:

~~~~python
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")
~~~~



- Novo teste.

D:\OneDrive\Documents\Dev\Python\Alura\Python-comecando-com-a-linguagem\002-modulo\venv\Scripts\python.exe D:/OneDrive/Documents/Dev/Python/Alura/Python-comecando-com-a-linguagem/002-modulo/03-comparando-variaveis.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Digite o seu número: 42
Você digitou:  42
Você acertou!

Process finished with exit code 0



- Agora a comparação é feita corretamente! Para sair do bloco do else, basta escrevermos algo depois dele, sem a indentação de 4 espaços:

~~~~python
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo")
~~~~





# Testando na console do Python
- Testando e verificando os tipos dos valores, comparando eles e testando:

Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
chute = input("digite")
digite>? 42

type(chute)
<class 'str'>

numero_secreto = 42
type(numero_secreto)
<class 'int'>

numero_secreto == chute
False

numero = int(chute)
type(numero)
<class 'int'>

numero_secreto == numero
True




- Observação:
cuidar a identação no Python
usar 4 espaços ou TAB