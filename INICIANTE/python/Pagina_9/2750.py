"""
beecrowd | 2750
Saída 4
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor de programação gostaria que você fizesse um programa com 
as seguintes características:

1. Criar 16 variáveis inteiras;
2. Atribuir a elas valores de 0 a 15 a cada um das variáveis anteriores;
3. Ter 39 traços (-) na primeira linha;
4. Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo 
terceiro e do trigésimo nono traço da primeira linha, embaixo do 4o 
traço deve começar a escrever “decimal”, embaixo do 16o traço deve 
começar a escrever “octal”, embaixo do 26o traço deve começar a escrever 
“Hexadecimal” e o restante preencher com espaço em branco;
5. Repita o procedimento 3;
6. Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo 
terceiro e do trigésimo nono traço da primeira linha, embaixo do 8o 
traço deve imprimir o valor da primeira variável em valor decimal, 
embaixo do 18o traço deve imprimir o valor da primeira variável em 
valor octal, embaixo do 31o traço deve imprimir o valor da primeira 
variável em valor hexadecimal e o restante preencher com espaço em 
branco;
7. Repita o procedimento 6 para as outras 15 variáveis;
8. Repita o procedimento 3.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
| decimal   |  octal  |  Hexadecimal  |
---------------------------------------
|      0    |    0    |       0       |
|      1    |    1    |       1       |
|      2    |    2    |       2       |
|      3    |    3    |       3       |
|      4    |    4    |       4       |
|      5    |    5    |       5       |
|      6    |    6    |       6       |
|      7    |    7    |       7       |
|      8    |   10    |       8       |
|      9    |   11    |       9       |
|     10    |   12    |       A       |
|     11    |   13    |       B       |
|     12    |   14    |       C       |
|     13    |   15    |       D       |
|     14    |   16    |       E       |
|     15    |   17    |       F       |
--------------------------------------- (39 traços)
Entrada
Não há.

Saída
A saída será impressa conforme a figura acima.

Exemplo de Entrada	Exemplo de Saída
---------------------------------------
| decimal   |  octal  |  Hexadecimal  |
---------------------------------------
|      0    |    0    |       0       |
|      1    |    1    |       1       |
|      2    |    2    |       2       |
|      3    |    3    |       3       |
|      4    |    4    |       4       |
|      5    |    5    |       5       |
|      6    |    6    |       6       |
|      7    |    7    |       7       |
|      8    |   10    |       8       |
|      9    |   11    |       9       |
|     10    |   12    |       A       |
|     11    |   13    |       B       |
|     12    |   14    |       C       |
|     13    |   15    |       D       |
|     14    |   16    |       E       |
|     15    |   17    |       F       |
---------------------------------------
"""
COLUNAS = 39
CABECALHO_RODAPE = f"{'-' * COLUNAS}"
THEAD = f"|{'decimal':^{11}}|{'octal':^{9}}|{'Hexadecimal':^{15}}|"
print(CABECALHO_RODAPE)
print(THEAD)
print(CABECALHO_RODAPE)
for i in range(16):
    TBODY = f"|{i:>{7}}{' ' * 4}|{oct(i)[2:]:>{5}}{' ' * 4}|{hex(i)[2:].upper():^{15}}|"
    print(TBODY)
print(CABECALHO_RODAPE)
