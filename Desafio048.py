"""
Faça um programa que calcule a soma entre todos números ímpares que são múltiplos de três e
que se encontram no intervalo de 1 até 500.
"""


soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('Qual a soma dos números impares multiplos de 3 que estão entre o número 1 e 500?')
print('='*50)
print('A soma de todos os \033[33m{}\033[m valores solicitados é \033[33m{}\033[m'.format(cont, soma))
