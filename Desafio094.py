"""
Desafio 094:
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa num dicionário.
No final, mostre:
A) Número de pessoas cadastradas.
B) A média de idade entre elas.
C) Uma lista com as mulheres.
D) Uma lista com idade acima da média.
"""


# print('\033[31;40;51m-\033[m'*40)
# print('\033[30;41;51m              JOGO DO DADO              \033[m')
# print('\033[31;40;51m-\033[m'*40)

galera = list()
pessoa = dict()
soma =  média = 0
print('\033[30;46;51m•\033[m'*165)
print()
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [ M / F ]')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('\033[30;41;51m  ERRO! \033[m\nPor favor, digite apenas M para masculino ou F para feminino.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [ S / N ]')).upper()
        if resp in 'SN':
            break
        print('\033[30;41;51m  ERRO! \033[m\nResponda apenas S para sim e N para não.')
    if resp == 'N':
        break
print('\033[30;46;51m•\033[m'*165)
print()
print(f'A) Ao todo, temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end='')
print()
print('D) Lista das pessoas acima da média: ', end='')
for p in galera:
    if p['Idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} | ', end='')
        print()
print('\033[30;46;51m•\033[m'*69)
print('\033[30;47;51m                            FIM DO PROGRAMA                          \033[m')
print('\033[30;46;51m•\033[m'*69)
