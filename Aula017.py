#     LISTAS      #

# Tuplas ( )  →  Tuplas são imutáveis
# Listas [ ]  →  Listas SÃO MUTÁVEIS

# lanche = ['Hamburguer', 'Suco', 'Pizza', 'Picolé']

# Para adicionar ou alterar um valor na lista, usa-se o comando: 'append()'
# lanche.append('Cookie')

# Para adicionar e alterar a posição do item na lista, usa-se o comando: 'insert()'
# lanche.insert(0, 'Hot-dog')

# Para apagar elementos na lista, usa-se o comando: 'del lanche[3]
# e também o: 'lanche.pop[3]'
# ou o: lance.remove['picolé']
# Esses comandos, eliminam o elemento da lista e refazem a contagem da lista, reordenando-a


# num = (2, 5, 9, 1)
# print(num)

n = [2, 5, 9, 1, 8, 11, 69, 0]
print(n)
n[2] = 3
n[1] = 10
print(n)
n.append(4)
print(n)
n.insert(3, 11)
print(n)
n.sort()  # para colocar a lista ordenadamente
print(n)
n.sort(reverse=True)  # para colocar a lista ordenadamente, invertida
print(n)
print(f'Essa lista tem {len(n)} elementos.')
print('\033[36m#*\033[m'*20)
n.pop()  # se não indicar nenhum número, o comando pop elimina o último elemento
print(n)
n.pop(1)
print(n)
n.remove(2)
print(n)
if 2 in n:
    n.remove(2)
else:
    print('Não achei o número 2')
print('\033[36m#*\033[m'*20)
for c, v in enumerate(n):
    print(f'Na posição {c} encontrei o valor {v}!')
print('\033[36m#*\033[m'*20)
for cont in range(0, 5):
    n.append(int(input('Digite um valor para adicionar na lista: ')))
print(n)

A = [2, 3, 4, 7]
B = A
C = B[:]
print(f'Lista A: {A}')
print(f'Lista B: {B}')
print(f'Lista C: {C}')
print('\033[36m#*\033[m'*5)
B[2] = 8
print(f'Lista A: {A}')
print(f'Lista B: {B}')
print(f'Lista C: {C}')
print('\033[36m#*\033[m'*5)
B.insert(2, 4)
print(f'Lista A: {A}')
print(f'Lista B: {B}')
print(f'Lista C: {C}')
print('\033[36m#*\033[m'*5)
C.insert(2, 4)
print(f'Lista A: {A}')
print(f'Lista B: {B}')
print(f'Lista C: {C}')
print('\033[36m#*\033[m'*5)
