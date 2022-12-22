#     INTERROMPENDO REPETIÇÔES 'WHILE'     #


# O comando 'break' quebra o laço 'while'.


#  Esse código vai ficar com loop infinito

"""
cont = 1
while True:
    print(cont, ' → ', end='')
    cont += 1
print('Acabou')
"""

# Esse código lê até o número indicado e para.
"""
cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')
"""

# Esse código vai ler infinitas vezes, a nao ser que digite o número 999
"""
n = 0
while n != 999:      # != (Diferente)
    n = int(input('Digite um número: '))
"""

# Esse código faz a variável cont(contador) realizar a operação 3 vezes
"""
n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1
"""

# Esse código não exclui o número 999 da soma
"""
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s))
"""

# Esse código exclui, mas com gambiarra
"""
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))
"""

# Esse código interrompe o loop causado pela função True, usando o 'break'
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
print(f'O resultado da soma é {s}')  # facilitando a linha de codigo 67, usando uma 'f' string.

nome = 'José'
idade = 33
salario = 1600.30
print(f'O {nome} tem {idade} anos.')  # com o 'f string'      # Python 3.6+
print('O {} tem {} anos.'.format(nome, idade))  # sem o 'f string'      # Python 3
print('O %s tem %d anos.' % (nome, idade))  # jeito antigo usado no Python 2
print(f'O {nome:^20} tem {idade:->10} e ganha R${salario:.2f}')
#  '^' para centralizar / o número 20 são espaços / > ou < para alinhar a direita ou esquerda
