"""
Desafio074:
Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.
"""

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('')
print(f'Os valores \033[1:4:36msorteados\033[m foram: ', end='')
for num in n:
    print(f'{num} ', end='')
print('')
print(f'\nO \033[1:4:33mmaior\033[m valor sorteado foi: {max(n)} \033[33m>\033[m')
print('')
print(f'O \033[1:4:32mmenor\033[m valor sorteado foi: {min(n)} \033[32m<\033[m')
