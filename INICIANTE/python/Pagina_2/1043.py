# beecrowd | 1043
# Triângulo
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


# Perimetro = XX.X


# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


# Area = XX.X

# Entrada
# A entrada contém três valores reais.

# Saída
# O resultado deve ser apresentado com uma casa decimal.

# Exemplo de Entrada	Exemplo de Saída
# 6.0 4.0 2.0           Area = 10.0

# 6.0 4.0 2.1           Perimetro = 12.1

# Função que verifica se forma triângulo, caso positivo retorna o perímetro, caso negativo a área do trapézio
def forma_triangulo(lista: list):
    '''
    Função que verifica se forma triângulo.
    Para que seja um triângulo os 3 testes tem que retornar true
    '''

    a = lista[0]
    b = lista[1]
    c = lista[2]

    teste1 = abs(b - c) < a < abs(b + c)
    teste2 = abs(a - c) < b < abs(a + c)
    teste3 = abs(a - b) < c < abs(a + b)

    if teste1 and teste2 and teste3:
        return f'Perimetro = {(a + b + c):.1f}'

    return f'Area = {(((a + b) * c) / 2):.1f}'

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(float, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    lista = dados(input())

    # Processamento dos dados
    resultado = forma_triangulo(lista)

    # Retorno do pedido
    print(resultado)


if __name__ == '__main__':
    main()
