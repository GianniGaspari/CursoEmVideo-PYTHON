"""
Desafio 097:
Faça um programa que tenha uma função chamada "escreva()", que receba
um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def escreva(msg):
    tamanho = len(msg) + 8
    print('*' * tamanho)
    print(f'    {msg}')
    print('*' * tamanho)
    print()


# MP
escreva(input('Nome completo: '))
escreva(input('Nacionalidade: '))
escreva(input('Idade: '))
escreva(input('Área de atuação: '))
escreva(input('O que deseja criar e desenvolver na empresa: '))
