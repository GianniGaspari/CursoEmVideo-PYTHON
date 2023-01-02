time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [ S / N ] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S para sim e N para não. ')
    if resp == 'N':
        break
print('-'*40)
print('', end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f' {k+1:<} ', end='')
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
            print(f'No {i+1}º jogo fez: {g} gols')
    print('-'*40)
print(' → → FIM DO PROGRAMA ← ← ')
