# beecrowd | 1179
# Preenchimento de Vetor IV
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

# Entrada
# A entrada contém 15 números inteiros.

# Saída
# Imprima a saída conforme o exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 1                     par[0] = 4
# 3                     par[1] = -4
# 4                     par[2] = 2
# -4                    par[3] = 8
# 2                     par[4] = 2
# 3                     impar[0] = 1
# 8                     impar[1] = 3
# 2                     impar[2] = 3
# 5                     impar[3] = 5
# -7                    impar[4] = -7
# 54                    impar[0] = 789
# 76                    impar[1] = 23
# 789                   par[0] = 54
# 23                    par[1] = 76
# 98                    par[2] = 98

def imprime_vetor(vetor, par=True) -> None:
    '''Imprime o pedido'''
    if par:
        for i, num in enumerate(vetor):
            print(f'par[{i}] = {num}')
    else:
        for i, num in enumerate(vetor):
            print(f'impar[{i}] = {num}')

def main() -> None:
    ''' Função principal'''
    pares = []
    impares = []
    for _ in range(15):
        n = int(input())
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
        if len(pares) == 5:
            imprime_vetor(pares)
            pares = []
        if len(impares) == 5:
            imprime_vetor(impares, par=False)
            impares = []
    imprime_vetor(impares, par=False)
    imprime_vetor(pares)


if __name__ == '__main__':
    main()
