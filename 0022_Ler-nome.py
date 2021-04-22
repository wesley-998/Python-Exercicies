nome = str(input('Digite o seu nome: '))

print('O seu nome em maiúsculo: ',nome.upper())
print('O seu nome em minúsculo ', nome.lower())


nome1 = nome.replace(' ','')
print('O seu nome tem ', len(nome1), 'letras ao todo')

splitado = nome.split()
primeiro = splitado[0]
print('Seu primeiro nome tem:', len(primeiro) ,'letras')

