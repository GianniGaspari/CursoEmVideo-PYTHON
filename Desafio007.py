"""
Desafio 007:
Faça um programa que leia as duas notas de um aluno, depois calcule e mostre a sua média entre as notas.
"""

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2      # Ordem de precedência
print(f'A média entre a nota {n1:.1f} e {n2:.1f} é {media:.1f}')
