"""
Desafio  071:
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$1, R$10, R$20 e R$50.
"""

titulo = '\033[36mCAIXA ELETRÔNICO\033[m'
print('='*159)
print('{:^20}'.format('BANCO GIM')*8)
print(f'{titulo:^28}'*8)
print('='*159)
valor = int(input('Que valor quer sacar? R$'))
total = valor
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        if ced == 100:
            ced = 50
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 159)
print('{:^40}'.format('\033[36mOBRIGADO\033[m')*5)
print('='*159)
