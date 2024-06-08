# beecrowd | 1175
# Troca em Vetor I
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

# Entrada
# A entrada contém 20 valores inteiros, positivos ou negativos.

# Saída
# Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

# Exemplo de Entrada	Exemplo de Saída
# 0                     N[0] = 230
# -5                    N[1] = 63
# ...                   ...
# 63                    N[18] = -5
# 230                   N[19] = 0

def main() -> None:
    '''
    Mostra todas as posições do vetor que possuem valor <= 10

    Argumentos:
        n: casos teste
    
    Retorno:
        string com o vetor
    '''
    n = [0] * 20
    for i in range(19, -1, -1):
        n[i] = int(input())

    for j in range(20):
        print(f'N[{j}] = {n[j]}')


if __name__ == '__main__':
    main()
