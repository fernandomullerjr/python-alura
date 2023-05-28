07
for com continue
PRÓXIMA ATIVIDADE

E se fosse o código abaixo usando for e continue?

~~~~python
i = 1
for i in range(1,8):
    if(i == 5):
        continue
    print(i)
~~~~

Qual será a saída no console?

Selecione uma alternativa

1
2
3
4
6
7

1
2
3
4

1
2
3
4
5
6
7


Qual será a saída no console?

Alternativa incorreta
1
2
3
4
6
7

Alternativa incorreta
1
2
3
4

Alternativa incorreta
1
2
3
4
5
6
7

Errado! Não pulamos apenas a iteração 5.

Pulamos apenas a iteração 5. A saída será:

1
2
3
4
6
7










# ###################################################################################################################################################################
# ###################################################################################################################################################################
# GPT
Como funciona o código abaixo:

~~~~python
i = 1
for i in range(1,8):
    # Se i for igual a 5, o comando continue é executado. 
    # Isso faz com que a iteração atual seja interrompida e o controle volte para o início do loop, ignorando qualquer 
    # código que esteja abaixo do continue nessa iteração.
    # Se i não for igual a 5, o programa executa o comando print(i), que exibe o valor atual de i.
    if(i == 5):
        continue
    print(i)
~~~~

ChatGPT

Esse código executa um loop for que itera sobre os valores no intervalo de 1 a 7 (inclusive). Dentro do loop, há uma verificação condicional com um if para verificar se o valor atual de i é igual a 5. Se for, o comando continue é executado, fazendo com que a iteração seja interrompida e o controle volte para o início do loop.

Vamos analisar o código passo a passo:

    A variável i é inicializada com o valor 1.
    O loop for é iniciado com i no valor 1 e percorre os valores no intervalo de 1 a 7 (inclusive). A cada iteração, o valor de i é atualizado automaticamente pelo loop.
    Dentro do loop, a condição if(i == 5): verifica se i é igual a 5.
    Se i for igual a 5, o comando continue é executado. Isso faz com que a iteração atual seja interrompida e o controle volte para o início do loop, ignorando qualquer código que esteja abaixo do continue nessa iteração.
    Se i não for igual a 5, o programa executa o comando print(i), que exibe o valor atual de i.
    O loop continua iterando até que todos os valores no intervalo de 1 a 7 tenham sido percorridos.

O resultado impresso pelo código será:

1
2
3
4
6
7

Observe que o número 5 é pulado devido ao uso do comando continue quando i é igual a 5.