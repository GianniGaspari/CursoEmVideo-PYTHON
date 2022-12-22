"""
Desafio 013:
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
"""


s = float(input('Qual o salário do funcionário? R$'))
n = s + (s * 15 / 100)
n2 = 12 * (s * 15 / 100)
print(f'O funcionário que ganhava R${s:.2f}, com 15% de aumento passará a ganhar R${n:.2f}')
print(f'Terá em 1 ano, R${n2} de aumento em seu caixa')
print(f'Representado por R${n} x 12 = {n2}')
