"""
beecrowd | 2630
Escala de Cinza
Por Edson Alves da Costa Júnior, UNB BR Brazil

Timelimit: 1
Alguns algoritmos de processamento de imagem exigem um pré-processamento 
no qual é necessário transformar uma imagem colorida em uma imagem em 
tons de cinza. Esta conversão pode ser realizada de diversas maneiras, 
dependendo do resultado que se pretende obter.

Para preservar a percepção das cores básicas pelo olho humano, uma 
conversão apropriada seria tomar 30% da componente vermelha (R), 59% da 
componente verde (G) e 11% da componente azul (B). Em termos matemáticos,

P = 0, 30R + 0, 59G + 0, 11B

Outras abordagens possíveis seriam determinar o valor de P através da 
média aritmética das três componentes ou atribuir a P os valores da 
maior ou da menor entre as três componentes.

Dadas as componentes RGB de um pixel da imagem colorida, determine o 
valor do pixel P da imagem em tons de cinza correspondente, determinada 
a conversão a ser utilizada. Despreze a parte decimal do resultado, caso 
exista.

Entrada
A entrada em T (1 ≤ T ≤ 100) casos de teste, onde o valor de T é dado na 
primeira linha da entrada. Cada caso de teste é composto por duas linhas: 
a primeira linha contém a conversão a ser utilizada: eye para a primeira 
abordagem descrita, mean para a média aritmética, max para o valor da 
maior componente e min para o valor da menor componente. A segunda linha 
contém os valores R, G, B (0 ≤ R, G, B ≤ 255) do pixel da imagem 
colorida.

Saída
Para cada caso de testes dever ser impressa a seguinte mensagem 
"Caso #t: P", onde P é o nível de cinza do pixel da imagem em tons de 
cinza após a conversão do pixel da imagem colorida. Esta mensagem deve 
ser seguida de uma quebra de linha.

Exemplo de Entrada	Exemplo de Saída
3                   Caso #1: 35
min                 Caso #2: 88
35 70 35            Caso #3: 74
mean
10 74 181
eye
23 78 197
"""
def calcula_p(metrica, r, g, b):
    """Verifica o valor de p para conversão em escala de cinza"""
    p = 0
    if metrica == 'eye':
        p = 0.30 * r + 0.59 * g + 0.11 * b
    elif metrica == 'mean':
        p = (r + g + b) / 3
    elif metrica == 'min':
        p = min(r, g, b)
    elif metrica == 'max':
        p = max(r, g, b)
    return int(p)

casos_teste = int(input())

for i in range(casos_teste):
    conversao = input()
    r, g, b = map(int, input().split())
    print(f'Caso #{i + 1}: {calcula_p(conversao, r, g, b)}')
