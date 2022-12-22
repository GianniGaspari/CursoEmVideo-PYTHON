"""
Desafio 056:
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('\033[33m-------\033[m {}ª PESSOA \033[33m-------\033[m'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('\033[33m-\033[m'*50)
print('A \033[1mmédia\033[m de idade do grupo é de \033[1:33m{:.0f} anos\033[m'.format(mediaidade))
print(
    f'O \033[1mhomem mais velho\033[m tem \033[33m{maioridadehomem}\033[m anos e se chama \033[1:33m{nomevelho}\033[m.')
print('Ao todo, são \033[1:33m{}\033[m \033[1mmulheres\033[m com menos de 20 anos'.format(totmulher20))
