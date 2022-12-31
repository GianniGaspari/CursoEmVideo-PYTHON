"""
Desafio 091:
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados num dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter
print('\033[31;40;51m-\033[m'*40)
print('\033[30;41;51m              JOGO DO DADO              \033[m')
print('\033[31;40;51m-\033[m'*40)
jogo = {'\033[30;46;51m  Jogador nº1  \033[m': randint(1, 6),
        '\033[30;45;51m  Jogador nº2  \033[m': randint(1, 6),
        '\033[30;42;51m  Jogador nº3  \033[m': randint(1, 6),
        '\033[30;43;51m  Jogador nº4  \033[m': randint(1, 6)}
sleep(1)
ranking = list()
print()
print('\033[30;41;51mVALORES SORTEADOS:                      \033[m')
sleep(1)
for k, v in jogo.items():
    print(f'{k}', end='')
    sleep(1)
    print(f'\033[30;41;51m          \033[m\033[31;40;51m  {v}  \033[m\033[30;41;51m          \033[m')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(0.5)
print()
# print(ranking)
print('\033[30;41;51m     ↓ ↓ ↓ ↓ ↓   RANKING   ↓ ↓ ↓ ↓ ↓    \033[m')
sleep(1)
print()
for i, v in enumerate(ranking):
    print(f'\033[30;41;51m  {i+1}º lugar:  \033[m{v[0]}\033[30;41;51m   jogou {v[1]}. \033[m')
    sleep(0.2)
print()
print('\033[31;40;51m-\033[m'*40)
print('\033[30;41;51m               FIM DO JOGO              \033[m')
print('\033[31;40;51m-\033[m'*40)
