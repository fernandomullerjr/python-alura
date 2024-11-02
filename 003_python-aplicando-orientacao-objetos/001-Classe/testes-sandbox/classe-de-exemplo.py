class Cachorro:
    # Método inicializador (construtor)
    def __init__(self, nome, idade):
        # Atributos do objeto (características)
        self.nome = nome
        self.idade = idade
    
    # Método (comportamento)
    def latir(self):
        return f"{self.nome} está latindo: Au au!"

# Instanciando objetos (criando cachorros específicos)
rex = Cachorro("Rex", 3)  # Criando um objeto da classe Cachorro
bob = Cachorro("Bob", 5)  # Outro objeto da mesma classe

# Usando os objetos
print(rex.nome)      # Acessando atributo -> Rex
print(bob.idade)     # Acessando atributo -> 5
print(rex.latir())   # Chamando método -> Rex está latindo: Au au!