

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 6 - aula 06 O grande sorteio."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 06 O grande sorteio

PRÓXIMA ATIVIDADE

O professor Flávio tem o costume de sortear um livro da Casa do Código ao final de todos os seus cursos para os seus 3 melhores alunos. Desta vez, os três melhores alunos foram:

Paulo
Juliana
Tamires
Para realizar o sorteio, foi utilizado o seguinte script em Python para determinar o vencedor:

~~~~python
import random

sorteado = random.randrange(0,4)

print(sorteado)

if sorteado == 1:
    print( "Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires")
~~~~

Quando executado o script foi anunciado que a Tamires era a vencedora, porém Paulo após conferir o código exclamou que o sorteio não era justo e que ele e a Juliana tinham menos de chances de ganhar!

De acordo com seus conhecimentos de Python, analise o código acima e avalie se o sorteio foi justo ou não e dê uma justificativa para tal!

Selecione uma alternativa

O sorteio foi justo, afinal os possíveis números retornados são 0, 1 e 2, e cada uma das pessoas está associada a um número.


O sorteio foi justo, afinal os possíveis números retornados são 1, 2 e 3 e cada uma das pessoas está associada a um número.


O sorteio foi injusto, afinal os possíveis números retornados são 0, 1, 2 e 3 , e como o Paulo e a Juliana estão associadas a apenas um número cada sobram ainda outros dois para Tamires poder ganhar.










## RESPOSTA CORRETA

O sorteio foi injusto, afinal os possíveis números retornados são 0, 1, 2 e 3 , e como o Paulo e a Juliana estão associadas a apenas um número cada sobram ainda outros dois para Tamires poder ganhar.


## EXCPLICAÇÃO DETALHADA

A verdade é que o sorteio não foi justo pois a Tamires realmente tinha mais chance de ganhar! A função random.randrange nos retorna um número no intervalo especificado. Nesse exemplo, temos como saída os possíveis valores 0, 1, 2 e 3. Como o Paulo está associado ao valor 1 e a Juliana ao valor 2, sobram mais dois possíveis valores para a Tamires poder ganhar ( 0 ou 3 ).

Quando estamos trabalhando com números aleatórios, é importante observar bem o resultado das nossas funções e como se comporta nosso código, além de entender sobre aleatoriedade. Neste caso o sorteio era apenas de um livro, porém em sistemas de verdade pode ser que o efeito de um sorteio indesejado possa beneficiar acidentalmente uma certa pessoa ou até mesmo causar prejuízos à sua empresa.