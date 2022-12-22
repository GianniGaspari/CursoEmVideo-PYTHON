"""
Desafio 045:
Crie um programa que faça o jogador jogar Jokenpô com você.
"""


from random import randint
from time import sleep
itens = ('\033[33mPEDRA\033[m', '\033[36mPAPEL\033[m', '\033[32mTESOURA\033[m')
computador = randint(0, 2)
print('''Suas opções:
\033[33m[ 0 ] PEDRA\033[m
\033[36m[ 1 ] PAPEL\033[m
\033[32m[ 2 ] TESOURA\033[m''')
jogador = int(input('Escolha uma jogada e aperte enter:'))
sleep(1)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')

sleep(1)
print('\033[34m-=-\033[m'*15)
print('O Computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogador]))
print('\033[34m-=-\033[m'*15)
print('\033[31mProcessando...\033[m')
sleep(3)
print('\033[35m * \033[m'*5)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[36mVOCÊ VENCEU\033[m')
    elif jogador == 2:
        print('\033[33mComputador VENCEU\033[m')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('\033[36mComputador VENCEU\033[m')
    elif jogador == 1:
        print('\033[36mEMPATE\033[m')
    elif jogador == 2:
        print('\033[32mVOCÊ VENCEU\033[m')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('\033[33mVOCÊ VENCEU\033[m')
    elif jogador == 1:
        print('\033[36mComputador VENCEU\033[m')
    elif jogador == 2:
        print('\033[32mEMPATE\033[m')
print('\033[35m * \033[m'*5)