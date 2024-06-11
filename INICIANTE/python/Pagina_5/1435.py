# beecrowd | 1435
# Matriz Quadrada I
# Adaptado por Josué P. de Castro  Brasil
# Timelimit: 2
# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

# Entrada
# A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

# Saída
# Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

# Exemplo de Entrada	Exemplo de Saída
# 1
# 2
# 3
# 4
# 5
# 0

#   1

#   1   1
#   1   1

#   1   1   1
#   1   2   1
#   1   1   1

#   1   1   1   1
#   1   2   2   1
#   1   2   2   1
#   1   1   1   1

#   1   1   1   1   1
#   1   2   2   2   1
#   1   2   3   2   1
#   1   2   2   2   1
#   1   1   1   1   1

casos_teste = []

while True:
    n = int(input())
    if n > 0:
        casos_teste.append(n)
        continue
    break

for caso in casos_teste:
    # Usando a lógica da menor distância da borda

    for i in range(caso):
        for j in range(caso):

            # Calcula a distância da borda em cada direção
            esquerda = j
            direita = (caso - 1) - j
            cima = i
            embaixo = (caso - 1) - i

            # Verifica qual é a menor distância da borda e acrescenta 1 para atender ao pedido
            menor = sorted([esquerda, direita, cima, embaixo])[0] + 1

            # Retorna o pedido com tamanho 3 para todas as saídas
            if j == 0:
                print(f'{menor:>3}', end='')
            else:
                print(f'{menor:>4}', end='')
        print()
    print()
