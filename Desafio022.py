"""
Desafio022:

"""

n = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(n.upper()))
print('Seu nome em minúsculas é: {}'.format(n.lower()))
print('Seu nome tem ao todo: {} letas'.format(len(n)-n.count(' ')))
#print('Seu primeiro nome tem: {} letras'.format(n.find(' ')))
s = n.split()
print('Seu primeiro nome é {} e tem {} letras'.format(s[0], len(s[0])))
