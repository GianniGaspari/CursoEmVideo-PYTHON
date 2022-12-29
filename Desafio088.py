"""
Desafio 088:
Faça um programa que ajude um jogador da MEGA-SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep
titulo = '\033[36mMEGA-SENA\033[m'
linha = '\033[33m*=\033[m'
lista = []
jogos = []
print('{}'.format(linha)*80)
print(f'{titulo:^50}'*4)
print(f'{linha}'*80)
quant = int(input('Quantos jogos deseja fazer o sorteio?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1  # para interromper o loop infinito
sleep(0.2)
print()
print('→ '*3, f'Sorteando {quant} jogos...', ' ←'*3)
sleep(3)
print()
for i, lista in enumerate(jogos):
    print(f'Jogo \033[4:4m{i+1}\033[m: \033[34m{lista}\033[m')
    sleep(1)
print()
print(f'{linha}'*80)
print('\033[36m             B O A    S O R T E         \033[m'*4)
print(f'{linha}'*80)
