# beecrowd | 1080
# Maior e Posição
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

# Entrada
# O arquivo de entrada contém 100 números inteiros, positivos e distintos.

# Saída
# Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 2                     34565
# 113                   4
# 45
# 34565
# 6
# ...
# 8

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(float, entrada.split()))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    maior = -1
    posicao = 0
    for i in range(100):
        casos_teste = int(input())
        if casos_teste > maior:
            maior = casos_teste
            posicao = i + 1

    # Retorno do pedido
    print(f'{maior}\n{posicao}')


if __name__ == '__main__':
    main()
