"""Programa para aprovar o empréstimo bancário para a compra de uma casa,
    Calcule o valor da prestação mensal, 
    sabendo que ela não pode exceder 30% do salário"""

casa = float(input('Qual o valor da casa? '))
salario = int(input('Qual a sua renda mensal? '))
anos = int(input('Em quantos anos você pretende pagar a casa? '))

parcela = casa / (anos*12)
fatia = ((parcela * 100)/salario*1000)

if fatia>=30:
    print('Não podemos aprovar o seu empréstimo!')
    print('O valor da parcela corresponde a {:.0f}% do seu salário'.format(fatia))
else:
    print('O seu empréstimo foi aprovado!')
    print('O valor da sua parcela será de R$ {:.4}'.format(parcela))
    print('O valor da parcela corresponde a {:.0f}% do seu salário'.format(fatia))
