# beecrowd | 1133
# Resto da Divisão
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

# Entrada
# O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

# Saída
# Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

# Sample Input	Sample Output
# 10              12
# 18              13
#                 17

# Funções Auxiliares
def resto_divisao(xy: list):
    '''Retorna o processamento dos dados aprentados'''

    xy = sorted(xy)

    for numero in range(xy[0] + 1, xy[1]):
        if (numero % 5 == 2) or (numero % 5 == 3):
            print(numero)

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    x = dados(input())
    y = dados(input())

    # Retorno do pedido
    # Processamento dos dados
    resto_divisao([x, y])


if __name__ == '__main__':
    main()
