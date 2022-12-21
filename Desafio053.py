"""
Desafio053:
Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, descosiderando os espaços.
"""


f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = j[::-1]
'''
i = ''
for l in range(len(j) - 1, -1, -1):
    i += j[l]
'''
print('O inverso de {} é \033[36m→\033[m {}.'.format(j, i))
if i == j:
    print('Temos um \033[36mPALÍNDROMO\033[m!')
else:
    print('A frase digitada \033[31mNÃO é um PALÍNDROMO\033[m!')
