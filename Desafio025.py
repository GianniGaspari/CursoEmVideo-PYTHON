"""
Desafio 025:
Crie um programa que leia o nome de uma peessoa e diga se ela tem "Silva" no nome.
"""


n = str(input('Digite seu nome completo: '))
# print('Seu nome tem Silva? {}'.format(n[:5] == 'Silva'))
print('Seu nome tem Silva? {}'.format('silva' in n.lower()))#in é um operador do Pyhon#
