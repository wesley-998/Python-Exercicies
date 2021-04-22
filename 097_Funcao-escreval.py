'''
Programa com a função escreva(), que recebe um texto, 
e cria um sublinhado de acordo com o tamanho do texto
'''

def escreval():
    print('~' * (lin +3))
    print(f' {texto}')
    print('~' * (lin +3))
def linha():
    print('__' * 50)

linha()
texto = str(input('Digite o texto: '))
lin = len(texto)

linha()
print()
print()


escreval()
