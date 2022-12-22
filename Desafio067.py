"""
Desafio 067:
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.
"""

titulo = '\033[33mPROGRAMA DE TABUADA\033[m'
linha = '-*-'*54
fim = '\033[33mPROGRAMA ENCERRADO\033[m'
print('')
print(linha)
print(f'{titulo:^160}')
print(linha)
print('')

while True:
    n = int(input('Digite um número para saber a sua tabuada: '))
    print('')
    if n < 0:
        print(linha)
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print(f'{fim:^160}')
