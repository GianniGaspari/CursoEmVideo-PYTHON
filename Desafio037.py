"""
Desafio037:
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal; 3 para hexadecimal
"""


from time import sleep
num = int(input('Digite um número inteiro: '))
print('''Agora escolha uma das bases para conversão:
[\033[33m 1\033[m ] converter para \033[33mBINÁRIO\033[m
[\033[32m 2\033[m ] converter para \033[32mOCTAL\033[m
[\033[31m 3\033[m ] converter para \033[31mHEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
print('\033[34mPROCESSANDO...\033[m')
sleep(1)
if opção == 1:
    print('{} convertido para \033[33mBINÁRIO\033[m é igual a \033[33m{}\033[m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para \033[32mOCTAL\033[m é igual a \033[32m{}\033[m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para \033[31mHEXADECIMAL\033[m é igual a \033[31m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('-=-'*20)
    print('\033[31:1mOpção inválida. \033[33mTente novamente.')
