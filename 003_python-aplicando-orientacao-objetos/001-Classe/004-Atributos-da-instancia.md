
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 1 - Aula 04 Atributos de instância."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04 Atributos de instância

## Transcrição

Guilherme: Nós temos agora o desafio de definir o nome, a categoria e o estado ativo para os restaurantes que temos. Começaremos pelo restaurante_praca. Para definirmos um nome para ele, abaixo da linha em branco abaixo dele escreveremos restaurante_praca..

~~~~python
# código omitido

restaurante_praca = Restaurante()
restaurante_praca.
restaurante_pizza = Restaurante()

# código omitido
~~~~

Ao escrevermos o ponto (.) depois de restaurante_praca, acessamos esse objeto e, dessa forma, ele abre um menu suspenso com várias opções, como ativo, categoria e nome. Selecionaremos a opção nome e atribuiremos o nome 'Praça', como string: restaurante_praca.nome = 'Praça'. E qual será a categoria, Lais?

Lais: A categoria dele será "Gourmet".

Guilherme: Então escrevemos restaurante_praca.categoria = 'Gourmet'. Finalmente, o Restaurante Praça terá com o atributo ativo definido como Falso e manteremos assim, portanto, não precisaremos alterar esse valor. Vamos alterar somente a última linha para visualizarmos apenas o Restaurante Praça, deixando como print(restaurante_praca).

~~~~python
# código omitido

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
~~~~

No Terminal, quando executamos o python modelos/restaurante.py, ainda não conseguimos ver os valores que criamos, apenas o endereço de memória desse objeto. Existe uma maneira de conseguirmos visualizar, pelo menos, algumas informações. O que a classe Restaurante tem como propriedades, atributos e métodos?

Lais: Temos uma função que podemos utilizar, que é a função dir(). Então, ao invés de passarmos o nome da classe no print(), passamos o dir(restaurante_praca), com o nome do objeto, restaurante_praca, como atributos. Vamos descobrir o que o Terminal retorna.

~~~~python
# código omitido

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(dir(restaurante_praca))
~~~~

Guilherme: Ao limparmos o Terminal e executarmos o comando python modelos/restaurante.py novamente, obtemos várias informações dessa vez, entre elas "'ativo', 'categoria' e 'nome', no final da lista, que são os últimos que criamos.

    Terminal:

    PS C:\Users\nome\Desktop\oo-sabor-express> python modelos/restaurante.py

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ativo', 'categoria', 'nome']

Mas esse objeto dir() já possui uma série de informações, como __classe__. Sempre que temos esse __ (underline, underline), significa que é um método especial que toda classe em Python possui. Quando faz sentido olhar para o dir()? Principalmente quando se trata de uma classe que não conhecemos.

Quando queremos entender os métodos e como ela funciona, conseguimos visualizar através do retorno do dir(). No entanto, existe outra função que exibirá um dicionário com os atributos dessa classe, similar ao que vimos no nosso curso onde trabalhamos com várias funções.

Portanto, o dir() mostrará tudo: os atributos, métodos e propriedades de um objeto. Quando o substituímos por vars(), queremos um dicionário desses atributos e métodos. Vamos fazer um teste.

    Código:

~~~~python
# código omitido

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
~~~~

Terminal:

PS C:\Users\nome\Desktop\oo-sabor-express> python modelos/restaurante.py
{'nome': 'Praça', 'categoria': 'Gourmet'}

Ao executarmos dessa vez, recebemos no formato que tínhamos na função, com o 'nome': 'Praça', 'categoria': 'Gourmet'. Porém o 'ativo' não apareceu.

O ativo está definido para esse restaurante, tanto que, se executarmos o print(restaurante_praca.ativo) e, no Terminal, rodarmos o python modelos/restaurante.py, recebemos o retorno False (Falso). Portanto, o ativo está armazenado, mas ele não listou esse valor para nós.

Temos apenas um pequeno problema. Entendemos como criar uma classe e como definir os valores dessa classe através do ponto (.). A vantagem da classe é que todo objeto restaurante terá um nome e uma categoria, que são os atributos da classe. Mas seria ainda melhor se criássemos a classe e já definíssemos o nome e a categoria do restaurante.

Portanto, é melhor que, ao criarmos uma nova classe, já temos esses métodos. Faremos isso na sequência.




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04 Atributos de instância



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESUMO

- Função dir
interessante usar para identificar classes que não conhecemos
Quando faz sentido olhar para o dir()? Principalmente quando se trata de uma classe que não conhecemos.
Quando queremos entender os métodos e como ela funciona, conseguimos visualizar através do retorno do dir(). No entanto, existe outra função que exibirá um dicionário com os atributos dessa classe, similar ao que vimos no nosso curso onde trabalhamos com várias funções.
Portanto, o dir() mostrará tudo: os atributos, métodos e propriedades de um objeto. 
Quando o substituímos por vars(), queremos um dicionário desses atributos e métodos. 

- Métodos especiais começam com 2 underline __
Sempre que temos esse __ (underline, underline), significa que é um método especial que toda classe em Python possui.