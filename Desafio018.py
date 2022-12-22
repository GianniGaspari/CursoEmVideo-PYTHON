"""
Desafio 018:
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# Primeiro jeito
from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que deseja: '))
s = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
c = cos(radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
t = tan(radians(a))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, t))


# Segundo jeito
"""import math
a = float(input('Digite o ângulo que deseja: '))
s = math.sin(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
c = math.cos(math.radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
t = math.tan(math.radians(a))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, t))"""
