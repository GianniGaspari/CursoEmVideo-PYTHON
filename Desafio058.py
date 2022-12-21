"""
Desafio058:
Melhore o jogo do DESAFIO 028, onde o computador vai pensar num número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final,
quantos palpites foram necessários para vencer.
"""


from random import randint
computador = randint(0, 10)     # no 'randint', o número mostrado é o que aparece. Diferente do 'for/in'.
print('\033[36m-=-\033[m'*30)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print('\033[36m-=-\033[m'*6)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[31:1mÉ mais\033[m...tente de novo.')
        elif jogador > computador:
            print('\033[31:1mÉ menos\033[m...tente de novo.')
print('\033[33m-=-\033[m'*14)
print('Você \033[36mACERTOU\033[m o palpite com {} tentativas.'.format(palpites))
print('\033[33m-=-\033[m'*14)