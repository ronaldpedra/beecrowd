# beecrowd | 1165
# Número Primo
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

# Exemplo de Entrada	Exemplo de Saída
# 3                     8 nao eh primo
# 8                     51 nao eh primo
# 51                    7 eh primo
# 7

#        1    2  3   4   5   6   7   8   9  10  soma algarismos
# 1           2  3       5       7              impar
# 2     11      13              17      19      par
# 3             23                      29      impar
# 4     31                      37              par
# 5     41      43              47              impar

import time

n = int(input())
for i in range(0, n):
    num = int(input())
    inicio = time.time()
    if num > 9:
        s = 0
        j = 1
        while j <= num:
            if num % j == 0:
                s += 1
                if s > 2:
                    break
            j += 2
    if num <= 9:
        s = 0
        j = 1
        while j <= num:
            if num % j == 0:
                s += 1
                if s > 2:
                    break
            j += 1
    if s > 2:
        print('{} nao eh primo'.format(num))
    else:
        print('{} eh primo'.format(num))
    fim = time.time()
    print(f'{(fim - inicio):.6f}')