"""
Desafio031:

"""

dist = float(input('Qual é a distância da viagem? '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(dist))
'''if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45'''
preço = dist * 0.50 if dist <=200 else dist * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
