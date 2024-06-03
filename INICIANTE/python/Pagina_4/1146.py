# beecrowd | 1146
# Sequências Crescentes
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 2
# Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero). Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor.

# Obs: cuide para não deixar espaço em branco após o último valor apresentado na linha ou você receberá Presentation Error.

# Entrada
# O arquivo de entrada contém vários números inteiros. O último número no arquivo de entrada é 0.

# Saída
# Para cada número N do arquivo de entrada deve ser impressa uma linha de 1 até N, conforme o exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

# Exemplo de Entrada	Exemplo de Saída
# 5                     1 2 3 4 5
# 10                    1 2 3 4 5 6 7 8 9 10
# 3                     1 2 3
# 0

# Funções Auxiliares
def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    # Retorno do pedido
    while True:
        sequencia = dados(input())
        if sequencia:
            for i in range(1, sequencia + 1):
                if i == 1:
                    print(i, end='')
                else:
                    print(f' {i}', end='')
            print()
        else:
            break


if __name__ == '__main__':
    main()
