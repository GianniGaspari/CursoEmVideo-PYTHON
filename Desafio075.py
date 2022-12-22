"""
Desafio 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
→ Quantas vezes apareceu o valor 9.
→ Em que posição foi digitado o primeiro valor 3.
→ Quais foram os números pares.
"""

n = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')),
     int(input('Digite o 3º número: ')), int(input('Digite o último número: ')))
print('')
print(f'Os números digitados foram: \033[32m{n}\033[m ')
print(f'O número \033[32m9\033[m apareceu \033[32m{n.count(9)} vezes\033[m.')
if 3 in n:
    print(f'O número \033[32m3\033[m foi digitado na \033[32m{n.index(3) + 1}ª vez\033[m.')
else:
    print('O número \033[32m3\033[m não foi digitado \033[1:4:31mnenhuma vez\033[m.')
print(f'Os números pares digitados foram: \033[32m', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
print('\033[m')
print('='*50)
print('{:^60}'.format('\033[1:4:32mFIM DO PROGRAMA\033[m'))
print('='*50)
