"""
Desafio 014:
Faça um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""

c = float(input('Qual a temperatura em Celsius?'))
# f = ((9*c)/5) + 32
f = 9*c/5+32
print(f'A temperatura de {c}ºC corresponde a {f}ºF')
