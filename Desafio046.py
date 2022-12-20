"""
Faça um desafio que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep
print(' ')
i = str(input('''Digite qualquer \033[1mnúmero\033[m ou \033[1mletra\033[m do teclado
para iniciar a \033[33mCONTAGEM REGRESSIVA\033[m
e depois aperte \033[3m"Enter"\033[m: '''))
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[35mFELIZ\033[m \033[34mANO\033[33m \033[33mNOVO\033[m       ' * 5)
print('\033[33m-=-\033[m' * 35)
sleep(1)
print('\033[34mFELIZ\033[m \033[33mANO\033[33m \033[32mNOVO\033[m       ' * 5)
print('\033[32m-=-\033[m' * 35)
sleep(1)
print('\033[32mFELIZ\033[m \033[31mANO\033[33m \033[36mNOVO\033[m       ' * 5)
print('\033[34m-=-\033[m' * 35)
sleep(1)
print('\033[36mFELIZ\033[m \033[35mANO\033[33m \033[34mNOVO\033[m       ' * 5)
print('\033[32m-=-\033[m' * 35)
sleep(1)
