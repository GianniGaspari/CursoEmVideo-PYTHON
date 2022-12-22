"""
Desafio 029:
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite.
"""


from time import sleep
'''print('*'*165)
print('Olá. Seja bem vindo.')
n = str(input('Me diga seu nome completo por favor, para que possa melhor lhe atender.')).strip()
nome = n.split()
print('Olá {}! Muito prazer em te conhecer.'.format(nome[0]))'''
vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite de 80mk/h!')
    multa = (vel-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia, diriga com segurança!')
print('*'*40)
