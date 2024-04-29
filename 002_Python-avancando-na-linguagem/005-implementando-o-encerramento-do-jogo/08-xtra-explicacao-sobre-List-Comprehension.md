


porque neste código o upper vem primeiro que o for? Como funciona?

~~~~python
frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]
~~~~


ChatGPT

Nesse código, a expressão [fruta.upper() for fruta in frutas] é uma compreensão de lista em Python. Ela cria uma nova lista onde cada elemento é o resultado da chamada do método upper() em cada elemento da lista frutas.

A estrutura básica de uma compreensão de lista é: [expressão for item in iterável].

Então, o que está acontecendo aqui é o seguinte:

    for fruta in frutas: Isso itera sobre cada elemento na lista frutas, e em cada iteração, fruta recebe um elemento da lista.

    fruta.upper(): Isso aplica o método upper() a cada elemento fruta. O método upper() retorna uma versão em maiúsculas da string.

    [...]: Isso cria uma nova lista contendo os resultados da expressão fruta.upper() para cada elemento fruta na lista frutas.

Portanto, a ordem em que está escrito, com upper() antes de for, é o padrão em compreensões de lista em Python. Isso ocorre porque você está especificando o que deseja fazer com cada elemento antes de definir de onde esses elementos vêm.