"""
Crie um programa que mostre na tela todos
os números pares que estão no intervalo entre 1 e 50.
"""

from time import sleep
print('Os números pares entre 1 e 50 são:')
sleep(2)
for c in range(2, 50, +2):
    print(c, end=' \033[33m/\033[m ')
