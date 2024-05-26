# beecrowd | 1036
# Fórmula de Bhaskara
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# Entrada
# Leia três valores de ponto flutuante (double) A, B e C.

# Saída
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

# Exemplos de Entrada	Exemplos de Saída
# 10.0 20.1 5.1       R1 = -0.29788
#                     R2 = -1.71212

# 0.0 20.0 5.0        Impossivel calcular

# 10.3 203.0 5.0      R1 = -0.02466
#                     R2 = -19.68408

# 10.0 3.0 5.0        Impossivel calcular

# Função auxiliar verificar se os valores atendem ao pedido
def bhaskara(valores: list):
    '''Função que retorna a mensagem apropriada à verificação'''
    a = valores[0]
    b = valores[1]
    c = valores[2]

    if a == 0 or (b ** 2 - 4 * a * c) < 0:
        return 'Impossivel calcular', ''

    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return x1, x2

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(float, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    valores = dados(input())

    # Processamento dos dados
    r1, r2 = bhaskara(valores)

    # Retorno do pedido
    if isinstance(r1, float):
        print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
    else:
        print(r1)


if __name__ == '__main__':
    main()
