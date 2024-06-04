# beecrowd | 1153
# Fatorial Simples
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

# Entrada
# A entrada contém um valor inteiro N (0 < N < 13).

# Saída
# A saída contém um valor inteiro, correspondente ao fatorial de N.

# Exemplo de Entrada	Exemplo de Saída
# 4                     24

# Funções Auxiliares
def fatorial(n: int):

    if n <= 1:
        return 1

    return n * fatorial(n - 1)

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta dos dados
    n = dados(input())

    # Processamento dos dados
    # Retorno do pedido
    print(fatorial(n))


if __name__ == '__main__':
    main()
