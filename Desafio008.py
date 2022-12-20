"""
Desafio008:
Escreva um progama que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

medida = float(input('Digite um valor em metros para fazermos a conversão: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
dam = medida / 10
hm = medida / 100
dm = medida / 10
print(f'A medida de {medida:.0f} metros equivale a: \n{cm:.0f} centímetros \n{mm:.0f} milímetros')
print(f'{dm} decímetros \n{dam} decâmetros')
print(f'{hm} hectometros \n{km} kilometros')
