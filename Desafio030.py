"""
Desafio 030:
Crie um programa que leia um número inteiro, e mostre na tela se ele é PAR ou ÍMPAR.
"""


n = int(input('Me diga um numero qualquer: '))
resultado = n % 2
if resultado == 0:
    print('O numero {} é PAR'.format(n))
else:
    print('O numero {} é IMPAR'.format(n))
