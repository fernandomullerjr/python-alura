
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 1 - Aula 03 Classes."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Classes

## Transcrição

Lais: Até o momento, estávamos desenvolvendo de um segmento do back-end de um aplicativo chamado Sabor Express, que está, atualmente, realizando o cadastro de restaurantes. Estávamos utilizando funções, métodos e estruturas sequenciais em nosso código. Agora, vamos adentrar um paradigma que utilizamos bastante, o orientado a objetos.

Guilherme: Esse paradigma de orientação a objetos é muito usado no mercado e nos ajudará a garantir um pouco mais como conseguimos lidar com os dados na nossa aplicação. No primeiro curso que desenvolvemos, usamos bastante função. Agora, vamos transportar para um conceito que vamos chamar de objeto, muito conhecido em Python.

Vamos começar o Sabor Express agora com outro paradigma de programação. Vamos criar um arquivo do desde o início, então, no Desktop (Área de tarefas), clicarei com o botão direito do mouse em um espaço vazio e vou selecionar "Nova pasta" no menu. Chamaremos a paste de "oo-sabor-express", e nela manteremos todo o código relacionado ao que desenvolveremos nesse curso.

Agora abriremos o Visual Studio Code e arrastaremos a pasta "oo-sabor-express" para dentro do programa para começarmos a desenvolver. Começaremos criando uma pasta onde manteremos todas as nossas classes.

Para isso, na aba Explorador, que fica no lado esquerdo do VS Code, clicaremos no botão de "Nova Pasta", na parte superior direita da aba. Nomearemos essa pasta como "modelos". Com a pasta "modelos" selecionada, clicaremos no botão "Novo arquivo", que chamaremos de restaurante.py, onde criaremos um modelo de um restaurante. É nesse arquivo que manteremos a nossa classe em Python.

Antes de começarmos a criar uma classe, vamos pensar o que é uma classe em Python. Vamos começar pensando o que é um restaurante na nossa aplicação. Quais são as características que esse restaurante tem?

Lais: Até agora temos o nome do restaurante, a categoria e se ele está ou não ativo, ou seja, o estado daquele restaurante no momento.

    Arquivo restaurante.py.

nome
categoria
ativo

Guilherme: No projeto anterior, criamos dicionários com essas informações, ou seja, cada dicionário tinha "nome, categoria e ativo". Mas tem um problema, se quiséssemos criar um novo valor em um dos restaurantes, por exemplo, a quantidade de likes, conseguiríamos fazer isso, mas os outros restaurantes criados não teriam esse valor novo.

A ideia é que, quando falarmos em classe, estamos pensando em uma abstração do mundo real: em um código onde conseguiremos juntar tipos diferentes. Por exemplo, sabemos que o nome é uma string, então podemos escrever como nome = '', porque pode ser qualquer nome de restaurante, assim como a categoria também é uma string, ou seja, categoria = ''. O ativo era um tipo booleano, e falávamos que todo restaurante, quando criamos, queremos que ele seja falso, então ativo = False.

~~~~python
nome = ''
categoria = ''
ativo = False
~~~~

Mas como conseguimos transformar essas três informações para que eles estejam em qualquer restaurante que formos criar? Para isso, usamos uma palavra reservada do Python, chamada class. Sempre que escrevemos class, estamos criando uma classe no Python, e podemos dar um nome para essa classe.

No caso, essa classe representará um restaurante, então é interessante nomeá-la como Restaurante:, adicionando os dois pontos depois do nome. Em seguida, selecionamos o nome, a categoria e o ativo, e pressionamos a "Barra de Espaço" quatro vezes.

~~~~python
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
~~~~

Temos uma classe no Python de um jeito muito simples. Essa classe tem os atributos nome, que será uma string, categoria, que também será uma string, e ativo que será False (Falso). Agora, como criamos um restaurante com base nisso?

Quando temos uma classe e queremos criar um restaurante novo, falamos que estamos instanciando, ou criando, um objeto, sendo que um objeto é a instância de uma classe. Então, para criarmos um restaurante novo, primeiro criaremos uma variável. Por exemplo, criaremos a variável de restaurante_praca, que será igual ao objeto Restaurante().

~~~~python
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
~~~~

Criamos um Restaurante Praça. Podemos criar outro restaurante, pressionando "Enter" e, na linha abaixo, escrevendo restaurante_pizza = Restaurante().

~~~~python
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()
~~~~

