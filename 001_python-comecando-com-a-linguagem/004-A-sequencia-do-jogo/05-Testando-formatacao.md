
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 4 - aula 05 - Testando formatação."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 - Testando formatação
Veja a declaração das 4 variáveis:

~~~~python
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017
~~~~


Pedro precisa criar a seguinte string:
"Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"

Qual é a formatação correta para produzir a string acima?




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# Resposta - formulada por mim


~~~~python
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017
print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))
~~~~


- Testando
python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/05-resposta-formatacao.py

~~~~bash
fernando@debian10x64:~/cursos/python/python-alura$ python3 /home/fernando/cursos/python/python-alura/python-comecando-com-a-linguagem/004-A-sequencia-do-jogo/05-resposta-formatacao.py
Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28
fernando@debian10x64:~/cursos/python/python-alura$
~~~~