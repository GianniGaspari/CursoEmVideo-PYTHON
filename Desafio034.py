"""
Desafio034:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250, calcule um aumento de 10%.
Para salários inferiores ou igual a R$1.250, o aumento será de 15%.
"""


salario = float(input('Qual o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${} agora'.format(salario, novo))
