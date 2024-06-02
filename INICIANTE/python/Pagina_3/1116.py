# beecrowd | 1116
# Dividindo X por Y
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 2
# Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

# Entrada
# A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

# Saída
# Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

# Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

# Exemplo de Entrada	Exemplo de Saída
# 3                     -1.5
# 3 -2                  divisao impossivel
# -8 0                  0.0
# 0 8

# Funções Auxiliares
def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    # Retorno do pedido

    qtd_casos_teste = int(input())

    for _ in range(qtd_casos_teste):
        caso = dados(input())
        try:
            resultado = caso[0] / caso[1]
            print(f'{resultado:.1f}')
        except ZeroDivisionError:
            print('divisao impossivel')


if __name__ == '__main__':
    main()
