"""
Desafio 096:
Faça um programa que tenha uma função chamada: área().
E faça que ela receba as dimensões de um terreno retangular(largura e comprimento)
e mostre a área do terreno.
"""


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {a}m²')


print(' CONTROLE DE TERRENOS ')
print('-' * 20)
larg = float(input('Largura(m): '))
comp = float(input('Comprimento(m): '))
area(larg, comp)
