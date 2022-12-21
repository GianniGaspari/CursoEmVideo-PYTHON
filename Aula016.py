########     Variáveis compostas → TUPLAS     #########


# → As tuplas são imutáveis. Uma vez definida a Tupla, ela vai ficar assim até o final do programa.
# → Toda tupla fica entre parênteses ()
# → No python novo, não precisa de parênteses


# Usando variáveis simples:
lanche1 = 'Hamburguer'
lanche2 = 'Suco'
lanche3 = 'Pizza'
lanche4 = 'Pudim'
print(f'{lanche1}, {lanche2}, {lanche3}, {lanche4}')
print('-=-' * 20)

# Usando Tuplas:
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(lanche)
print(lanche[0])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])  # no fatiamento, é desconsiderado o último
print(lanche[0:3])
print(lanche[2:])  # elemento dois até o final
print(lanche[:2])  # do início até o elemento dois
print(lanche[-2])
print(lanche[-2:])  # do menos dois até o final
print('-=-' * 20)

for comida in lanche:  # se não precisar marcar posição, essa é a maneira mais simples
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('-=-' * 20)

print(len(lanche))
print('-=-' * 20)

for cont in range(0, len(lanche)):
    print(cont)
print('Comi pra caramba')
print('-=-' * 20)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer um monte de {lanche[cont]} na posição {cont}')  # melhor para usar posição
print('Comi pra caramba')
print('-=-' * 20)

for pos, comida in enumerate(lanche):  # também pode ser usado para marcar posição
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print('-=-' * 20)

print(sorted(lanche))
print(lanche)
print('-=-' * 20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
d = a + b
print(a)
print(b)
print(c)
print(len(c))
print(c.count(5))  # quantas vezes aparece o número 5 em c
print(c.index(8))  # a propriedade index mostra a posição da tupla c
print(d.index(8))  # a propriedade index mostra a posição da tupla d
print(d.index(5))
print(d.index(5, 1))  # deslocamento
print('-=-' * 20)

pessoa = ('Gianni', '33', 'M', '180')
print(pessoa)
pessoas = ('Gianni', 'Thamy', 'Violeta')
del pessoas  # tupla é imutável, mas pode ser deletada.
# print(pessoas)
print('-=-' * 20)
