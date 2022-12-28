"""
Desafio 084:
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo numa lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

from time import sleep
linha = '\033[33m*\033[m'*45
lista = []
dado = []
print(linha)
maior = menor = 0
while True:
    dado.append(str(input('NOME: ')))
    dado.append(int(input('PESO(Kg): ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [\033[36mS\033[m/\033[31mN\033[m] '))
    print()
    print('Próximo cadastro →')
    sleep(0.5)
    if resp in 'Nn':
        print('SÓ UM INSTANTE...')
        break
sleep(1)
print(linha)
print(f'Foram cadastradas {len(lista)} pessoas.')
sleep(0.5)
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}/ ', end='')
print()
sleep(0.5)
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}/ ', end='')
print()
print(linha)
sleep(2)
print('FIM DO PROGRAMA')
