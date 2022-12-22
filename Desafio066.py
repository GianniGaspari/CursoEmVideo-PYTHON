"""
Desafio 066:
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles(desconsiderando o flag).
"""

s = cont = 0
while True:
    n = int(input('Digite um número[999 para parar] \033[33m→\033[m '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'O resultado da soma dos \033[36m{cont}\033[m números digitados é: \033[34m{s}\033[m')
