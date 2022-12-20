"""
Crie um programa que leia dois números e mostre a soma entre eles.
"""

# números inteiros:
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
total = n1 + n2
print(f'A soma entre {n1} e {n2} é {total}')   # com 'f'string
print('A soma entre {} e {} é {}'.format(n1, n2, total))     # sem 'f' string


# números flutuantes(quebrados):
n1 = float(input('Informe um número quebrado(Ex:5.5): '))
n2 = float(input('Informe outro número(Ex: 8.88): '))
total = n1 + n2
print(f'A soma entre {n1:.2f} e {n2:.2f} é {total:.2f}')
