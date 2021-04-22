'''
Programa com uma função chamada voto, que recebe o ano de nascimento como parâmetro e retorna um valor literal, 
indicando se o voto é NEGADO, OPCIONAL ou obrigatório nas eleições.
''' 
from datetime import date

def voto(ano):
    
    s = (date.today().year - ano)

    if s < 16:
        return f'Com {s} anos: Não vota!'
    
    elif 16 <= s < 18 or s >= 65 :
        return f'Com {s} anos: Voto Opcional!'
    
    elif s >= 18:
        return f'Com {s} anos: Voto Obrigatório!'
    

def linha():
    print("_" * 50)

linha()

ano = int(input('Em que ano você nasceu? '))

print(voto(ano))


linha()
