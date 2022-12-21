"""
Desafio057:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""


from time import sleep
print('Para informar o sexo masculido, digite \033[31mM\033[m.')
sleep(0.6)
print('Para informar o sexo feminino digite \033[34mF\033[m.')
sleep(1)
print('Qual seu sexo? ')
sexo = str(input("""[ \033[31mM\033[m ] [ \033[34mF\033[m ]""")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'Ff':
    print('Sexo \033[34m{}\033[m registrado com SUCESSO!'.format(sexo))
else:
    print('Sexo \033[31m{}\033[m registrado com SUCESSO!'.format(sexo))
