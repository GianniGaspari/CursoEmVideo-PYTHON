"""
Desafio 006:
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

# Primeiro Exemplo com mais de uma variável:
n = int(input('Digite um número: '))
d = n * 2    # dobro
t = n * 3    # triplo
r = n ** (1/2)  # raiz quadrada
print(f'O dobro de {n} vale {d}.')
print(f'O triplo de {n} vale {t}')
print(f'A raiz quadrada de {n} vale {r:.2f}')    # → {:.2f} é para deixar com duas casas decimais.


# Segundo Exemplo com apenas 1 variável:
n = int(input('Digite um número: '))
print(f'O dobro de {n} vale {n*2}.')
print(f'O triplo de {n} vale {n*3}')
print(f'A raiz quadrada de {n} vale {n**(1/2):.2f}')
print(f'Raiz cúbica: {n**(1/3):.2f}\nQuadrada com a função POW: {pow(n, (1/2)):.2f}')
print(f'Raiz cúbica com função POW: {pow(n, (1/3)):.2f}')
