"""
Desafio 090:
Faça um programa que leia o nome e média de um aluno, guardando também a situação num dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}:'))
if aluno['Média'] >= 7:
    aluno['Situação'] = '\033[30;46;51m Aprovado \033[m'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = '\033[30;43;51m Recuperação \033[m'
else:
    aluno['Situação'] = '\033[30;41;51m Reprovado \033[m'
print('-' * 20)
for k, v in aluno.items():
    print(f'{k}: {v}')
print(f'O(a) aluno(a) {aluno["Nome"]} está: {aluno["Situação"]}')
if aluno['Situação'] in '\033[30;46;51m Aprovado \033[m':
    print('-' * 59)
    print('→ → → → → → → → → → → → PARABÉNS ← ← ← ← ← ← ← ← ← ← ← ← ←')
    print('-' * 59)
elif aluno['Situação'] in '\033[30;43;51m Recuperação \033[m':
    print('-' * 59)
    print('Terá 15 dias para se preparar para a prova de recuperação.')
    print('-' * 59)
elif aluno['Situação'] in '\033[30;41;51m Reprovado \033[m':
    print('-' * 59)
    print('Infelizmente, terá mais um ano para rever todo o conteúdo')
    print('-' * 59)
