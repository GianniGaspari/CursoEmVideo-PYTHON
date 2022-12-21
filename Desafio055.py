"""
Desafio055:
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor dos pesos lidos.
"""


maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa em Kg:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {:.1f}Kg'.format(maior))
print('O menor peso lido foi {:.1f}Kg'.format(menor))

