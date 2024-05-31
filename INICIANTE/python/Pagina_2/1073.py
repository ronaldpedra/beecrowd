# beecrowd | 1073
# Quadrado de Pares
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

# Entrada
# A entrada contém um valor inteiro N (5 < N < 2000).

# Saída
# Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaixo.

# Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída 1e+006 ao invés de 1000000 o que ocasionará resposta errada. Neste caso, configure a precisão adequadamente para que isso não ocorra.

# Exemplo de Entrada	Exemplo de Saída
# 6                   2^2 = 4
#                     4^2 = 16
#                     6^2 = 36

def quadrado_de_pares(inteiro: int):
    '''Retorna os quadrados dos pares'''

    for i in range(1, inteiro + 1):

        if i % 2 == 0:
            print(f'{i}^2 = {i ** 2}')

    return None

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    inteiro = dados(input())

    # Processamento dos dados
    # Retorno do pedido
    quadrado_de_pares(inteiro)


if __name__ == '__main__':
    main()
