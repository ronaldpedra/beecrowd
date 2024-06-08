# beecrowd | 1156
# Sequência S II
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
# S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# A saída contém um valor correspondente ao valor de S.
# O valor deve ser impresso com dois dígitos após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída

# Funções Auxiliares
# None

# Programa principal
def main():
    '''Função Principal'''

    # Coleta dos dados
    # None

    # Processamento dos dados
    soma = 0
    contagem = 0
    for i in range(1, 40, 2):

        soma += i / 2 ** contagem
        contagem += 1

    # Retorno do pedido
    print(f'{soma:.2f}')


if __name__ == '__main__':
    main()
