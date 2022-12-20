"""
Escreva um programa que leia dois números inteiros
 e compare-os mostrando na tela uma mensagem:
- O primeiro valor é MAIOR
- O segundo valor é MENOR
- Não existe valor maior, os dois são iguais
"""


n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é \033[32mmaior\033[m')
elif n2 > n1:
    print('O SEGUNDO valor é \033[32mmaior\033[m')
elif n1 == n2:
    print('Não existe valor maior. Os dois são \033[34mIGUAIS\033[m')

