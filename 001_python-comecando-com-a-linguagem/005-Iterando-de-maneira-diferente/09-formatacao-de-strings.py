
# Exemplo de format mais comum
print("Tentativa {} de {}".format(1, 3))


## Formatação de floats
print("R$ {:.2f}".format(1.59))
# R$ 1.59

# Preenchendo no começo com zeros:
print("R$ {:07.2f}".format(1.5))
# R$ 0001.50


## INTEIROS
# Conseguimos formatar números inteiros também, não só números flutuantes. Para números inteiros, passamos a letra d:
print("R$ {:07d}".format(4))
# R$ 0000004