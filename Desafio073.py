"""
Desafio073:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão de futebol, em ordem de colocação.
Depois mostre:
→ Os 5 primeiros
→ Os 4 últimos
→ Times em ordem alfabética
→ Em que posição está o time do São Paulo.
"""

# Brasileirão 2022
from time import sleep
print('='*129)
print('{:^129}'.format('BRASILEIRÃO 2022'))
print('='*129)
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
         'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(f'Os primeiros 5 times do Brasileirão 2022 foram: \033[36m{times[:5]}\033[m')
print(f'Os últimos 4 foram \033[31m{times[-4:]}\033[m')
sleep(4)
print('')
print(f'Os times do Brasileirão 2022 em ordem alfabética ficam assim:\n{sorted(times)}')
sleep(5)
print('')
print(f'O \033[1:4mSão Paulo\033[m ficou na {times.index("São Paulo")+1}ª posição.')
print('')
sleep(2)
print('='*150)
print('{:^150}'.format('FIM DO PROGRAMA'))
print('='*150)
