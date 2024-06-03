# beecrowd | 1145
# Sequência Lógica 2
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.

# Entrada
# O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

# Saída
# Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

# Exemplo de Entrada	Exemplo de Saída
# 3 99                  1 2 3
#                       4 5 6
#                       7 8 9
#                       10 11 12
#                       ...
#                       97 98 99

# Funções Auxiliares
def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    # Retorno do pedido
    xy = dados(input())
    x = xy[0]
    y = xy[1]

    j = 0
    for i in range(1, y + 1):
        if j == x - 1:
            print(i)
            j = 0
        else:
            print(i, end=' ')
            j += 1


if __name__ == '__main__':
    main()
