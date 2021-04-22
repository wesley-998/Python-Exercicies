'''Programa que lê a altura e o peso e calcula o IMC e diz o seu estado'''

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso/(altura*altura)

if  imc < 18.5:
    print('O seu IMC é de {:.2f}, você está abaixo do peso ideal'.format(imc))

elif  imc > 18.5 and imc < 25:
    print('O seu IMC é de {:.2f}, você está no peso ideal'.format(imc))

elif  imc > 25 and imc < 30:
    print('O seu IMC é de {:.2f}, você está sobrepeso'.format(imc))

elif  imc > 30 and imc < 40:
    print('O seu IMC é de {:.2f}, você está obeso'.format(imc))

elif imc > 40:
    print('O seu IMC é de {:.2f}, você é obeso mórbido'.format(imc))
    
