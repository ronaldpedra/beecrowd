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
        # Entrada de dados
        matriz_entrada = []
        linhas, colunas = map(int, input().split())
        for _ in range(linhas):
            matriz_entrada.append(list(map(int, input().split())))

        # Cria uma matriz saída somente com 0
        matriz_saida = [[0 for _ in range(colunas)] for _ in range(linhas)]

        # Movimentos para verificação dos vizinhos
        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Percorre a matriz entrada para processamento dos dados
        for i in range(linhas):
            for j in range(colunas):
                if matriz_entrada[i][j] == 1:
                    matriz_saida[i][j] = 9
                else:

                    # Verifica os vizinhos
                    paes_em_volta = 0
                    for di, dj in movimentos:
                        viz_i, viz_j = i + di, j + dj

                        # Verifica se os vizinhos estão dentro do intervalo
                        if 0 <= viz_i < linhas and 0 <= viz_j < colunas:
                            if matriz_entrada[viz_i][viz_j] == 1:
                                paes_em_volta += 1
                    matriz_saida[i][j] = paes_em_volta

        # Imprime o resultado
        for linha in matriz_saida:
            print(''.join(map(str, linha)))

    except EOFError:
        break
