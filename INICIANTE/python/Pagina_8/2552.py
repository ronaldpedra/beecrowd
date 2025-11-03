"""
beecrowd | 2552
PãodeQuejoSweeper
Por Ricardo Oliveira, UFPR BR Brazil

Timelimit: 1
Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, 
que este ano ocorrerá na cidade de Bonita Horeleninha (BH)! Nesta 
cidade, o jogo PãodeQueijoSweeper é bastante popular!

O tabuleiro do jogo consiste em uma matriz de N linhas e M colunas. Cada 
célula da matriz contém um pão de queijo ou o número de pães de queijo 
que existem nas celulas adjacentes a ela. Uma célula é adjacente a outra 
se estiver imediatamente à esquerda, à direita, acima ou abaixo da 
célula. Note que, se não contiver um pão de queijo, uma célula deve 
obrigatoriamente conter um número entre 0 e 4, inclusive.

Dadas as posições dos pães de queijo, determine o tabuleiro do jogo!

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso 
contém os inteiros N e M (1 ≤ N, M ≤ 100). As próximas N linhas contém 
M inteiros cada, separados por espaços, descrevendo os pães de queijo no 
tabuleiro. O j-ésimo inteiro da i-ésima linha é 1 se existe um pão de 
queijo na linha i e coluna j do tabuleiro, ou 0 caso contrário.

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima N linhas com M inteiros cada, não 
separados por espaços, descrevendo a configuração do tabuleiro. Se uma 
posição contém um pão de queijo, imprima 9 para ela; caso contrário, 
imprima o número cuja posição deve conter.

Exemplo de Entrada	Exemplo de Saída
4 4                 0299
0 0 1 1             1949
0 1 0 1             1393
0 0 1 0             9939
1 1 0 1             19
1 2
0 1
"""
while True:
    try:
        linhas, colunas = map(int, input().split())
        matriz = {}
        for linha in range(linhas):
            entradas = list(map(int, input().split()))
            for coluna in range(colunas):
                if entradas[coluna] == 1:
                    matriz[f'{linha}{coluna}'] = '9'
        resultado_final = []
        for linha in range(linhas):
            resultado = ''
            for coluna in range(colunas):
                if matriz.get(f'{linha}{coluna}') == '9':
                    resultado += '9'
                else:
                    paes_em_volta = 0
                    if matriz.get(f'{linha - 1}{coluna}') == '9':
                        paes_em_volta += 1
                    if matriz.get(f'{linha + 1}{coluna}') == '9':
                        paes_em_volta += 1
                    if matriz.get(f'{linha}{coluna - 1}') == '9':
                        paes_em_volta += 1
                    if matriz.get(f'{linha}{coluna + 1}') == '9':
                        paes_em_volta += 1
                    resultado += str(paes_em_volta)
            resultado_final.append(resultado)
        for linha in resultado_final:
            print(linha)

    except EOFError:
        break
