"""
Desafio027:
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
E.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer {}'.format(nome[0]))
print('Seu nome completo tem {} letras'.format(len(n)-n.count(' ')))
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))#para selecionar a ultima string
