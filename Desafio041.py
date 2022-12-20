"""
A Confederação Nacional de Natação precisa de programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""


from datetime import date
atual = date.today().year
nascimento = int(input('Informe o ano de nascimento para descobrir qual categoria pertence: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')
elif 9 < idade <= 14:
    print('Categoria: INFANTIL')
elif 14 < idade <= 19:
    print('Categoria : JUNIOR')
elif idade > 19 and idade <=25:
    print('Categoria: SÊNIOR')
elif idade > 25:
    print('Categoria: MASTER')

