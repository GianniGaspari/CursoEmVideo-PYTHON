"""
Desafio 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) num dicionário.
Se por acaso o CTPS diferir de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente além da idade, com quantos anos a pessoa irá se aposentar.
"""

from time import sleep
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
print()
nasc = int(input(f'Ano de Nascimento do(a) {dados["Nome"]}: '))
print()
idade = datetime.now().year - nasc
dados['CTPS'] = str(input(f'O(a) {dados["Nome"]} possui Carteira de Trabalho? \n'
                          f'\033[30;41;51mDigite X se NÃO possuir\033[m: '))
if dados['CTPS'] in 'Xx':
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = ((dados['Contratação'] + 35) - datetime.now().year)
sleep(0.5)
print()
print('\033[30;43;51m*\033[m'*23)
for k, v in dados.items():
    print(f'- {k}: {v}.')
    sleep(0.7)
print('\033[30;43;51m*\033[m'*23)
