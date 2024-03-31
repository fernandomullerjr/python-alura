
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 04 Forca com teste de erros alternativo"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 04 Forca com teste de erros alternativo

No nosso jogo da forca imagine que você inicialize a variável erros com 6 tentativas:

erros = 6

O que você precisa mudar no código para manter o jogador sendo enforcado após 6 tentativas frustradas?
Selecione 2 alternativas

    Nada.

    Apenas decrementar a variável erros com:

    erros = erros - 1

    Apenas mudar o teste da variável enforcou para:

    enforcou =  erros == 12

    Decrementar a variável erros com:

    erros = erros - 1

    e mudar o teste da variável enforcou para:

    enforcou = erros == 0




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

Apenas mudar o teste da variável enforcou para:

enforcou =  erros == 12

    Correto! Se a variável erros começou com 6, pra manter a quantidade de tentativas em 6, precisamos mudar o teste da variável enforcou para 6 + 6, mas seria nada elegante e legível, certo?
    Alternativa correta



ou



Decrementar a variável erros com:

erros = erros - 1

e mudar o teste da variável enforcou para:

enforcou = erros == 0

    Correto! Podemos decrementarmos a variável erros para que ela chegue até zero e com isso o teste da variável enforcou precisará mudar para refletir isso.