De agora em diante, qualquer restaurante que quisermos criar, teremos o nome de uma variável, onde vamos armazená-lo, e informaremos que ele será do tipo, Restaurante(). Para visualizarmos esses restaurantes da forma que aparecem no programa, adicionaremos esses dois restaurantes em uma lista chamada restaurantes. Também pediremos um print() nos nossos restaurantes para vê-los.

~~~~python
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)
~~~~

Vamos abrir o Terminal para vermos como ficou. Com o Terminal aberto, precisei executar o comando quit(), porque abri o terminal integrado sem querer. Porém, para vermos nossos restaurantes, escreveremos o comando python seguido do endereço do nosso código no VS Code, ou seja, python modelos/restaurante.py. Quando pressionamos "Enter", aparecem duas informações um pouco estranhas, mas não é um erro.

    [<__main__.Restaurante object at 0x...>, <__main__.Restaurante object at 0x...>]

Apareceu essa lista onde temos __main__.Restaurante object at seguido de um valor estranho e, depois de uma vírgula, uma informação parecida, mas com outro valor. Por que o Python está mostrando esses valores para nós?

Lais: Ele não está mostrando tantas informações. A única coisa que sabemos é que a informação que ele exibe é um objeto da classe Restaurante. Ele não mostra mais informações ou detalhes, apenas o local da memória onde está armazenado aquele objeto.

Guilherme: Ou seja, não conseguimos ver as informações que queríamos, por exemplo, como definimos o nome ou a categoria de um restaurante que criamos. Então, criamos a classe contendo os atributos que queríamos para ela.

Sempre que pensarmos em uma classe, temos que pensar quais são os atributos, ou seja, as características dessa entidade que queremos criar. Vamos supor que queremos criar uma entidade chamada pessoa, então precisamos pensar nas características de uma pessoa que queremos dentro de um sistema, como o RG e o CPF.

Se quisermos criar uma classe de carros, podemos pensar como características a quantidade de rodas e a cor. Reparem que toda essa abstração que trazemos do mundo real e colocamos no programa, definirá as nossas classes posteriormente.

Depois que criamos a nossa classe, queremos usar essa classe. Para isso, criamos uma variável e passamos o nome da classe, abrindo e fechando parênteses após o nome, ou seja, NomeDaClasse(). Dessa forma, criamos um objeto dessa classe.

Tanto que, quando pedimos para mostrar um print() dos restaurantes, as informações apareceram como restaurante object, um objeto de restaurante armazenado no endereço que aparece depois dele. Esse objeto está na memória, mas não conseguimos ver os outros dados, e é isso que vamos ver no próximo vídeo.






# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 03 Classes

Vamos começar o Sabor Express agora com outro paradigma de programação. Vamos criar um arquivo do desde o início, então, no Desktop (Área de tarefas), clicarei com o botão direito do mouse em um espaço vazio e vou selecionar "Nova pasta" no menu. Chamaremos a paste de "oo-sabor-express", e nela manteremos todo o código relacionado ao que desenvolveremos nesse curso.


Agora abriremos o Visual Studio Code e arrastaremos a pasta "oo-sabor-express" para dentro do programa para começarmos a desenvolver. Começaremos criando uma pasta onde manteremos todas as nossas classes.

Para isso, na aba Explorador, que fica no lado esquerdo do VS Code, clicaremos no botão de "Nova Pasta", na parte superior direita da aba. Nomearemos essa pasta como "modelos". Com a pasta "modelos" selecionada, clicaremos no botão "Novo arquivo", que chamaremos de restaurante.py, onde criaremos um modelo de um restaurante. É nesse arquivo que manteremos a nossa classe em Python.

- Criando pasta
oo-sabor-express
modelos




Antes de começarmos a criar uma classe, vamos pensar o que é uma classe em Python. Vamos começar pensando o que é um restaurante na nossa aplicação. Quais são as características que esse restaurante tem?

Lais: Até agora temos o nome do restaurante, a categoria e se ele está ou não ativo, ou seja, o estado daquele restaurante no momento.

    Arquivo restaurante.py.

- Criando arquivo
restaurante.py




- Ao executar o código
ele retorna somente a posição do objeto

>
> python3 /home/fernando/cursos/python/python-alura/003_python-aplicando-orientacao-objetos/001-Classe/oo-sabor-express/modelos/restaurante.py
[<__main__.Restaurante object at 0x7f776d47db50>, <__main__.Restaurante object at 0x7f776d47db80>]



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESUMO

- Classe é algo que tem atributos.