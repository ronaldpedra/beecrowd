# beecrowd | 1174
# Seleçao em Vetor I
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

# Entrada
# A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.

# Saída
# Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# 0                     A[0] = 0.0
# -5                    A[1] = -5.0
# 63                    A[3] = -8.5
# -8.5                  ...
# ...

def main() -> None:
    '''
    Mostra todas as posições do vetor que possuem valor <= 10

    Argumentos:
        n: casos teste
    
    Retorno:
        string com o vetor
    '''

    for i in range(100):
        n = float(input())
        if n <= 10:
            print(f'A[{i}] = {n:.1f}')


if __name__ == '__main__':
    main()
