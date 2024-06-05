# beecrowd | 1157
# Divisores I
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Ler um número inteiro N e calcular todos os seus divisores.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Escreva todos os divisores positivos de N, um valor por linha.

# Exemplo de Entrada	Exemplo de Saída
# 6                     1
#                       2
#                       3
#                       6

# Funções Auxiliares
def calcula_divisores(n: int):
    '''Calcula os divisores de um número'''
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta dos dados
    n = dados(input())

    # Processamento dos dados
    divisores = calcula_divisores(n)

    # Retorno do pedido
    print(*divisores, sep='\n')


if __name__ == '__main__':
    main()
