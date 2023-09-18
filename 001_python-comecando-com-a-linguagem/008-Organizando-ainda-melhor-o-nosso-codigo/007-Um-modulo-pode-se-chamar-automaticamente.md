
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 8 - aula 07 Um módulo pode se chamar automaticamente?"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 07 Um módulo pode se chamar automaticamente?

Kellen criou o seguinte módulo no arquivo a.py:

~~~~python
# arquivo a.py
def executa():
    print("Executando a")
~~~~

Aprendemos a importar um módulo, inclusive a chamar uma função específica desse módulo. No entanto, Kellen deseja usar a.py independente de outros módulos, ou seja, quer ser capaz de chamá-lo através do console, como:

~~~~python
python a.py
~~~~


Qual das opções abaixo possui a modificação correta de a.py para que seja possível chamar o arquivo diretamente do terminal?

Selecione uma alternativa

def executa():
    print("Executando a")

if(__name__ = "__main__"):
    executa()

def executa():
    print("Executando a")

if(__name__ == "_main_"):
    executa()

def executa():
    print("Executando a")

if(__name__ == "__main__"):
    executa()

def executa():
    print("Executando a")

if(_name_ == "__main__"):
    executa()







# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

~~~~python
def executa():
    print("Executando a")

if(__name__ == "__main__"):
    executa()
~~~~


Correto!

