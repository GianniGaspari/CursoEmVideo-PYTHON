"""
Desafio004:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

# Independente do que for mostrado aqui vai aparecer o tipo string, pois a função input retorna sempre uma função...
# ...string, a menos q seja direcionado antes com outra função.
a = input('Digite algo para descobrir o tipo primitivo: ')
print('O tipo primitivo do que foi digitado é: ', type(a))

a = input(print('Digite algo:'))
print('Seu tipo primitivo é: ', type(a))
print('Só tem espaços?: ', a.isspace())
print('É um número?: ', a.isnumeric())
print('É alfabético?: ', a.isalpha())
print('É alfanumérico?: ', a.isalnum())
print('Está em maiúsculas?: ', a.isupper())
print('Está em minúsculas?: ', a.islower())
print('Está capitalizada?: ', a.istitle())
