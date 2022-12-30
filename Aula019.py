#       DICIONÁRIOS        #
"""
Tuplas ( )
Listas [ ]
Dicionários { }

dados = dict()
ou
dados = {}

dados = {'nome':'Pedro, 'idade':25}
print(dados['nome'])    Pedro
print(dados['idade'])   25

Para criar um novo elemento(não funciona o append em dicionários):
dados['sexo']='M'

Para deletar um elemento:
del dados['idade']

print(dados.values())    Pedro 25
print(dados.keys())   nome idade
print(dados.items())   pedro 25 nome idade
"""


t = '\033[4;30;41;51mDICIONÁRIOS\033[m'
print()
print(f'{t:^170}')
print()
pessoas = {'Nome': 'Gianni', 'Sexo': 'M', 'Idade': 34}
print(pessoas)
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
pessoas['Cabelo'] = 'Cacheado'
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
del pessoas['Cabelo']
pessoas['Peso'] = 80
for k, v in pessoas.items():
    print(f'\033[4;30;41;51m{k:^7}\033[m \033[4;30;43;51m{v:^8}\033[m')
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

print()
brasil.append(estado1)
brasil.append(estado2)
print(f'\033[4;30;42;51m{estado1}\033[m')
print(f'\033[4;30;44;51m{estado2}\033[m')
print(f'\033[4;30;47;51m{brasil[0]}\033[m')
print(brasil[1]['UF'], end=' ')
print(brasil[1]['Sigla'])

estado = dict()
brasill = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasill.append(estado.copy())
print(brasill)
for e in brasill:
    print(e)
    for k, v in e.items():
        print(f'O {k} tem valor {v}')
for e in brasill:
    for v in e.values():
        print(v, end=' ')
    print()
