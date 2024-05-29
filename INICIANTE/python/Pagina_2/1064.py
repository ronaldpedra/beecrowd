# beecrowd | 1064
# Positivos e Média
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

# Entrada
# A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

# Saída
# O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

# Exemplo de Entrada	Exemplo de Saída
# 7                   4 valores positivos
# -5                  7.4
# 6
# -3.4
# 4.6
# 12

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return float(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    positivos = 0
    media = 0
    for _ in range(6):
        valor = dados(input())
        if valor > 0:
            positivos += 1
            media += valor

    media = media / positivos

    # Retorno do pedido
    print(f'{positivos} valores positivos\n{media:.1f}')

if __name__ == '__main__':
    main()

