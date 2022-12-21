"""
Desafio069:
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos.
"""

from time import sleep
titulo = '\033[36mPROGRAMA DE CADASTRAMENTO\033[m'
linha = '\033[32m-*-\033[m'*10
print('')
print(f'{titulo:^60}'*3)
print('')
sleep(1)
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        sleep(1)
    if resp == 'N':
        break
print(linha)
print(f'Total de {tot18} pessoas com mais de 18 anos.')
print(f'Ao todo, temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos cadastradas.')
print(linha)
