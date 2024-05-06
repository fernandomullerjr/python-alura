
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 6 - 01 Escrevendo em um arquivo."
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Escrevendo em um arquivo

## Transcrição

Uma funcionalidade que ainda nos atrapalha no nosso jogo é a palavra secreta, que atualmente está fixa. Se queremos que a palavra seja diferente, devemos modificá-la no código.

A nossa ideia é ler palavras de um arquivo de texto, e dentre elas escolhemos uma palavra aleatoriamente, que será a palavra secreta do jogo
Escrita de um arquivo

Para abrir um arquivo, o Python possui a função built-in open. Ela recebe dois parâmetros: o primeiro é o nome do arquivo a ser aberto, e o segundo parâmetro é o modo que queremos trabalhar com esse arquivo, se queremos ler ou escrever. O modo é passado através de uma string: "w" para escrita e "r" para leitura.

No nosso jogo, faremos a leitura de um arquivo, mas vamos ver antes no terminal do Python 3 como funciona a escrita:

>>> arquivo = open("palavras.txt", "w")

Vale lembrar que o w sobrescreve o arquivo, se o mesmo existir. Se só quisermos adicionar conteúdo ao arquivo, utilizamos o a.

Agora que temos o arquivo, como escrevemos nele? Basta chamar no arquivo a função write, passando para ela o que queremos escrever no arquivo:

>>> arquivo.write("banana")
6
>>> arquivo.write("melancia")
8

O retorno dessa função é o número de caracteres que adicionamos no arquivo.
Fechando um arquivo

Quando estamos trabalhando com arquivos, devemos nos preocupar em fechá-lo. Assim como abrimos um arquivo, devemos fechá-los, chamando a função close:

>>> arquivo.close()

Após isso, podemos verificar o conteúdo do arquivo, ele foi criado na mesma pasta em que o comando para a abrir o console do Python 3 foi executado. Ao verificar o seu conteúdo, vemos:

bananamelancia

As palavras foram escritas em uma mesma linha. Mas como escrever em uma nova linha?
Escrevendo palavras em novas linhas

A primeira coisa que devemos fazer é abrir o arquivo novamente, dessa vez utilizando o a, de append:

>>> arquivo = open("palavras.txt", "a")

Podemos escrever novamente no arquivo, mas dessa vez com a preocupação de criar uma nova linha após o que vamos escrever. Para representar uma nova linha em código, adicionamos o \n ao final do que queremos escrever:

>>> arquivo.write("morango\n")
8
>>> arquivo.write("manga\n")
6

Ao fechar o arquivo e verificar novamente o seu conteúdo, vemos:

bananamelanciamorango
manga

A palavra morango ainda ficou na mesma linha, mas como especificamos na sua adição que após a palavra deverá ter uma quebra de linha, a palavra manga foi adicionada abaixo, em uma nova linha.

Por fim, vamos mover esse arquivo para dentro do nosso projeto, e ajeitar as suas palavras, quebrando as linhas. Ele ficará assim:

banana
melancia
morango
manga







# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 01 Escrevendo em um arquivo

- Para abrir arquivos, usamos uma função built-in chamada "open"
<https://docs.python.org/3.8/library/functions.html#open>

 open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

The available modes are:

~~~~markdown
'r'
	

open for reading (default)

'w'
	

open for writing, truncating the file first

'x'
	

open for exclusive creation, failing if the file already exists

'a'
	

open for writing, appending to the end of the file if it exists

'b'
	

binary mode

't'
	

text mode (default)

'+'
	

open for updating (reading and writing)
~~~~



open("palavras.txt", "w")

arquivo = open("palavras.txt", "w")


fernando@debian10x64:~$ python3
Python 3.8.3 (default, Jun  4 2023, 19:15:23)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>> arquivo = open("palavras.txt", "w")
>>>
>>> arquivo
<_io.TextIOWrapper name='palavras.txt' mode='w' encoding='UTF-8'>
>>>



arquivo.write("banana")

>>>
>>> arquivo.write("banana")
6
>>>
>>>




arquivo.write("melancia")

arquivo.close()

>>> arquivo.write("melancia")
8
>>>
>>>
>>> arquivo.close()
>>>





- Verificando o arquivo criado:

~~~~bash
fernando@debian10x64:~$ ls
arquivo-de-teste.txt  cursos     event-simulator.yaml         kubectl  nrdiag-filelist.txt  output.txt    python             setar-hora.sh        terraform_1.1.5_linux_amd64.zip  testes             work
aws                   Desktop    go                           laravel  nrdiag-output.json   palavras.txt  Python-3.8.3       snap                 terraform.tfstate                tmp.json
awscliv2.zip          Documents  go1.12.7.linux-amd64.tar.gz  Music    nrdiag-output.zip    Pictures      Python-3.8.3.tgz   static-busybox.yaml  teste1.txt                       Videos
bin                   Downloads  index.html                   nrdiag   out-3.txt            Public        rascunho-teste.md  Templates            teste-kubernetes-aula9           webapp-green.yaml
fernando@debian10x64:~$
fernando@debian10x64:~$ cat palavras.txt
bananamelancia
fernando@debian10x64:~$
~~~~

Porém as palavras ficaram tudo juntas!

Porém as palavras ficaram tudo juntas!






- Vamos usar o append agora, usando o parametro "a"

arquivo = open("palavras.txt", "a")
arquivo.write("morango\n")
arquivo.write("maça\n")
arquivo.close()

>>>
>>> arquivo = open("palavras.txt", "a")
>>>
>>> arquivo.write("morango\n")
8
>>> arquivo.write("maça\n")
5
>>> arquivo.close()
>>>


- Validando

~~~~bash
fernando@debian10x64:~$ cat palavras.txt
bananamelanciamorango
maça
fernando@debian10x64:~$
fernando@debian10x64:~$
~~~~

Palavra "morango" foi adicionada colada nas demais
A palavra "maça" foi adicionada corretamente



- Movimentando para outra pasta o arquivo "palavras.txt"



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESUMO

