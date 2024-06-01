# beecrowd | 1101
# Sequência de Números e Soma
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

# Entrada
# O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

# Saída
# Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 5 2                   2 3 4 5 Sum=14
# 6 3                   3 4 5 6 Sum=18
# 5 0

def experiencias(conjunto_de_valores: list):
    '''Retorna os tipos de números'''

    sequencias = []

    for caso_teste in conjunto_de_valores:

        sequencia = []
        caso = sorted(caso_teste)
        soma = 0

        for i in range(caso[0], caso[1] + 1):
            sequencia.append(i)
            soma += i
            if i == caso[1]:
                sequencia.append(soma)

        sequencias.append(sequencia)

    return sequencias

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    conjunto_de_valores = []
    while True:
        caso = dados(input())
        if caso[0] <= 0 or caso[1] <= 0:
            break
        conjunto_de_valores.append(caso)

    # Processamento dos dados
    sequencias = experiencias(conjunto_de_valores)

    # Retorno do pedido
    for sequencia in sequencias:
        for i, numero in enumerate(sequencia):
            if i == len(sequencia) - 1:
                print(f'Sum={numero}')
            else:
                print(f'{numero}', end=' ')


if __name__ == '__main__':
    main()
