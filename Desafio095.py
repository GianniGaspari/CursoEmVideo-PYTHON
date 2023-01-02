"""
Desafio 095:
Aprimore o desafio 093, para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.
"""

time = list()
jogador = dict()
partidas = list()
print('\033[32;40;52m-\033[m'*43)
print('\033[30;42;52m              CAMPEONATO 2022              \033[m')
print('\033[32;40;52m-\033[m'*43)
print()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    if total > 1:
        for c in range(0, total):
            partidas.append(int(input(f'\033[30;42;52m → Quantos gols {jogador["Nome"]} fez na '
                                      f'{c + 1}ª partida? \033[m')))
        jogador['Gols'] = partidas[:]
        jogador['Total de gols'] = sum(partidas)
        time.append(jogador.copy())
        while True:
            resposta = str(input('Quer continuar? [ S / N ]')).upper()[0]
            if resposta in 'SN':
                break
            print('ERRO! \nResponda apenas S para sim e N para não.')
        if resposta == 'N':
            break
        print()
    elif total == 1:
        partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida? ')))
        jogador['Gols'] = partidas[:]
        jogador['Total de gols'] = sum(partidas)
        time.append(jogador.copy())
        while True:
            resposta = str(input('Quer continuar? [ S / N ]')).upper()[0]
            if resposta in 'SN':
                break
            print('ERRO! \nResponda apenas S para sim e N para não.')
        if resposta == 'N':
            break
        print()
print('-'*40)
print('cod', end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f' {k:<} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [ 69 para parar) '))
    if busca == 69:
        break
    if busca >= len(time):
        print(f'ERRO! \nNão existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f' No {i+1}º jogo: {g} gols')
    print('-' * 40)
print(' → → FIM DO PROGRAMA ← ← ')
