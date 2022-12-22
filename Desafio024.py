"""
Desafio 024:
Faça um programa que leia o nome de uma cidade  e diga se ela começa ou não com o nome "santo".
"""


c = str(input('Em que cidade nasceu? ')).strip()
print(c[:5].upper() == 'SANTO')
