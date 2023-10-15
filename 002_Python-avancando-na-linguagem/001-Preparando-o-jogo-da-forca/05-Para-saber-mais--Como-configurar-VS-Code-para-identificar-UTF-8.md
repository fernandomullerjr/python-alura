
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Modulo 1 - aula 03 Ajustando a infraestrutura"
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git push
git status





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# 05 Para saber mais: como configurar o VS Code para identificar UTF-8

PRÓXIMA ATIVIDADE

Ao trabalhar com caracteres especiais ou acentuação em seus projetos, você pode ter notado como é importante que o seu editor de código seja capaz de identificar o UTF-8.

Afinal, o UTF-8 é um formato de codificação que permite que caracteres especiais e acentos sejam exibidos corretamente ao digitar no editor de códigos.

O Visual Studio Code é um dos editores de código mais populares atualmente e pode ser facilmente configurado para identificar o UTF-8. Caso você opte por utilizá-lo durante o curso, aqui estão alguns passos simples que você pode seguir para configurar o Visual Studio Code corretamente:

1 - Abra o Visual Studio Code e clique em "File" (Arquivo) na barra de menu superior; 2 - Selecione "Preferences" (Preferências) e depois "Settings" (Configurações); 3 - Na barra de pesquisa superior, digite "files.encoding"; 4 - Encontre a opção "Files: Encoding" na lista de resultados e selecione "UTF-8" na lista suspensa; 5 - Salve suas configurações e feche a janela de configurações.

alt text: imagem de uma janela do VS Code, nela a seta do mouse clica em arquivo, uma lista é aberta e nela a opção preferências é selecionada, depois a opção “Configurações” é selecionada, uma nova aba é aberta e então no campo de busca da nova aba é digitado o texto file.encoding, a opção Files: Encoding é aberta com uma lista de opções,e nela a opção UTF-8 é selecionada.

Pronto! Agora o Visual Studio Code está configurado para identificar o UTF-8 em seus projetos. Isso significa que você poderá trabalhar com caracteres especiais e acentuação sem problemas.

Lembre-se de que a configuração correta do encoding é importante para evitar erros na hora de salvar e executar seus projetos. Com essa simples configuração, você poderá se concentrar em escrever seu código sem se preocupar com problemas de codificação.