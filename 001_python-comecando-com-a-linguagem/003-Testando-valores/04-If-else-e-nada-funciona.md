
# ################################################################################################################################################################
# ################################################################################################################################################################
# ################################################################################################################################################################
# 04 - If..else. e nada funciona!

Henrique, mesmo dando os primeiros passos com a linguagem Python, decidiu criar um sistema de identificação de usuários. É claro que em uma aplicação real é necessário acessar o banco de dados, entre outras coisas, mas usando o que ele já aprendeu, ele conseguiu algo parecido. Esse é o código do aluno:

~~~~python
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
else(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
else(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")
~~~~

A ideia de Henrique é simples, porém não muito eficiente. Ele quer aceitar apenas os usuários Flávio, Douglas e Nico. No entanto, seu código não funciona!

Consegue identificar a razão? Quebre a cabeça um pouquinho.





# ################################################################################################################################################################
# ################################################################################################################################################################
# ################################################################################################################################################################
# TSHOOT


- Teste1, não ficou ok.
imprime "Usuário não identificado!" para todos os casos

~~~~python
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
else:
    if (usuario == "Douglas"):
        print("Seja bem-vindo Douglas!")
    elif (usuario == "Nico"):
        print("Seja bem-vindo Nico")
    print("Usuário não identificado!")
~~~~




- Teste2
está OK agora
imprime a mensagem "Seja bem-vindo usuário" quando o usuário existe
imprime a mensagem "Usuário não identificado!" somente quando o usuário não existe mesmo.
material de apoio: <https://www.devmedia.com.br/python-estrutura-condicional-if-else/38217>

- Código corrigido:

~~~~python
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif (usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif (usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")
~~~~

- Validando:

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/003-modulo-Testando-valores/04-If-else-e-nada-funciona-Versao-corrigida.py
Informe o usuário do sistema!fernando
Usuário não identificado!
fernando@debian10x64:~/cursos/python/python-alura$
fernando@debian10x64:~/cursos/python/python-alura$
fernando@debian10x64:~/cursos/python/python-alura$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/003-modulo-Testando-valores/04-If-else-e-nada-funciona-Versao-corrigida.py
Informe o usuário do sistema!Nico
Seja bem-vindo Nico
fernando@debian10x64:~/cursos/python/python-alura$
~~~~



# ################################################################################################################################################################
# ################################################################################################################################################################
# ################################################################################################################################################################
# Opinião do instrutor

O problema é que a instrução else não aceita receber uma condição. Nesse caso, para resolver o problema do código, precisamos trocar para a instrução elif:

~~~~python
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")
~~~~

Veja que deixamos apenas um else que não recebe qualquer condição. Também tem que ser assim, porque se o usuário identificado não for nenhum dos que listamos, imprimimos na tela "Usuário não identificado".