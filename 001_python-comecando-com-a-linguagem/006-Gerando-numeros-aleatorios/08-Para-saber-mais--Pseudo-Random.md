

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 6 - aula 08 Para saber mais: Pseudo-Random."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status




# ###################################################################################################################################################################
# ###################################################################################################################################################################
#  08 Para saber mais: Pseudo-Random

Pseudo-Random?
Aparentemente a geração de números aleatórios funcionou muito bem. Cada vez que chamamos o random.random() ou random.randrange(..), foi gerado um outro número.

No entanto, computadores têm os seus problemas com aleatoriedade, pois são sistemas determinísticos. Em outras palavras, o nosso Python é previsível e na verdade não sabe criar números verdadeiramente aleatórios. Por isso se chama Pseudo-Random!

Por que funcionou então?
random é um função que, dada a mesma entrada, gerará o mesmo número. O truque é oferecer sempre uma entrada diferente para ter números diferentes e exatamente isso que está acontecendo por baixo dos panos.

Essa entrada também é chamada de seed (semente, em português). Entre as chamadas da função random, sempre é utilizado um novo seed. Por padrão o Python usa a hora (os milissegundos) como semente, mas nada nos impede de definir o mesmo seed antecipadamente. Para isso, existe a função seed!

Usando seed
Por exemplo, no jogo usamos a função randrange para gerar um número aleatório entre 1 e 100. Antes do randrange podemos chamar o seed para definir a entrada:

>>> random.seed(100)
>>> random.randrange(1, 101)
19
Repare que foi gerado 19 e se usarmos o mesmo seed será gerado o mesmo número:

>>> random.seed(100)
>>> random.randrange(1, 101)
19
Repare que a biblioteca random é bem previsível e por isso se chama pseudo-random!




- Testando

~~~~bash

fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/006-Gerando-numeros-aleatorios/08-random-com-seed.py
19
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$
fernando@debian10x64:~$ python3 /home/fernando/cursos/python/python-alura/001_python-comecando-com-a-linguagem/006-Gerando-numeros-aleatorios/08-random-com-seed.py
19
fernando@debian10x64:~$ date
Sat 26 Aug 2023 09:32:48 PM -03
fernando@debian10x64:~$

~~~~