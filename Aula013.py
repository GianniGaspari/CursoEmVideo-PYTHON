#    ESTRUTURA DE REPETIÇÃO 'FOR'    #

print('\033[33m-=-INÍCIO DA AULA\033[m'*10)
for c in range(10, 0, -1):
    print(c)
print('-=-'*10)

for c in range(10, 0, -2):
    print(c)
print('-=-'*10)

for a in range(0, 6):
    print(a)

print('-=-'*10)

n1 = int(input('\033[33mDigite um número de 0 a 10\033[m: '))
for c in range(0, n1):
    print(c)
print('-=-'*10)

for c in range(0, n1+1):
    print(c)
print('-=-'*30)

inicio = int(input('INÍCIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
for p in range(inicio, fim+1, passo):
    print(p)
print('FIM')

print('-=-'*10)

for b in range(0, 3):
    n2 = int(input('Digite um valor: '))
print('Fim')
print('-=-'*10)

s = 0
for b in range(0, 4):
    n2 = int(input('Digite um valor: '))
    s += n2
print('O somatório de todos os valores foi: {}'.format(s))

print('\033[31m-=-FIM DA AULA\033[m'*10)
