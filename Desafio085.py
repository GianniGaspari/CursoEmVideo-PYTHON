"""
Desafio 085:
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
numa única lista que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.
"""

"""
n = []
pares = []
impares = []
for c in range(0, 7):
    n.append(int(input('Digite um valor: ')))
for v in n:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Dos 7 números digitados, {len(pares)} foram pares e {len(impares)} foram impares.')
pares.sort()
impares.sort()
print(f'Os números pares digitados foram: {pares}')
print(f'Os números impares digitados foram: {impares}')
"""

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[1].append(valor)
    else:
        num[0].append(valor)
print('*'*40)
print(f'Todos os valores: {num}')
num[0].sort()
num[1].sort()
print(f'Os números pares: {num[1]}')
print(f'Os números impares: {num[0]}')
print('*'*40)
print('FIM DO PROGRAMA')
