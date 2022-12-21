"""
Desafio064:
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada(flag).
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando a flag).
"""

n = cont = soma = 0
n = int(input('Digite um número [999 para acabar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para acabar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
