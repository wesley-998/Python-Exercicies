'''
Programa com uma função chamado maior que identifica 
o maior valor entre vários valores/parâmetros. 
'''
def maior(*num):
    print('Analisando os valores passados...')
    print(f'{num} Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')

def linha():
    print('__' * 50)

linha()
maior(4,6,9,8,7,4,6,5,2,9,8,7,6)
linha()
maior(6,9,8,7,4,5,1,3,6,9)
linha()
maior(5,6,9,8,7)
linha()
maior(4,1,2,)
linha()
maior(6,5)
linha()
maior(0)
linha()
