"""
Desafio039:
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou o tempo que passou do prazo.
"""


from datetime import date
atual = date.today().year
print('''Para informar o sexo:
[ \033[31m1\033[m ] Masculino
[ \033[34m2\033[m ] Feminino''')
opção = int(input('Digite um dos números aqui ao lado: '))
if opção == 2:
    print('Você não é obrigada a se alistar.')
else:
        nasc = int(input('Ano de nascimento: '))
        idade = atual - nasc
        print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
        if idade == 18:
            print('Você tem que se alistar \033[31mIMEDIATAMENTE\033[m!')
        elif idade < 18:
            saldo = 18 - idade
            print('Você ainda \033[mnão tem 18 anos. Faltam {} anos para o Alistamento.'.format(saldo))
            ano = atual + saldo
            print('Seu alistamento será em {}'.format(ano))
        elif idade > 18:
            saldo = idade - 18
            print('Você já deveria ter se alistado há {} anos.'.format(saldo))
            ano = atual - saldo
            print('Seu Alistamento foi em {}'.format(ano))
