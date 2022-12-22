"""
Desafio 017:
Faça um programa que leia o comprimento do cateto oposto, e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

# Primeiro jeito
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')


# Segundo jeito
"""import math
co = float(input('Comprimento do cateto oposto: '))
ca =  float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""

# Terceiro Jeito
"""co = float(input('Comprimento do cateto oposto: '))
ca =  float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""
