"""
Desafio 098:
Faça um programa que tenha uma função chamada "contador()", que receba 3 parâmetros: início, fim e passo.
Seu programa tem que realizar 3 contagens através da função criada:
A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem personalizada.
"""
from time import sleep


def contador(i, f, p):
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    print('\033[36m▓\033[m' * 33)
    print(f'A contagem de {i} até {f} de {p} em {p}:')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('→ FIM')
        print('\033[33m▓\033[m' * 33)
        sleep(0.5)
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('→ FIM')
        print('\033[33m▓\033[m' * 33)
        sleep(0.5)
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('\033[31m▓\033[m' * 33)
print('↓ CONTAGEM PERSONALIZADA ↓')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
