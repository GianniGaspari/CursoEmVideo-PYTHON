"""
Desafio 019:
Um profressor quer sortear 1 de seus 4 alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles, e escrevendo o nome do escolhido.
"""

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
