"""
Desafio 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
"""

from time import sleep
print('='*129)
print('{:^129}'.format('LISTA DE NÚMEROS'))
print('='*129)
sleep(1)
print('Vamos criar uma lista de números 5 números, ok? ')
sleep(1)
listanum: list = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('='*39)
print(f'Você digitou os números: {listanum}')
print(f'O maior número foi digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
sleep(2)
print('='*129)
print('{:^129}'.format('FIM DO PROGRAMA'))
print('='*129)
