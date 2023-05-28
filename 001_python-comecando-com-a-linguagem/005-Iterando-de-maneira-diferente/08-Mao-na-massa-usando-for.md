# 08 Mão na massa: Usando for

PRÓXIMA ATIVIDADE

Como apresentamos no vídeo, substitua o laço while com o for. A função range deve gerar uma sequência de 1 até total_de_tentativas + 1:

~~~~python
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
~~~~

No final do código, não esqueça de remover a linha que incrementa a variável rodada. Lembrando, o incremento é automaticamente feito pelo laço for.

## Encerrando o jogo
Dentro do if, se acertarmos, devemos parar e sair do laço para parar o jogo.

Para tal, use o comando break:

~~~~python
if (acertou):
    print("Você acertou!")
    break
~~~~


## Limitando a entrada
Para limitar o número que o usuário deve digitar, altere a mensagem da função input:

~~~~python
chute_str = input("Digite um número entre 1 e 100: ")
~~~~

Agora verifique o número digitado através de um novo if, logo após a declaração da variável chute. Use o comando continue para continuar com a próxima iteração:

~~~~python
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
~~~~

## Rodando o jogo
Rode o programa e teste uma entrada inválida (-1, por exemplo).