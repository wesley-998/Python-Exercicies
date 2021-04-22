
salario = int(input('Qual o seu salário?? '))

if salario > 1250:
    aumento = salario * 1.10
    print('O seu salário recebeu um aumento de 10% ficando é {:.2f}'.format(aumento))

elif salario < 1250:
    aumento1 = salario * 1.15
    print('O seu salário recebeu um aumento de 15% ficando é {:.2f}'.format(aumento1))

else:
    print('else') 

    