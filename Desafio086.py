"""
Desafio 086:
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))
print('*'*27)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'\033[36m[\033[m{matriz[linha][coluna]:^7}\033[36m]\033[m', end='')
    print()
print('*'*27)
