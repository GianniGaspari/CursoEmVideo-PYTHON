"""
Desafio065:
Crie um programa que leia vários números inteiros no teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
valor lido. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(' ')
print('Você digitou \033[32m{}\033[m números e a média foi \033[32m{:.2f}\033[m'.format(quant, media))
print('O maior valor foi \033[34m{}\033[m e o menor foi \033[36m{}\033[m'.format(maior, menor))
