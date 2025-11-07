"""
beecrowd | 2747
Saída 1
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor de programação gostaria de fazer uma tela com as 
seguintes características:

1. Ter 39 traços (-) na primeira linha;
2. Ter uma | embaixo do primeiro traço e do trigésimo nono traço da 
primeira linha, preencher no meio com espaço em branco;
3. Repita o procedimento 2 mais quatro vezes;
4. Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
--------------------------------------- (39 traços)
Entrada
Não há.

Saída
A saída será impressa conforme a figura acima.

Exemplo de Entrada	Exemplo de Saída
---------------------------------------
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
---------------------------------------
"""
LINHAS = 7
COLUNAS = 39
for i in range(LINHAS):
    if i in (0, LINHAS - 1):
        print('-' * COLUNAS)
    else:
        print(f'|{' ' * (COLUNAS - 2)}|')

# # Sem loop for
# # Pré-calcula as duas linhas que precisamos
# LINHA_BORDA = '-' * COLUNAS
# LINHA_MEIO = f"|{' ' * (COLUNAS - 2)}|\n" # Adicionamos a quebra de linha

# # Imprime o resultado
# print(LINHA_BORDA)
# print(LINHA_MEIO * (LINHAS - 2), end='') # Multiplica a linha 5x
# print(LINHA_BORDA)
