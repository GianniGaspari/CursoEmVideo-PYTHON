'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('carro novo' if tempo<=3 else'carro velho')
print('--FIM--')'''

'''nome = str(input('Qual o seu nome? '))
if nome == 'Gianni':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal')
print('Bom dia {}'.format(nome))'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('Sua média é: {:.1f}'.format(m))
if m >=6:
    print('Acima da média! Parabéns!!!')
else:
    print('Que vacilo hein. Estude mais da proxima vez')
    
