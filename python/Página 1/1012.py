# beecrowd | 1012
# Área
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.
# Entrada
# O arquivo de entrada contém três valores com um dígito após o ponto decimal.

# Saída
# O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

# Exemplos de Entrada	Exemplos de Saída
# 3.0 4.0 5.2           TRIANGULO: 7.800
#                       CIRCULO: 84.949
#                       TRAPEZIO: 18.200
#                       QUADRADO: 16.000
#                       RETANGULO: 12.000

# 12.7 10.4 15.2        TRIANGULO: 96.520
#                       CIRCULO: 725.833
#                       TRAPEZIO: 175.560
#                       QUADRADO: 108.160
#                       RETANGULO: 132.080

# Função auxiliar para calcular o volume da esfera
def area_triangulo(a: float, c: float):
    '''Função que retorna a área do triângulo'''
    return a * c / 2

def area_circulo(c: float):
    '''Função que retorna a área do círculo'''
    return 3.14159 * (c ** 2)

def area_trapezio(a: float, b: float, c: float):
    '''Função que retorna a área do trapézio'''
    return (a + b) * c / 2

def area_quadrado(b: float):
    '''Função que retorna a área do quadrado'''
    return b ** 2

def area_retangulo(a: float, b: float):
    '''Função que retorna a área do retângulo'''
    return a * b

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    entrada = list(map(float, entrada.split(' ')))
    return entrada[0], entrada[1], entrada[2]


# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    entrada = input()
    a, b, c = dados(entrada)

    # Processamento dos dados
    triangulo = area_triangulo(a, c)
    circulo = area_circulo(c)
    trapezio = area_trapezio(a, b, c)
    quadrado = area_quadrado(b)
    retangulo = area_retangulo(a, b)

    # Retorno do pedido
    print(f'TRIANGULO: {triangulo:.3f}')
    print(f'CIRCULO: {circulo:.3f}')
    print(f'TRAPEZIO: {trapezio:.3f}')
    print(f'QUADRADO: {quadrado:.3f}')
    print(f'RETANGULO: {retangulo:.3f}')


if __name__ == '__main__':
    main()
