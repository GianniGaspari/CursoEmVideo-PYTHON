"""
Desafio051:
Desenvolva um programa que leia o
primeiro termo e a razão de uma P.A.
e no final mostre os 10 primeiros
termos dessa progressão.
"""


print('='*30)
print('    10 TERMOS DE UMA P.A.')
print('='*30)
p1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = p1 + (10 - 1) * razão
for c in range(p1, décimo + razão, razão):
    print('\033[33m{}\033[m '.format(c), end=' \033[31m→\033[m ')
print('\033[34mACABOU\033[m')