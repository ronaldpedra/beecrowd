# beecrowd | 1142
# PUM
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N.

# Saída
# Imprima a saída conforme o exemplo fornecido.

# Exemplo de Entrada	Exemplo de Saída
# 7                     1 2 3 PUM
#                       5 6 7 PUM
#                       9 10 11 PUM
#                       13 14 15 PUM
#                       17 18 19 PUM
#                       21 22 23 PUM
#                       25 26 27 PUM

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
    n = dados(input())
    offset = 0
    for i in range(1, n + 1):
        for k in range(0, 3):
            print(k + i + offset, end=' ')
        print('PUM')
        offset += 3

if __name__ == '__main__':
    main()
