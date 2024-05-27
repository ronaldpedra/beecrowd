# beecrowd | 1038
# Lanche
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

# CODIGO    ESPECIFICAÇÃO   PREÇO
# 1         Cachorro Quente R$ 4.00
# 2         X-Salada        R$ 4.50
# 3         X-Bacon         R$ 5.00
# 4         Torrada Simples R$ 2.00
# 5         Refrigerante    R$ 1.50

# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# 3 2                 Total: R$ 10.00

# 4 3                 Total: R$ 6.00

# 2 3                 Total: R$ 13.50

# Função auxiliar para calcular o valor da conta a pagar
def conta_a_pagar(valor: list):
    '''Função que retorna o valor da conta a pagar'''

    precos = [4.0, 4.5, 5.0, 2.0, 1.5]

    return precos[(valor[0] - 1)] * valor[1]

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    valor = dados(input())

    # Processamento dos dados
    conta = conta_a_pagar(valor)

    # Retorno do pedido
    print(f'Total: R$ {conta:.2f}')


if __name__ == '__main__':
    main()
