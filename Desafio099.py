"""
Desafio 099:
Faça um programa que tenha uma função chamada "maior()", que receba vários parâmetros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(*num):
    cont = maior = 0
    print()
    print('\033[33m▓\033[m' * 46)
    print('Valores passados: ')
    for v in num:
        print(f'\033[30;46;51m {v} \033[m', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print('\nAnalisando valores...')
    sleep(2)
    print(f'Foram informados \033[30;46;51m {cont} \033[m valores ao todo.')
    print(f'Dentre eles, o maior valor informado foi → \033[30;46;51m {maior} \033[m')
    sleep(3)


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 9)
maior(1, 2)
maior(6)

print()
print('\033[31m▓\033[m' * 46)
print('\033[33m FIM \033[m' * 9)
print('\033[31m▓\033[m' * 46)
