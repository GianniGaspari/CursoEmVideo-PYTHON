"""
Desafio016:
Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela sua porção inteira.
Ex: Digite um número: 6.127
Porção inteira: 6
"""


# Primeiro jeito
n = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, int(n)))

# Segundo jeito
'''from math import trunc
n = float(input('Digite um valor: '))
print('O valor foi {} e sua porção inteira é {}'.format(n, trunc(n)))'''
