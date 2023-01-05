"""
Desafio 100:
Faça um programa que tenha uma lista chamada "números" e duas funções chamadas "sorteio()" e "somapar()".
A primeira função vai sortear 5 números e vai colocá-los dentro da lista, e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior.
"""
from time import sleep
from random import randint


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    print(' \033[31m▓\033[m', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f' {n} ', end='', flush=True)
        print('\033[31m▓ \033[m', end='')
        sleep(0.3)
    print('Pronto!')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print()
    print(f'Somando os valores pares de \033[31m{lista}\033[m, temos o resultado de → {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)
