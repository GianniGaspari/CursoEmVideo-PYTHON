"""
Desafio031:
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
"""


dist = float(input('Qual é a distância da viagem? '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(dist))
'''if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45'''
preço = dist * 0.50 if dist <=200 else dist * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
