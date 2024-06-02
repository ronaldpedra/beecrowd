# beecrowd | 1132
# Múltiplos de 13
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

# Entrada
# O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

# Saída
# Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.

# Sample Input	Sample Output
# 100           13954
# 200

# Funções Auxiliares
def soma_numeros(xy: list):
    '''Retorna o processamento dos dados aprentados'''

    soma = 0
    xy = sorted(xy)

    for numero in range(xy[0], xy[1] + 1):
        if numero % 13 != 0:
            soma += numero

    return soma

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    x = dados(input())
    y = dados(input())

    # Processamento dos dados
    soma = soma_numeros([x, y])

    # Retorno do pedido
    print(soma)


if __name__ == '__main__':
    main()
