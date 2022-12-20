"""
Escreva um programa que leia um número 'n' inteiro qualquer e
mostre na tela os 'n' primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""
nome = '\033[31mSEQUÊNCIA DE FIBONACCI\033[m'
print('\033[33m   *   \033[m'*20)
print(' ')
print(f'{nome:^160}')
print(' ')
print('\033[33m   *   \033[m'*20)
print(' ')
n = int(input('Quantos termos quer mostrar? '))
print(' ')
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → \033[31mFIM\033[m')


