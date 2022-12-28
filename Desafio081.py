"""
Desafio 081:
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e se está ou não na lista.
"""

valores = []
linha = '\033[33m*=*\033[m'*20
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [\033[36mS\033[m/\033[31mN\033[m] '))
    if resp in 'Nn':
        break
print(f'{linha}')
print(f'Você digitou {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print('O valor 5 \033[36mfaz\033[m parte da lista.')
else:
    print('O valor 5 \033[31mnão\033[m foi digitado na lista.')
print(f'{linha}')
fim = '\033[31mFIM DO PROGRAMA\033[m'
print(f'{fim:^65}')
