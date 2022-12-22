"""
Desafio 028:
Escreva um programa que faça o computador pensar um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""


from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-'*20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar: ')
print('-=-'*20)
jogador = int(input('Em que numero pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == comp:
    print('parabens, vc me venceu')
else:
    print('ganhei! pensei no numero {} e nao no {}'.format(comp, jogador))
