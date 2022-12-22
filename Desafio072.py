"""
Desafio 072:
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
O programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
"""


from time import sleep
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('\033[1;31mTente novamente\033[m. ')
        sleep(0.5)
    print(f'Você digitou o número \033[33m{tupla[n]}\033[m')
    continuar = str(input('Quer continuar? [ \033[36mS\033[m / \033[31mN\033[m ]')).upper().strip()[0]
    if continuar in 'Nn':
        print('Encerrando...')
        break
    elif continuar in 'Ss':
        print('Vamos de novo então...')
sleep(1)
print('\033[31mFIM DO PROGRAMA\033[m')
