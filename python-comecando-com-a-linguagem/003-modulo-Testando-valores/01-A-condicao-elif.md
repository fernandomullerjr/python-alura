

# Aula 01 - A condição elif

# Dia 09/08/2022

# Transcrição
No capítulo anterior começamos a implementar o jogo, vimos como capturar os dados digitados pelo usuário, como converter o valor e como fazer um if para saber se o usuário acertou ou não.

Nesse capítulo, vamos fazer com que o usuário possa dar vários chutes para tentar acertar o número, já que atualmente ele só tem uma tentativa. Mas antes disso, vamos implementar uma dica para o usuário, dizendo se o número que ele chutou é maior ou menor que o número secreto.

Para isso, precisamos mexer no bloco do else. Vamos ter que testar novamente, se o número for maior, imprimimos uma mensagem dizendo isso ao usuário, se for menos, diremos ao usuário que o número digitado é menor que o número secreto:

~~~~python
if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    if (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")
~~~~

Podemos testar e ver que tudo está funcionando perfeitamente.

- Testando:
teste para baixo

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/003-modulo-Testando-valores/01-adivinhacao-elif-teste1.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Fim do jogo
fernando@debian10x64:~$
~~~~

teste para cima

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/003-modulo-Testando-valores/01-adivinhacao-elif-teste1.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Digite o seu número: 45
Você digitou:  45
Você errou! O seu chute foi maior que o número secreto.
Fim do jogo
fernando@debian10x64:~$
~~~~


# else com condição de entrada

Podemos notar que, se o chute não for igual, nem maior que o número secreto, obviamente ele será menor, então o último if não é necessário:

~~~~python
if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor que o número secreto.")
~~~~


Mas para esses casos, podemos fazer um else com uma condição de entrada, o elif. Vamos utilizá-lo para deixar o código mais semântico, já que na prática não há diferença:

~~~~python
if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")
~~~~




# Melhorando a legibilidade do código

Podemos melhorar a legibilidade do nosso código, para que outros programadores que possam vir a desenvolver conosco o entendam melhor. Vamos deixar nossas condições mais claras, o que significa chute == numero_secreto, por exemplo? Que o usuário acertou, logo vamos extrair essa condição para uma variável:

~~~~python
acertou = chute == numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")
~~~~



Agora a condição if fica um pouco mais clara. Vamos fazer a mesma coisa para as outras duas condições:

~~~~python
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
~~~~

Podemos testar e ver que tudo continua funcionando como antes, mas agora com um código um pouco mais legível. No próximo vídeo implementaremos a chance do usuário poder dar vários chutes para tentar acertar o número secreto. Até lá!



- Efetuando testes com o novo formato:

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/003-modulo-Testando-valores/01-adivinhacao-elif-teste5.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Digite o seu número: 42
Você digitou:  42
Você acertou!
Fim do jogo
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/003-modulo-Testando-valores/01-adivinhacao-elif-teste5.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Digite o seu número: 33
Você digitou:  33
Você errou! O seu chute foi menor que o número secreto.
Fim do jogo
fernando@debian10x64:~$
~~~~