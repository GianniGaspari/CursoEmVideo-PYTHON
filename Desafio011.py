"""
Desafio011:
Faça um programa que leia a largura e altura de uma parede em metros.
Calcule a sua área e a quantidade de tinta necessária para pintá-lo,
sabendo que cada litro de tinta, pinta uma área de 2m².
"""


larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parade tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m2.'.format(larg, alt, area))
tinta = area / 2    # 2m² = 1l == tinta = area / 2
print('Para pintar a parede, precisará de {:.2f}l de tinta.'.format(tinta))
