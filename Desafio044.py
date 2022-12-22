"""
Desafio 044:
Elabore um programa que calcule o valor a ser pago por um produtor,
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro e cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""


valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
à_vista_dinheiro_cheque = valor - (valor * 0.1)
à_vista_cartão = valor - (valor * 0.05)
cartão2x = valor
cartão3x = (valor * 0.2) + valor
opção = int(input('Opção escolhida:'))
if opção == 1:
    print('Com 10% de desconto, você irá pagar R${:.2f}'.format(à_vista_dinheiro_cheque))
elif opção == 2:
    print('Com 5% de desconto, você irá pagar R${}'.format(à_vista_cartão))
elif opção == 3:
    parcela = valor / 2
    print('2x de R${:.2f} sem juros: R${}'.format(parcela, cartão2x))
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    if parcela == 3:
        print('3x de R${:.2f} com juros de 20%. TOTAL: R${:.2f}'.format(parcela, cartão3x))
    elif parcela == 4:
        print('4x de R${:.2f} com juros de 20%. TOTAL: R${:.2f}'.format(parcela, cartão3x))
    elif parcela == 5:
        print('5x de R${:.2f} com juros de 20%. TOTAL: R${:.2f}'.format(parcela, cartão3x))
    elif parcela == 6:
        print('6x de R${:.2f} com juros de 20%. TOTAL: R${:.2f}'.format(parcela, cartão3x))
    elif parcela == 7:
        print('7x de R${:.2f} com juros de 20%. TOTAL: R${:.2f}'.format(parcela, cartão3x))
    elif parcela == 8:
        print('8x de R${:.2f} com juros de 20%. TOTAL: R${:.2f}'.format(parcela, cartão3x))
    elif parcela == 9:
        print('9x de R${:.2f} com juros de 20%. TOTAL: R${:.2f}'.format(parcela, cartão3x))
    elif parcela == 10 * (cartão3x / 10):
        print('10x de R${:.2f} com juros de 20%. TOTAL: R${:.2f}'.format(parcela, cartão3x))
else:
    total = 0
    print('\033[31mOPÇÃO INVÁLIDA\033[m de pagamento. Tente novamente!')