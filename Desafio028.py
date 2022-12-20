"""
Desafio028:

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



