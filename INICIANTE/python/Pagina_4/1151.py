# beecrowd | 1151
# Fibonacci Fácil
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).

# Saída
# Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

# Exemplo de Entrada	Exemplo de Saída
# 5                     0 1 1 2 3

# Funções Auxiliares
def sequencia_fibonacci(n: int):
    ''' Retorna a sequencia fibonacci '''
    sequencia = [0, 1]
    if n < 3:
        return sequencia[:n]

    for i in range(2, n):
        sequencia.append(sequencia[i - 1] + sequencia[i - 2])

    return sequencia

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    n = dados(input())

    # Processamento dos dados
    resultado = sequencia_fibonacci(n)

    # Retorno do pedido
    print(*resultado)


if __name__ == '__main__':
    main()
