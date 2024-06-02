# beecrowd | 1144
# Sequência Lógica
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

# Saída
# Imprima a saída conforme o exemplo fornecido.

# Exemplo de Entrada	Exemplo de Saída
# 5                     1 1 1
#                       1 2 2
#                       2 4 8
#                       2 5 9
#                       3 9 27
#                       3 10 28
#                       4 16 64
#                       4 17 65
#                       5 25 125
#                       5 26 126

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
    for i in range(1, n + 1):
        print(f'{i ** 1} {i ** 2} {i ** 3}')
        print(f'{i ** 1} {i ** 2 + 1} {i ** 3 + 1}')


if __name__ == '__main__':
    main()
