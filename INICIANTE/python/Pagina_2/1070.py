# beecrowd | 1070
# Seis Números Ímpares
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

# Entrada
# A entrada será um valor inteiro positivo.

# Saída
# A saída será uma sequência de seis números ímpares.

# Exemplo de Entrada	Exemplo de Saída
# 8                   9
#                     11
#                     13
#                     15
#                     17
#                     19

def numeros_impares(valor: int):
    '''Retorna os tipos de números'''
    impares = []

    while True:

        if valor % 2 != 0:
            impares.append(valor)
        if len(impares) == 6:
            break
        valor += 1

    return impares

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    valor = dados(input())

    # Processamento dos dados
    impares = numeros_impares(valor)

    # Retorno do pedido
    print(*impares, sep='\n')


if __name__ == '__main__':
    main()
