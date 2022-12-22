#     ESTRUTURA DE REPETIÇÂO 'WHILE'     #


# using "for/in"
for c in range(1, 11):
    print(c)
print('Fim')

# the same program, but using "while"
c = 1
while c < 11:
    print(c)
    c += 1
    #  c = c + 1
print('Fim')



# Usa-se o 'for' quando se sabe o limite de valores.
for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('Fim')

# Usa-se o 'while' quando não se sabe o limite de valores.
#     n != 0    ==  Flag(ponto de parada)
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()  # para jogar para MAIÚSCULO usa-se o .upper
print('FIM')


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:            # esse 'if' foi para não contar o número 0 como número par.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
