



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 7 - aula  05 Mão na massa: Níveis e Pontuação."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 Mão na massa: Níveis e Pontuação

Definindo o nível
Como vimos na aula, pergunte ao usuário qual nível de dificuldade ele quer. Para tal, capture o que ele digitar, já convertendo o valor para inteiro e guardando em uma variável:

~~~~python
total_de_tentativas = 0

print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível: "))
~~~~


Sabendo o nível, redefina a variável total_de_tentativas, baseado no nível:

~~~~python
if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
~~~~

Calculando a pontuação
A pontuação inicial é de 1000 pontos. Para isso, defina a variável pontos no início do nosso jogo:

~~~~python
pontos = 1000
~~~~

Quando o usuário não acertar o número secreto, calcule os pontos_perdidos. Para tal, subtraia o chute do numero_ secreto, considerando apenas o valor absoluto. Adicione o código abaixo no bloco else:

~~~~python
pontos_perdidos = abs(numero_secreto - chute)
~~~~

Logo abaixo, subtraia os pontos_perdidos dos pontos:

~~~~python
pontos_perdidos = abs(numero_secreto - chute)
pontos = pontos - pontos_perdidos
~~~~

Por fim, falta exibirmos a pontuação final ao usuário. Altere a mensagem de acerto do usuário, acrescentando a pontuação total. Use novamente a interpolação de strings:

~~~~python
print("Você acertou e fez {} pontos!".format(pontos))
~~~~

Na mensagem de erro, acrescente um if para exibir, ao final do jogo, qual era o número secreto que não foi adivinhado e a pontuação final do usuário, mesmo que ele não tenha vencido a partida.

O 'if(maior)' vai ficar assim:

~~~~python
if(maior):
    print("O seu chute foi maior que o número secreto")
    if (rodada == total_de_tentativas):
        print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
~~~~

O 'if (rodada == total_de_tentativas):' ficará igual tanto dentro da cláusula 'elif(menor)'.

Teste o seu jogo e verifique o nível e a pontuação!









# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 Mão na massa: Níveis e Pontuação

- Testando

~~~~bash
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/007-Nivel-e-pontuacao/005-nova-versao-pontuacao.py
*********************************
Bem vindo ao jogo de Adivinhação!
*********************************
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Defina o nível: 3
Tentativa 1 de 5
Digite o seu número: 100
Você digitou:  100
Você errou! O seu chute foi maior que o número secreto.
Tentativa 2 de 5
Digite o seu número: 99
Você digitou:  99
Você errou! O seu chute foi maior que o número secreto.
Tentativa 3 de 5
Digite o seu número: 98
Você digitou:  98
Você errou! O seu chute foi maior que o número secreto.
Tentativa 4 de 5
Digite o seu número: 97
Você digitou:  97
Você errou! O seu chute foi maior que o número secreto.
Tentativa 5 de 5
Digite o seu número: 96
Você digitou:  96
Você errou! O seu chute foi maior que o número secreto.
O número secreto era 54. Você fez 822
Fim do jogo
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$ date
Fri 08 Sep 2023 09:19:53 PM -03
fernando@debian10x64:~$
~~~~