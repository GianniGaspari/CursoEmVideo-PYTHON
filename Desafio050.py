"""
Desafio 050:
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o.
"""


soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números \033[33mPARES\033[m e a soma foi {}'.format(cont, soma))
