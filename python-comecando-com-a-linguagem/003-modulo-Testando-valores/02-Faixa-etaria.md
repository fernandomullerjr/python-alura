
# aula 02 - Faixa Etária

Considere o programa abaixo:

~~~~python
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")
~~~~



Quando o usuário digitar 12, o que será mostrado no console?

Alternativa correta
O programa não irá rodar.


Alternativa correta
Será impresso Você é um adolescente.


Alternativa correta
Nada.


Correto!

Alternativa correta
Será impresso Você é maior de idade.


Alternativa correta
Será impresso Você é uma criança.





Quando o usuário digitar 12, nenhuma condição será satisfeita! Repare que:

12 não é maior que 18 (idade > 18).
12 não é menor que 12 (idade < 12).
12 não é maior que 12 (idade > 12).
É preciso testar a igualdade através do ==.

Saiba também, que além do == (igualdade), > (maior) e < (menor), também temos >= (maior ou igual), <= (menor ou igual) e != (diferente).

Seguem todas as operadores de comparação:

< - menor que
> - maior que
<= - menor ou igual a
>= - maior ou igual a
== - igual a
!= - diferente de