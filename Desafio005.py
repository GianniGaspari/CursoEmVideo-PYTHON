"""
Desafio 005:
Faça um programa que leia um número inteiro e mostre na tela seu número sucessor e seu antecessor.
"""

# Primeiro exemplo é criando 3 variáveis para chegar ao resultado.
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print(f'Analisando o valor {n}, seu antecessor é {a} e seu sucessor é {s}')

# Segundo exemplo é apenas com uma variável.
n = int(input('Digite um número: '))
print(f'Analisando o valor {n}, seu antecessor é {n - 1} e seu sucessor é {n + 1}')
