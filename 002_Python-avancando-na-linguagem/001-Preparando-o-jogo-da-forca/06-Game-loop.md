
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 1 - aula 06 Game Loop"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status





# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  06 Game Loop

## Transcrição
Agora já temos tudo pronto. Podemos desenvolver o nosso Jogo da Forca.

## Conhecendo o jogo

O jogo da forca também é um jogo de adivinhação, mas no caso o usuário deve adivinhar uma palavra secreta. No arquivo forca.py, já há a função jogar definida, onde ficará o código do nosso jogo:

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    print("Fim do jogo")
~~~~


E caso executemos o programa como programa principal, executamos essa função jogar. Verificamos isso através de um if:

~~~~python
if(__name__ == "__main__"):
    jogar()
~~~~




## Definindo a palavra secreta
Como no jogo devemos adivinhar uma palavra secreta, nada mais justo do que defini-la em uma variável. Por enquanto a palavra será fixa, com o nome de banana:

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    print("Fim do jogo")
~~~~

Mais à frente deixaremos essa palavra secreta mais dinâmica.



## Primeiros passos do jogo
Agora, enquanto o usuário estiver jogando, devemos ficar verificando se o usuário acertou a palavra secreta ou se ele perdeu (se "enforcou"), mas devemos fazer isso em quantas iterações?

O usuário continua jogando enquanto ele não acertar a palavra e enquanto ele ainda tiver tentativas para acertar a palavra, ou seja, enquanto ele não "se enforcar". Para representar esse loop, já conhecemos o while:

~~~~python
palavra_secreta = "banana"

while(não acertou E não enforcou):
    print("Jogando...")
~~~~

Mas o que colocamos como condição do while, está em português e não existe em Python, logo isso não funcionará.

No caso de se enforcar, podemos ter dois valores, ou o usuário se enforcou, ou não. Logo, podemos ter os valores verdadeiro ou falso.



## O tipo bool

Nas linguagens de programação, e no Python não é diferente, há um tipo específico para representar esses valores, o tipo bool. Ele pode ter os valores True (Verdadeiro) e False (Falso). Então vamos definir uma variável enforcou, que começará com o valor False:

~~~~python
palavra_secreta = "banana"

enforcou = False

while(não acertou E não enforcou):
    print("Jogando...")
~~~~

Criaremos também a variável acertou, que representa se o usuário acertou ou não a palavra. Ela também começará com o valor False, pois quando o jogo começa, o usuário ainda não acertou a palavra secreta:

~~~~python
palavra_secreta = "banana"

enforcou = False
acertou = False

while(não acertou E não enforcou):
    print("Jogando...")
~~~~

Agora podemos modificar a condição do while, mas a condição é não acertar a palavra e não se enforcar. Para representar o não, no Python existe a palavra chave de negação, o not. E para representar o E, existe o operador lógico and:

~~~~python
palavra_secreta = "banana"

enforcou = False
acertou = False

while(not acertou and not enforcou):
    print("Jogando...")
~~~~

Então, enquanto não acertamos a palavra e enquanto não nos enforcamos, continuamos jogando.

Daremos continuação à programação do nosso jogo no próximo capítulo :)









# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  06 Game Loop


fernando@debian10x64:~$ python3
Python 3.8.3 (default, Jun  4 2023, 19:15:23)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> enforcou = False
>>> type(enforcou)
<class 'bool'>
>>>




Como funciona exatamente a linha do while neste código?

~~~~python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
~~~~


ChatGPT

Neste código, a estrutura de controle while é usada para criar um loop que continuará executando até que a condição especificada não seja mais verdadeira. No caso deste código, o loop while é controlado pela expressão while(not acertou and not enforcou).

Vou explicar o funcionamento do loop passo a passo:

    Inicialização das variáveis:
        enforcou e acertou são inicializadas como False. Elas são usadas como flags para determinar se o jogador perdeu (enforcou) ou ganhou (acertou) o jogo.

    Condição do loop:
        O loop while continuará executando enquanto acertou for False e enforcou for False. Isso significa que o loop continuará enquanto o jogador não tiver acertado a palavra (acertou é False) e não tiver cometido erros suficientes para ser enforcado (enforcou é False).

    Execução do loop:
        Dentro do loop, há uma instrução print("Jogando..."). Esta linha será repetidamente impressa na tela enquanto a condição do loop for verdadeira.

    Atualização das variáveis dentro do loop:
        O loop while não tem instruções para atualizar as variáveis acertou e enforcou. Isso significa que, a menos que haja alguma alteração dentro do loop para tornar acertou ou enforcou verdadeiras, o loop será executado indefinidamente, criando um loop infinito.

Devido à ausência de código para alterar os valores de acertou ou enforcou dentro do loop, este código irá imprimir "Jogando..." infinitamente, e o programa nunca alcançará a linha print("Fim do jogo").

Para tornar o código funcional, você precisa adicionar lógica dentro do loop para verificar se o jogador acertou a palavra ou se foi enforcado, e então atualizar as variáveis acertou ou enforcou de acordo. Por exemplo, você pode adicionar lógica para receber entradas do jogador, comparar com a palavra secreta e verificar se o jogador cometeu erros o suficiente para ser enforcado.






User
pode me explicar melhor? e também sobre o not no while

ChatGPT

Certamente! Vamos analisar o trecho de código e entender o funcionamento do while e do operador not.

O while é uma estrutura de controle de fluxo em Python que permite que um bloco de código seja executado repetidamente enquanto uma condição específica seja verdadeira. A sintaxe geral do while é a seguinte:

~~~~python
while condição:
    # código a ser executado enquanto a condição for verdadeira
