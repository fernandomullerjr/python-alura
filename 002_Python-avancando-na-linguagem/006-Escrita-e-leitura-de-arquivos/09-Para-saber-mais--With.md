
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 6 - 09 Para saber mais: with."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  09 Para saber mais: with

Já falamos da importância de fechar o arquivo, certo? Veja o código abaixo que justamente usa a função close :

~~~~python
logo = open('palavras.txt', 'r')
data = logo.read()
logo.close()
~~~~

Agora imagine que dê algum problema na hora da leitura quando chamarmos a função read(). Será que mesmo com erro o arquivo será fechado?

Se for algum erro grave, o programa pode parar a execução sem ter fechado o arquivo! Isso seria muito ruim ...

Para evitar esse tipo de situação, o Python criou uma sintaxe especial para abertura de arquivo. Veja só:

~~~~python
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
~~~~

Repare que o with usa a função open. Repare também que não fechamos o arquivo. Isso não é mais necessário pois o Python vai cuidar disso e, mesmo com erro, garantirá o fechamento do arquivo! Muito melhor não?