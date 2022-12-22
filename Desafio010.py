"""
Desafio 010:
Faça um programa que leia quanto dinheiro uma pessoa tem na carteira,
e mostre quantos dólares ela pode comprar com esse dinheiro. (Use a conversão atual)
"""

real = float(input('Qual valor que vc tem? R$'))
dolar = real / 5.29
euro = real / 5.60
print('Com R${:.2f} reais é possível comprar ${:.2f} dólares e EU${:.2f} euros.'.format(real, dolar, euro))
