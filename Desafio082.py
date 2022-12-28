"""
Desafio 082:
Crie um programa que vai ler vários números e colocar numa lista.
Depois disso, crie duas listas extras que vão contar apenas os valores pares
e os valores impares digitados, respetivamente.
Ao final, mostre o conteúdo das 3 listas.
"""

l1 = []
pares = []
impares = []
while True:
    l1.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(l1):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('*'*30)
l1.sort()
pares.sort()
impares.sort()
print(f'A lista completa de números digitados é: {l1}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
print('*'*30)
print('\033[31mFIM DO PROGRAMA')
