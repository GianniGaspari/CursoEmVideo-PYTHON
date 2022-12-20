"""
Desafio012:
Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.
"""

# Primeiro exemplo de Porcentagem:
p = float(input('Qual o preço do produto? R$'))
novo = p - (p * 5 / 100)       # para calcular a porcentagem
print('O produto que custava R${:.2f}, com desconto de 5% vai custar R${:.2f}'.format(p, novo))

# Segundo exemplo com Porcentagem:
p = float(input('Qual o preço do produto? R$'))
novo = p - (p * 0.05)     # porcentagem
print('O produto que custava R${:.2f}, com desconto de 5% vai custar R${:.2f}'.format(p, novo))
