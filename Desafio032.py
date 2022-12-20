"""
Desafio032:
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""


from datetime import date
ano = int(input('\033[1mQue ano quer analisar?\033[m Para descobrir se o atual ano é \033[1mBISSEXTO, apenas digite 0 '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[1mBISSEXTO\033[m'.format(ano))
else:
    print('O ano {} não é \033[1mBISSEXTO\033[m'.format(ano))
