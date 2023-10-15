

# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 1 - aula 07 Quantos erros tem..."
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status



# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 07 Quantos erros tem...

Gustavo decidiu praticar o que aprendeu no vídeo deste capítulo e escreveu o seguinte código. Leia-o atentamente:

~~~~python
def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra_secreta = "banana"
    enforcou = false
    acertou = false

    while(Not enforcou and Not acertou):
        print("jogando...")

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()
~~~~

No entanto, seu código não funcionou. Sem executar o programa, apenas olhando o código anterior, podemos afirmar que a quantidade de erros cometidos é:

Selecione uma alternativa

3


4


2

