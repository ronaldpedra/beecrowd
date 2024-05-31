# beecrowd | 1071
# Soma de Impares Consecutivos I
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

# Entrada
# O arquivo de entrada contém dois valores inteiros.

# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

# Exemplo de Entrada	Exemplo de Saída
# 6                   5
# -5

# 15                  13
# 12

# 12                  0
# 12

def soma_dos_impares(inteiros: list):
    '''Retorna os tipos de números'''
    soma = 0

    for valor in range(inteiros[0] + 1, inteiros[1]):

        if valor % 2 != 0:
            soma += valor

    return soma

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    inteiros = []
    for _ in range(2):
        inteiros.append(dados(input()))

    # Processamento dos dados
    soma = soma_dos_impares(sorted(inteiros))

    # Retorno do pedido
    print(soma)


if __name__ == '__main__':
    main()
