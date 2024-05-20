# beecrowd | 1007
# Diferença
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

# Entrada
# O arquivo de entrada contém 4 valores inteiros.

# Saída
# Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

# Exemplos de Entrada	Exemplos de Saída
# 5                     DIFERENCA = -26
# 6
# 7
# 8

# 0                     DIFERENCA = -56
# 0
# 7
# 8

# 5                     DIFERENCA = 86
# 6
# -7
# 8

# Função auxiliar para calcular a diferença
def diferenca(a:int, b:int, c:int, d:int):
    return (a * b) - (c * d)

# Programa principal
def main():

    # Coleta os dados
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # Processamento dos dados
    dif = diferenca(a, b, c, d)

    # Retorno do pedido
    print(f'DIFERENCA = {dif}')


if __name__ == '__main__':
    main()
