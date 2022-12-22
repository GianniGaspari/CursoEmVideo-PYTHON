"""
Desafio 060:
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

"""
# Primeiro jeito
from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))"""

# Segundo jeito
from time import sleep

n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando: \033[33m{}!\033[m = '.format(n), end='')
sleep(2)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('\033[33m{}\033[m'.format(f))
