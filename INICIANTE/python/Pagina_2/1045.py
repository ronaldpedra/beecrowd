# beecrowd | 1045
# Tipos de Triângulos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
# Entrada
# A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

# Saída
# Imprima todas as classificações do triângulo especificado na entrada.

# Exemplos de Entrada	Exemplos de Saída
# 7.0 5.0 7.0         TRIANGULO ACUTANGULO
#                     TRIANGULO ISOSCELES

# 6.0 6.0 10.0        TRIANGULO OBTUSANGULO
#                     TRIANGULO ISOSCELES

# 6.0 6.0 6.0         TRIANGULO ACUTANGULO
#                     TRIANGULO EQUILATERO

# 5.0 7.0 2.0         NAO FORMA TRIANGULO

# 6.0 8.0 10.0        TRIANGULO RETANGULO

# Função que verifica se os tipos de trângulos que podem ser formados
def tipos_de_triangulo(lista: list):
    '''Função que retorna os triângulos que podem ser formados'''

    lista = sorted(lista)
    a = lista[2]
    b = lista[1]
    c = lista[0]

    if a >= b + c:
        print('NAO FORMA TRIANGULO')
    else:
        if a ** 2 == b ** 2 + c ** 2:
            print('TRIANGULO RETANGULO')
        if a ** 2 > b ** 2 + c ** 2:
            print('TRIANGULO OBTUSANGULO')
        if a ** 2 < b ** 2 + c ** 2:
            print('TRIANGULO ACUTANGULO')
        if a == b == c:
            print('TRIANGULO EQUILATERO')
        if (a == b != c) or (a == c != b) or (b == c != a):
            print('TRIANGULO ISOSCELES')

    return None

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(float, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    lista = dados(input())

    # Processamento dos dados
    # Retorno do pedido
    tipos_de_triangulo(lista)


if __name__ == '__main__':
    main()
