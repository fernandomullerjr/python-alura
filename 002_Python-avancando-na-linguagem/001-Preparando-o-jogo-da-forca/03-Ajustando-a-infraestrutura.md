
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 1 - aula 03 Ajustando a infraestrutura"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status





# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  03 Ajustando a infraestrutura

## Transcrição
Esse vídeo é para os alunos que não fizeram o primeiro treinamento de Python 3.

Continuaremos o projeto do curso anterior, que você pode baixar AQUI.

A seguir, veremos o que é preciso ter e configurar na sua máquina, para prosseguir com o treinamento sem transtornos.

Baixando e instalando o Python 3
O primeiro passo é instalar o Python 3, acessando o site do Python: https://www.python.org/. Na sessão de Downloads, o instalador específico para a sua plataforma será automaticamente disponibilizado, portanto é só baixar e instalar o Python 3, na sua versão mais atual.

Baixando e instalando o PyCharm
PyCharm é uma IDE voltada exclusivamente para o Python, e é ela que iremos utilizar aqui no treinamento. A sua instalação é bem simples, basta acessar a sessão de Download do site oficial, baixar e instalar a versão Community da IDE, já que a versão Professional é paga.

Conhecendo o PyCharm e criando o primeiro projeto
Após instalar o PyCharm e abri-lo, crie um projeto, clicando em Create New Project. Na tela que irá se abrir, é perguntada a localização do projeto e a versão do Python. Crie o projeto jogos, dentro da pasta PycharmProjects mesmo, e atente-se à versão do Python (caso você tenha mais de uma versão instalada), ela deve ser a versão 3.

O projeto será exibido no lado esquerdo e, para criar um arquivo Python nele, basta clicar com o botão direito do mouse em cima dele e selecionar New -> Python File. Mas não criaremos arquivos novos, já que há os arquivos do projeto feito no treinamento anterior, que podem ser baixados aqui.

Ao extrair o zip, uma pasta será criada, basta selecionar os três arquivos que estão dentro dela (adivinhacao.py, forca.py e jogos.py) e arrastar para dentro da pasta jogos, diretório do projeto que acabou de ser criado.

O arquivo que implementaremos nesse treinamento é o forca.py. Para executá-lo, podemos abri-lo, clicando com o botão direito do mouse dentro dele, e selecionando Run 'forca'. O console do PyCharm é aberto e exibe a saída do nosso programa.

Com o Python 3 e o PyCharm instalados, e o projeto na sua máquina, podemos dar prosseguimento ao treinamento :)