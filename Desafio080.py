"""
Desafio 080:
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os numa lista,
já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:    # n > lista[len(lista)]
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-='*27)
print(f'Os valores digitados em ordem foram: {lista}')
