"""
Desafio040:
Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média ABAIXO de 5.0: REPROVADO
- Média ENTRE5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Sua Média é \033[34m{}\033[m'.format(m))
    print('Você foi \033[34mAPROVADO\033[m')
elif m > 5 or m > 7:
    print('Sua Média é \033[33m{}\033[m'.format(m))
    print('Você está de \033[33mRECUPERAÇÃO\033[m')
elif m < 5:
    print('Sua Média é \033[31m{}\033[m'.format(m))
    print('Você está \033[31mREPROVADO\033[m')
