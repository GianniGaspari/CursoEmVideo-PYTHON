#     LISTAS COMPOSTAS      #

"""
teste = list()
teste.append('Gianni')
teste.append(34)
print(teste)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
"""

"""
galera = [['Gianni', 34, 180], ['Thamy', 34, 160], ['Violeta', 8, 142], ['Valentim', 8, 140],
          ['Amora', 10, 146], ['Liz', 13, 155]]
print(galera[2][0])
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade e {pessoa[2]} cm de altura.')
"""

galera = []
dado = []
totmai = totmen = 0
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    dado.append(int(input('Altura: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    # print(f'{p[0]} tem {p[1]} anos de idade e {p[2]} cm de altura')
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
    if p[2] <= 150:
        print(f'{p[0]} tem menos de 150cm.')
    else:
        pass
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')
