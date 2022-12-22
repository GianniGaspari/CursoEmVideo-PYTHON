"""
Desafio 042:
Desenvolva uma logica que leia o peso e altura de uma pessoa
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: ABAIXO DO PESO
- Entre 18.5 e 25: PESO IDEAL
- 25 até 30: SOBREPESO
- 30 até 40: OBESIDADE
- Acima de 40: OBESIDADE MÓRBIDA
"""


p = float(input('Peso(Kg): '))
a = float(input('Altura(m): '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu IMC é {:.1f}\n\033[31mABAIXO DO PESO\033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f}\n\033[34mPESO IDEAL\033[m'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}\n\033[31mSOBREPESO\033[m'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}\n\033[31mOBESIDADE\033[m'.format(imc))
else:
    print('Seu IMC é {:.1f}\nOBESIDADE MORBIDA'.format(imc))
