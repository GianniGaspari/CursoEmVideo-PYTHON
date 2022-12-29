"""
Desafio 087:
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))
print('*'*27)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'\033[36m[\033[m{matriz[linha][coluna]:^7}\033[36m]\033[m', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
print('*'*27)
print(f'A soma dos valores pares é {somapar}')
print('*'*35)
for linha in range(0, 3):
    somacoluna += matriz[linha][0]
print(f'A soma dos valores da 1ª coluna é {somacoluna}')
somacoluna = 0
for linha in range(0, 3):
    somacoluna += matriz[linha][1]
print(f'A soma dos valores da 2ª coluna é {somacoluna}')
somacoluna = 0
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da 3ª coluna é {somacoluna}')
print('*'*35)
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')
print('*'*35)
print('FIM DO PROGRAMA')
