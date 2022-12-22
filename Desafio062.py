"""
Desafio 062:
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostral mais alguns termos.
 O programa encerra qual ele disser que quer mostrar 0 termos(nenhum termo).
 """

print('='*30)
print('10 Primeiros TERMOS DE UMA P.A.')
print('='*30)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados: '.format(total))