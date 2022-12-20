"""
Desafio035:

"""

print('-=-'*50)
print('ANALIZADOR DE TRIÂNGULOS')
print('-=-'*50)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('-=-'*50)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo')

