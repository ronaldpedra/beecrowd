"""
beecrowd | 2749
Saída 3
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor de programação gostaria de fazer uma tela com as 
seguintes características:

1. Ter 39 traços (-) na primeira linha;
2. Ter uma | embaixo do primeiro traço e do trigésimo nono traço da 
primeira linha, embaixo do 2o traço deve começar a escrever "x = 35" e o 
restante preencher com espaço em branco;
3. Ter uma | embaixo do primeiro traço e do trigésimo nono traço da 
primeira linha, preencher no meio com espaço em branco;
4. Ter uma | embaixo do primeiro traço e do trigésimo nono traço da 
primeira linha, embaixo do 17o traço deve começar a escrever "x = 35" e 
o restante preencher com espaço em branco;
5. Repita o procedimento 3;
6. Ter uma | embaixo do primeiro traço e do trigésimo nono traço da 
primeira linha, embaixo do 33o traço deve começar a escrever "x = 35" e 
o restante preencher no meio com espaço em branco;
7. Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
|x = 35                               |
|                                     |
|                x = 35               |
|                                     |
|                               x = 35|
--------------------------------------- (39 traços)

Entrada
Não há.

Saída
A saída será impresso conforme a figura acima.

Exemplo de Entrada	Exemplo de Saída
---------------------------------------
|x = 35                               |
|                                     |
|                x = 35               |
|                                     |
|                               x = 35|
---------------------------------------
"""
LINHAS = 7
COLUNAS = 39
TEXTOS = ['', 'x = 35', '', 'x = 35', '', 'x = 35']
for i in range(LINHAS):
    if i in (0, LINHAS - 1):
        print('-' * COLUNAS)
    elif i == 1:
        print(f"|{TEXTOS[i]:<{COLUNAS - 2}}|")
    elif i == 3:
        print(f"|{TEXTOS[i]:^{COLUNAS - 2}}|")
    elif i == 5:
        print(f"|{TEXTOS[i]:>{COLUNAS - 2}}|")
    else:
        print(f"|{' ' * (COLUNAS - 2)}|")
