"""
Desafio 089:
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""

from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª nota:'))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('*'*50)
print(f'{"Nº":<5}{"NOME":<30}{"MÉDIA":>8}')
print('*'*50)
for i, a in enumerate(ficha):
    print(f'{i+1:<5}{a[0]:<30}{a[2]:>8.1f}')
while True:
    print('*'*50)
    opc = int(input('Deseja ver as notas de qual aluno? (Digite \033[31m999\033[m para sair) → '))
    if opc == 999:
        print()
        print('Finalizando programa...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
sleep(1)
print()
print('*'*15)
print(' \033[4:4:34mVOLTE SEMPRE\033[m')
print('*'*15)
