"""
Desafio 009:
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

# Primeiro Exemplo de formatação:
""" 
n = int(input('Digite um número para ver sua tabuada:'))
print('-'* 13)
print('{} x {:2} = {:3}'.format(n, 1, n*1))
print('{} x {:2} = {:3}'.format(n, 2, n*2))
print('{} x {:2} = {:3}'.format(n, 3, n*3))
print('{} x {:2} = {:3}'.format(n, 4, n*4))
print('{} x {:2} = {:3}'.format(n, 5, n*5))
print('{} x {:2} = {:3}'.format(n, 6, n*6))
print('{} x {:2} = {:3}'.format(n, 7, n*7))
print('{} x {:2} = {:3}'.format(n, 8, n*8))
print('{} x {:2} = {:3}'.format(n, 9, n*9))
print('{} x {:2} = {:3}'.format(n, 10, n*10))
print('-'*13)
"""

# Segundo Exemplo de formatação: (só que agora com 'f'string)
n = int(input('Digite um número para ver sua tabuada:'))
print('-' * 13)
print(f'{n} x {1:2} = {n*1:3}')
print(f'{n} x {2:2} = {n*2:3}')
print(f'{n} x {3:2} = {n*3:3}')
print(f'{n} x {4:2} = {n*4:3}')
print(f'{n} x {5:2} = {n*5:3}')
print(f'{n} x {6:2} = {n*6:3}')
print(f'{n} x {7:2} = {n*7:3}')
print(f'{n} x {8:2} = {n*8:3}')
print(f'{n} x {9:2} = {n*9:3}')
print(f'{n} x {10:2} = {n*10:3}')
