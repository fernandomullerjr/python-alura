
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 3 - aula 05 Um falso campeão."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 Um falso campeão

Romeu e seus colegas estavam competindo em um campeonato de futebol com o seu time 'Drible da emoção'.

Como ele era um dos organizadores, tinha de manter a colocação de cada um dos 4 times manualmente, levando em consideração diversos fatores como número de pontos, gols marcados e etc... Como Romeu era um estudante de Ciências da Computação, ele resolveu automatizar este processo todo em um script em Python, para facilitar sua vida e dedicar mais tempo aos treinos.

O seu script funcionou maravilhosamente bem, porém no dia de entrega dos resultados ele percebeu um erro. O script gerava a lista de colocação corretamente, porém na hora de exibir o resultado final com o campeão, ele sempre mostrava o segundo colocado em vez do primeiro colocado na Lista.

~~~~PYTHON
## Restante do código que gera a lista de colocação...

print(colocacao)
#Resultado: ['Drible da Emoção', 'Bruxos como Ronaldinho', 'Só golaço', '3x1 não é goleada']

campeao = colocacao[1]

print(' O grande campeão do torneio é o time ' + campeao)
#Resultado:  O grande campeão do torneio é o time Bruxos como Ronaldinho
~~~~

Aponte o provável erro de Romeu na hora de exibir o primeiro colocado de sua lista, para que o seu time Drible da Emoção seja devidamente coroado campeão.
Selecione uma alternativa

    Romeu fez quase tudo corretamente, errando apenas na linha:

    campeao = colocacao[1]

    Apesar dele querer o primeiro colocado de seu torneio, ele deve pedir o primeiro elemento da lista, que é o elemento de índice 0** e não de índice **1.

    Romeu errou ao salvar o resultado em um variaveĺ na linha abaixo:

    campeao = colocacao[1]

    Quando fez isto, acabou alterando a ordem da lista, então quando ele pede para imprimir o campeao no print final, o resultado não vem como ele espera.

    Romeu deveria ter impresso diretamente o resultado no print final, pulando a etapa de criar uma variável campeao. Caso ele tivesse feito assim:

    print(' O grande campeão do torneio é o time ' + colocacao[1])

    Ele obteria o resultado esperado.





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

Romeu fez quase tudo corretamente, errando apenas na linha:

campeao = colocacao[1]

Apesar dele querer o primeiro colocado de seu torneio, ele deve pedir o primeiro elemento da lista, que é o elemento de índice 0** e não de índice **1.

Correto! Vale lembrar que apesar de querermos o primeiro item de uma Lista, temos sempre que lembrar que as listas começam contando do índice 0


- Código corrigido:

~~~~PYTHON
## Restante do código que gera a lista de colocação...
print(colocacao)
campeao = colocacao[0]
print(' O grande campeão do torneio é o time ' + campeao)
~~~~
