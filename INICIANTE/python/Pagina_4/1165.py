# uai
#        1    2  3   4   5   6   7   8   9  10  soma algarismos
# 1           2  3       5       7              impar
# 2     11      13              17      19      par
# 3             23                      29      impar
# 4     31                      37              par
# 5     41      43              47              impar


def testar(n, primos_elementares):
    '''aqui vai o docstring'''
    ehprimo = 'é primo'
    naoehprimo = 'não é primo'

    if n in primos_elementares:
        return ehprimo

    if primos_elementares[-1] < n:
        baliza = primos_elementares[-1] + 1
        
        continua = True
        while True:
            print(baliza)
            if str(baliza)[-1] in ['1', '3', '7', '9']:
                for primo in primos_elementares:
                    print(baliza % primo)
                    if baliza % primo == 0:
                        continua = False
                if continua:
                    primos_elementares.append(baliza)
                break                    
            baliza += 1
        print(n, primos_elementares)
        testar(n, primos_elementares)
    return naoehprimo

numero = int(input())

primo_elementar = [2, 3, 5, 7, 11, 13, 17, 19, 23]
if str(numero)[-1] in ['1', '3', '7', '9']:
    print(testar(numero, primo_elementar))
else:
    print('não é primo')
