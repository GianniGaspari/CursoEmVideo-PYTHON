"""
Desafio 093:
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado num dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
partidas = list()
print('\033[32;40;52m-\033[m'*43)
print('\033[30;42;52m              CAMPEONATO 2022              \033[m')
print('\033[32;40;52m-\033[m'*43)
print()
jogador['Nome'] = str(input('Digite o nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
if total > 1:
    for c in range(0, total):
        partidas.append(int(input(f'\033[30;42;52m → Quantos gols {jogador["Nome"]} fez na {c + 1}ª partida? \033[m')))
    jogador['Gols'] = partidas[:]
    jogador['Total de gols'] = sum(partidas)
    print()
    print(f'O jogador {jogador["Nome"]} participou de {total} jogos no Campeonato Brasileiro, '
          f'com o total de {jogador["Total de gols"]} gols na temporada 2022.')
    for i, v in enumerate(jogador['Gols']):
        print(f'\033[30;42;52m → {i+1}ªpartida: {v} gols. \033[m')
elif total == 1:
    partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de gols'] = sum(partidas)
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
