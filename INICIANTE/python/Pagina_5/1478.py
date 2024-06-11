# beecrowd | 1478
# Matriz Quadrada II
# Por Josué Pereira de Castro, Unioeste  Brasil
# Timelimit: 1
# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

# Entrada
# A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

# Saída
# Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. (os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

# Exemplo de Entrada	Exemplo de Saída
# 1
# 2
# 3
# 4
# 5
# 0

#   1

#   1   2
#   2   1

#   1   2   3
#   2   1   2
#   3   2   1

#   1   2   3   4
#   2   1   2   3
#   3   2   1   2
#   4   3   2   1

#   1   2   3   4   5
#   2   1   2   3   4
#   3   2   1   2   3
#   4   3   2   1   2
#   5   4   3   2   1

casos_teste = []

while True:
    n = int(input())
    if n > 0:
        casos_teste.append(n)
        continue
    break

for caso in casos_teste:
    for i in range(caso):
        for j in range(caso):
            if i == j:
                saida = 1
            elif i > j:
                saida = (i - j + 1)
            else:
                saida = (j - i + 1)
            if j == 0:
                print(f'{saida:>3}', end='')
            else:
                print(f'{saida:>4}', end='')
        print()
    print()
