# coding: utf-8
frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

if(fruta_pedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')