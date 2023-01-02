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
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    if total > 1:
        for c in range(0, total):
            partidas.append(int(input(f'\033[30;42;52m → Quantos gols {jogador["Nome"]} fez na {c + 1}ª partida? \033[m')))
        jogador['Gols'] = partidas[:]
        jogador['Total de gols'] = sum(partidas)
        while True:
            resposta = str(input('Quer continuar? [ S / N ]')).upper()[0]
            if resposta in 'SN':
                break
            print('ERRO! \nResponda apenas S para sim e N para não.')
        if resposta == 'N':
            break
        print()
        #print(f'O jogador {jogador["Nome"]} participou de {total} jogos no Campeonato Brasileiro, '
              #f'com o total de {jogador["Total de gols"]} gols na temporada 2022.')
        #for i, v in enumerate(jogador['Gols']):
            #print(f'\033[30;42;52m → {i+1}ªpartida: {v} gols. \033[m')
    elif total == 1:
        partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida? ')))
        jogador['Gols'] = partidas[:]
        jogador['Total de gols'] = sum(partidas)
        while True:
            resposta = str(input('Quer continuar? [ S / N ]')).upper()[0]
            if resposta in 'SN':
                break
            print('ERRO! \nResponda apenas S para sim e N para não.')
        if resposta == 'N':
            break
        print()
        if jogador['Total de gols'] > 1:
            print(f'O jogador {jogador["Nome"]} participou de apenas {total} jogo no Campeonato Brasileiro, '
                  f'com o total de {jogador["Total de gols"]} gols na temporada 2022.')
        elif jogador['Total de gols'] == 1:
            print(f'O jogador {jogador["Nome"]} participou de apenas {total} jogo no Campeonato Brasileiro, '
                  f'com {jogador["Total de gols"]} gol na temporada 2022.')
        else:
            print(f'O jogador {jogador["Nome"]} participou de apenas {total} jogo no Campeonato Brasileiro, '
                  f'sem marcar gols na temporada 2022.')
