"""
Desafio 061:
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print('='*30)
print('10 Primeiros TERMOS DE UMA P.A.')
print('='*30)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = p1
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
