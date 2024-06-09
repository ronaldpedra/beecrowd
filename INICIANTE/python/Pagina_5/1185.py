# beecrowd | 1185
# Acima da Diagonal Secundária
# Por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal secundária da matriz, conforme ilustrado abaixo (área verde).




# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# S                   12.6
# 1.0
# 0.0
# -3.5
# 2.5
# 4.1
# ...

def main() -> None:
    ''' Função principal'''
    operacao = input()

    soma = 0
    divisor = 0
    for i in range(12):
        for k in range(12):
            n = float(input())
            if k < 12 - 1 - i:
                soma += n
                divisor += 1

    if operacao == 'S':
        print(f'{soma:.1f}')

    if operacao == 'M':
        print(f'{(soma / divisor):.1f}')


if __name__ == '__main__':
    main()
