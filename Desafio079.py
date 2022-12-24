"""
Desafio 079:
Crie um programa onde o usuário possa digitar vários números e cadastra-los em uma lista.
Caso o número já exista la dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
"""

numbers = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numbers:
        numbers.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado → Já foi adicionado à lista.')
    r = str(input('Quer continuar? [\033[36mS\033[m/\033[31mN\033[m] '))
    if r in 'Nn':
        break
print('='*49)
numbers.sort()
print(f'\033[33mOs números listados foram:\033[m \033[1:4:33m{numbers}\033[m')
print(' ')
print('\033[31m=\033[m'*49)
print('{:^73}'.format('\033[31m#\033[m \033[1:4mFIM DO PROGRAMA\033[m \033[31m#\033[m'))
print('\033[31m=\033[m'*49)
