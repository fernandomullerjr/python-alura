

# Aula 01 - A condição elif

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
