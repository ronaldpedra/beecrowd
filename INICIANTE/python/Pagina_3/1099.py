# beecrowd | 1099
# Soma de Ímpares Consecutivos II
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

# Saída
# Imprima a soma de todos valores ímpares entre X e Y.

# Exemplo de Entrada	Exemplo de Saída
# 7                     0
# 4 5                   11
# 13 10                 5
# 6 4                   0
# 3 3                   0
# 3 5                   0
# 3 4                   12
# 3 8

def experiencias(conjunto_de_valores: list):
    '''Retorna os tipos de números'''

    resultado = []

    for caso_teste in conjunto_de_valores:
        caso = sorted(caso_teste)
        soma = 0
        for i in range(caso[0] + 1, caso[1]):
            if i % 2 != 0:
                soma += i

        resultado.append(soma)

    return resultado

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    conjunto_de_valores = []
    casos_teste = int(input())
    for _ in range(casos_teste):
        conjunto_de_valores.append(dados(input()))

    # Processamento dos dados
    resultado = experiencias(conjunto_de_valores)

    # Retorno do pedido
    print(*resultado, sep='\n')


if __name__ == '__main__':
    main()
