# beecrowd | 1172
# Substituição em Vetor I
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

# Entrada
# A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

# Saída
# Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.

# Exemplo de Entrada	Exemplo de Saída
# 0                     X[0] = 1
# -5                    X[1] = 1
# 63                    X[2] = 63
# 0                     X[3] = 1
# ...                   ...

def main() -> None:
    '''
    Substitui todos os valores nulos e negativos do vetor X por 1

    Argumentos:
        n: caso teste
    
    Retorno:
        string se o número for primo ou não
    '''
    for i in range(10):
        n = int(input())
        if n <= 0:
            print(f'X[{i}] = 1')
        else:
            print(f'X[{i}] = {n}')


if __name__ == '__main__':
    main()
