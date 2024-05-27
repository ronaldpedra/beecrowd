# beecrowd | 1010
# Cálculo Simples
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# Entrada
# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

# Exemplos de Entrada	Exemplos de Saída
# 12 1 5.30             VALOR A PAGAR: R$ 15.50
# 16 2 5.10

# 13 2 15.30            VALOR A PAGAR: R$ 51.40
# 161 4 5.20

# 1 1 15.10             VALOR A PAGAR: R$ 30.20
# 2 1 15.10

# Função auxiliar para calcular o bonus do funcionário
def calcula_valor(a: float, b: float):
    '''Função que retorna o valor a ser cobrado por peça'''
    return a * b

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    peca1 = input().split(' ')
    peca2 = input().split(' ')

    # Processamento dos dados
    valor_a_pagar = calcula_valor(float(peca1[1]), float(peca1[2]))
    valor_a_pagar += calcula_valor(float(peca2[1]), float(peca2[2]))

    # Retorno do pedido
    print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')


if __name__ == '__main__':
    main()
