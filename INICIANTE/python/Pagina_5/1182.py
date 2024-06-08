# beecrowd | 1182
# Coluna na Matriz
# Por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser considerados na operação.

# Entrada
# A primeira linha de entrada contem um número C (0 ≤ C ≤ 11) indicando a coluna que será considerada para operação. A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# 5                     12.6
# S
# 0.0
# -3.5
# 2.5
# 4.1
# ...
lines = []
with open('./INICIANTE/stdin', 'r', encoding='utf-8') as stdin_file:
    for line in stdin_file:
        lines.append(line.replace('\n', ''))

def main() -> None:
    ''' Função principal'''
    coluna = int(input())
    operacao = input()

    soma = 0
    for _ in range(12):
        for k in range(12):
            n = float(input())
            if k == coluna:
                soma += n

    if operacao == 'S':
        print(f'{soma:.1f}')

    if operacao == 'M':
        print(f'{(soma / 12):.1f}')


if __name__ == '__main__':
    main()
