#         FUNÇÕES / FUNCTIONS         #


def lin():
    print('-' * 30)


lin()
print('       Curso em Video')
lin()
print('       Aprenda Python')
lin()
print('       Gustavo Guanabara')
lin()

print()
lin()
print('       Curso em Video')
print('       Aprenda Python')
print('       Gustavo Guanabara')
lin()
print()


def mensagem(msg):
    print('\033[31m-\033[m' * 30)
    print(msg)
    print('\033[31m-\033[m' * 30)


mensagem('Sistema de alunos')
print()


def titulo(txt):
    print('\033[31m▓\033[m' * 40)
    print(txt)
    print('\033[33m▓\033[m' * 40)
    print()
    print()


titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')


def soma(a, b, c):
    print('\033[36m▓\033[m' * 40)
    print(f'  A = {a}\n  B = {b}\n  C = {c}')
    s = a + b + c
    print()
    print(f'SOLUÇÃO:  {a} + {b} = {s}')
    print('\033[35m▓\033[m' * 40)
    print()
    print()


# Programa principal
soma(4, 5, 1)
soma(8, 9, 2)
soma(2, 1, 3)
soma(b=2, a=1, c=3)
soma(c=3, a=2, b=1)


def contador(*num):
    for v in num:
        print(f'{v} ', end='')


contador(1, 2, 3, 4, 5)
contador(6, 7, 8)
print()


def contador2(*n):
    tam = len(n)
    print(f'Recebi os valores{n} e são ao todo {tam} números.')
    print()


contador2(1, 2, 3, 4, 5)
contador2(6, 7, 8)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobra(valores)
print(valores)


def soma3(* valoress):
    s = 0
    for nm in valoress:
        s += nm
    print(f'Somando os valores {valoress} temos {s}')


soma3(5, 2)
soma3(2, 4, 8)
