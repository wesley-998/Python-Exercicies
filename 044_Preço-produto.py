'''Programa que lê o preço de um valor e considera o preço normal e a condição de pagamento'''

preço = float(input('Qual o valor do produto? '))

opção = int(input('''Temos as seguintes opções: 
[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: Preço normal
[ 4 ] 3x ou mais no cartão 20% de juros
'''))

if opção == 1:
    valor = preço - (preço*0.10)
    print('Com 10% de desconto o novo preço do produto é {}'.format(valor))

elif opção == 2:
    valor = preço - (preço*0.05)
    print('Com 5% de desconto o novo preço do produto é {}'.format(valor))

elif opção == 3:
    print('2x no cartão, o preço do produto permanece {}'.format(preço))

elif opção == 4:
    valor = preço*1.20
    print('Em 3x ou mais no cartão o preço do produto será de {} com 20% de juros'.format(valor))