~~~~

Neste caso específico:

~~~~python
while (not acertou and not enforcou):
    print("Jogando...")
~~~~

O while está sendo usado para criar um loop que continuará a ser executado enquanto acertou for False e enforcou for False.

A palavra-chave not é um operador de negação em Python. Ele inverte o valor da expressão booleana. Ou seja, se a expressão for True, not torna-a False, e se for False, not torna-a True.

Dentro do contexto do seu código, not acertou significa "enquanto não acertou" e not enforcou significa "enquanto não foi enforcado". O while continuará executando o código dentro dele enquanto ambas as condições forem verdadeiras, ou seja, enquanto o jogador não tiver acertado a palavra (acertou é False) e não tiver sido enforcado (enforcou é False).

Aqui está uma explicação mais detalhada do que acontece no seu código:

    acertou e enforcou são inicializados como False.
        acertou é uma flag que indica se o jogador acertou a palavra secreta.
        enforcou é uma flag que indica se o jogador foi enforcado (ou seja, cometeu erros demais).

    O loop while começa a ser executado.
        Ele verifica se not acertou (ou seja, "não acertou") e not enforcou (ou seja, "não foi enforcado") são verdadeiros. Se ambas as condições forem verdadeiras, o código dentro do loop é executado.

    Dentro do loop, a mensagem "Jogando..." é impressa.
        Esta mensagem será impressa repetidamente enquanto as condições not acertou e not enforcou forem verdadeiras.

    No entanto, não há código dentro do loop para alterar os valores de acertou ou enforcou.
        Como resultado, as condições not acertou e not enforcou permanecerão sempre verdadeiras (pois acertou e enforcou são inicializados como False e não são alterados dentro do loop). Isso cria um loop infinito, onde a mensagem "Jogando..." será impressa continuamente e o programa nunca alcançará a linha print("Fim do jogo").

Para que o jogo funcione corretamente, você precisará adicionar lógica dentro do loop para receber a entrada do jogador, compará-la com a palavra secreta, verificar se a palavra foi adivinhada corretamente ou se o jogador cometeu erros demais (indicando que foi enforcado). Dependendo dessas verificações, você deve atualizar os valores de acertou ou enforcou para que as condições do while eventualmente se tornem falsas e o loop pare de ser executado.









pode me trazer mais exemplos do while, not e suas possibilidades? e maiores detalhes
ChatGPT

Certamente! O while e o operador not são fundamentais em Python, e eles podem ser combinados de várias maneiras para criar loops flexíveis e poderosos. Vou fornecer alguns exemplos e detalhes adicionais para ajudar a entender melhor como essas construções podem ser usadas.
1. Loop while Simples:

O while é usado para repetir um bloco de código enquanto uma condição é verdadeira. Por exemplo:

~~~~python

contador = 0
while contador < 5:
    print(contador)
    contador += 1
~~~~

Neste exemplo, o código dentro do while será repetido enquanto o contador for menor que 5.
2. Uso do Operador not:

O operador not inverte o valor de uma expressão booleana. Ele é útil quando você quer verificar se uma condição não é verdadeira. Por exemplo:

~~~~python

tem_cafe = False
if not tem_cafe:
    print("Por favor, faça café!")
~~~~


Neste caso, a mensagem será impressa porque not tem_cafe é True quando tem_cafe é False.
3. Combinando while e not:

Você pode usar while com not para criar loops que continuam até que uma certa condição seja verdadeira. Por exemplo, um loop que pede entrada do usuário até que um número positivo seja inserido:

~~~~python

numero = int(input("Digite um número positivo: "))
while not (numero > 0):
    print("Número inválido. Tente novamente.")
    numero = int(input("Digite um número positivo: "))
print("Obrigado! Você digitou um número positivo:", numero)
~~~~


Este loop continuará enquanto o número inserido não for maior que 0 (not (numero > 0)).
4. Loop Infinito com while True:

while True cria um loop infinito, que continua para sempre, a menos que seja interrompido por uma instrução break. Isso é frequentemente usado para criar menus interativos:

~~~~python

while True:
    opcao = input("Escolha uma opção (1, 2, ou 3): ")
    if opcao == "1":
        print("Você escolheu a opção 1.")
    elif opcao == "2":
        print("Você escolheu a opção 2.")
    elif opcao == "3":
        print("Você escolheu a opção 3.")
    else:
        print("Opção inválida. Tente novamente.")
~~~~


Neste exemplo, o loop continua indefinidamente até que o usuário escolha uma opção válida.
5. Loops Controlados por break e continue:

Você pode usar break para sair de um loop e continue para pular a iteração atual e continuar com a próxima. Por exemplo, um loop que conta até 10, mas para se encontrar com um número específico:

~~~~python

contador = 1
while contador <= 10:
    if contador == 5:
        print("Encontramos o número 5!")
        break
    print(contador)
    contador += 1
~~~~


Neste caso, quando contador é igual a 5, o loop é interrompido com a instrução break.

Espero que esses exemplos ajudem a entender melhor como o while e o operador not podem ser usados em Python! Se você tiver mais perguntas ou precisar de exemplos adicionais, sinta-se à vontade para perguntar.









# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  
## RESUMO

Neste caso específico:

~~~~python
while (not acertou and not enforcou):
    print("Jogando...")
~~~~

O while está sendo usado para criar um loop que continuará a ser executado enquanto acertou for False e enforcou for False.

A palavra-chave not é um operador de negação em Python. Ele inverte o valor da expressão booleana. Ou seja, se a expressão for True, not torna-a False, e se for False, not torna-a True.
