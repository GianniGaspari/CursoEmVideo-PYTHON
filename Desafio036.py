"""
Desafio036:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário,
ou então o empréstimo será negado.
"""


casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de R$\033[36m{:.2f}\033[m'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser \033[34mCONCEDIDO!\033[m')
else:
    print('Empréstimo pode ser \033[31mNEGADO!\033[m')
