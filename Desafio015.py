"""
Desafio 015:
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado,
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
"""


d = int(input('Quantos dias de carro alugado?'))
km = float(input('Quantos Km rodados?'))
pago = (d * 60) + (km * 0.15)
print(f'Total a pagar é de R${pago:.2f}')
