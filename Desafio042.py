"""
Desafio042:
Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓCELES: dois lados iguais
- ESCALENO: todos os lados diferentes
"""


l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Os segmentos acima PODEM FORMAR um Triângulo ', end='')
    if l1 == l2 and l2 == l3:
        print('EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
            print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')