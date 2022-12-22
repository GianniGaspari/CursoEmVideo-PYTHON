"""
Desafio 077:
Crie um programa que tenha uma tupla com várias palavras (NÃO USAR ACENTOS).
Depois disso, deverá mostrar, para cada palavra, quais são suas vogais.
"""


from time import sleep
t = ('\033[33mamora\033[m', '\033[33mamor\033[m', '\033[33mabobora\033[m', '\033[33mtamarindo\033[m',
     '\033[33mgoiaba\033[m', '\033[33muva\033[m', '\033[33mgroselha\033[m', '\033[33mguarana\033[m',
     '\033[33mpessego\033[m', '\033[33mmorango\033[m', '\033[33mjaboticaba\033[m')
for p in t:
    print(f'\nNa palavra \033[1:4m{p.upper()}\033[m temos as seguintes vogais: ', end='')
    sleep(1)
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[32m{letra}\033[m', end=' ')
            sleep(0.5)
print('\n ')
sleep(1)
print('\033[1:4:36m*\033[m'*80)
print(f'{"FIM DO PROGRAMA DAS VOGAIS":^80}')
