
# Aula 06 - Comparação estranha

- Romeu fez uma simples comparação entre números, mas que não funciona. Segue o código:

~~~~python
numero1 = 10
numero2 = 10
if(numero1 = numero2):
    print("São números iguais")
~~~~

Consegue descobrir onde Romeu errou? Pense bem para em seguida clicar em Ver Opinião do Instrutor e ver a resposta do instrutor.



# Opinião do instrutor

O problema é que foi usado um = para realizar a comparação. Quando usamos apenas um =, estamos atribuindo um valor à variável. Para compararmos valores ou variáveis, usamos o ==. Sendo assim, para o código do Romeu funcionar:

~~~~python
numero1 = 10
numero2 = 10
if(numero1 == numero2):
    print("São números iguais")
~~~~
