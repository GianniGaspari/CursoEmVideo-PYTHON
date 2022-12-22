"""
Desafio 076:
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, em sequência.
No final, mostre uma listagem de preços, organizando, organizando os dados em forma tabular.
"""

from time import sleep
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.99,
         'Estojo', 30,
         'Compasso', 38,
         'Mochila', 170,
         'Caneta', 2.35,
         'Pasta', 4.90,)
print('='*40)
print(f'{"PRODUTOS ESCOLARES E SEUS PREÇOS":^40}')
print('='*40)
sleep(1)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f' R${lista[pos]:>7.2f}')
sleep(10)
print('='*40)
print(f'\033[34m{"FIM DAS COMPRAS":^40}\033[m')
print('='*40)
