######## CONDIÇÕES ANINHADAS ########

nome = str(input('Qual é seu nome? '))
if nome == 'Gianni':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
elif nome in 'José Mario Antonio':
    print('Que nome feio da moléstia')
else:
    print('Seu nome é bem diferente')
print('Tenha um bom dia {}'.format(nome))