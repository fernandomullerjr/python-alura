
# 03 - Faixa Etária - Variáveis

Considere o programa abaixo:

~~~~python
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12
~~~~




Quando o usuário digitar 15, o valor das variáveis maior_idade, crianca e adolescente será, respectivamente:

True, True, False

Alternativa correta
False, False, True
Correto!

True, False, False
False, False, False
0, 0, 1




Para a idade = 15:

maior_idade: 15 > 18 (False)
crianca: 15 < 12 (False)
adolescente: 15 > 12 (True)