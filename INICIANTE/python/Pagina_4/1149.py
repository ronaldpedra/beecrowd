# beecrowd | 1149
# Somando Inteiros Consecutivos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

# Entrada
# A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

# Saída
# A saída contém apenas um valor inteiro.

# Exemplo de Entrada	Exemplo de Saída
# 3 2                   7

# 3 -1 0 -2 2           7

# Funções Auxiliares
def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    inteiros = dados(input())

    # Processamento dos dados
    soma = 0
    for i, n in enumerate(inteiros):

        if i == 0:
            inicio = n

        if n > 0:
            fim = inicio + n

    for j in range(inicio, fim):
        soma += j

    # Retorno do pedido
    print(soma)


if __name__ == '__main__':
    main()
