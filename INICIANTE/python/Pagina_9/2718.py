"""
beecrowd | 2718
Luzes de Natal
Por Francisco Elio Parente Arcos Filho, UEA BR Brazil

Timelimit: 1
Giovanna adora o Natal. As festas, a família, decorações natalinas e 
principalmente os famosos pisca pisca led. Porém, esse ano a pequena Gio 
ficou triste ao perceber que seu jogo de luzes está quebrado. Algumas 
luzes ainda funcionam, outras não. Giovanna quer, obviamente, consertar 
seu objeto preferido mas não tem lâmpadas o suficiente pra substituir 
todas as queimadas então resolveu fazer o seguinte: dividir o pisca 
pisca em grupos ordenados de 50 lâmpadas e em cada grupo só consertar a 
maior quantidade de lâmpadas consecutivas queimadas.

Por serem muitos grupos, a tarefa se tornou tediosa e para tentar 
remediar isso, Giovanna, observando a semelhança dos grupos com 
representação binária de números quando imaginava lâmpadas queimadas 
como 1's e lâmpadas funcionais como 0's, decidiu pensar neles 
efetivamente como números e escreveu as representações decimais desses 
binários então tentou descobrir a quantidade de lâmpadas a serem 
trocadas a partir dessas anotações.

Sua tarefa é, dado as anotações de Gio, diga quantas lâmpadas serão 
trocadas em cada grupo.

Entrada
A primeira linha da entrada contém um número inteiro N (1 ≤ N ≤ 103) 
representando a quantidade de grupos que Giovanna anotou. As próximas N 
linhas contém um inteiro X cada uma representando o equivalente decimal 
do número que representa o grupo.

Saída
A saída consiste de N linhas cada uma contendo o tamanho da maior 
sequência de lâmpadas consecutivas queimadas em cada grupo, respeitando 
a ordem de entrada dos grupos.

Exemplos de Entrada	Exemplos de Saída
3                   2
11                  3
7                   3
23
"""
def maior_sequencia(sequencia_analizada, caractere_procurado='1'):
    """Retorna o valor da maior sequencia do caractere procurado"""
    max_sequencia = 0
    sequencia_atual = 0
    for char in sequencia_analizada:
        if char == caractere_procurado:
            sequencia_atual += 1
        else:
            max_sequencia = max(max_sequencia, sequencia_atual)
            sequencia_atual = 0
    max_sequencia = max(max_sequencia, sequencia_atual)
    return max_sequencia

grupos = int(input())
for _ in range(grupos):
    numero = int(input())
    # f'string transforma int em string binária e :b remove 0b da string
    string_binaria = f'{numero:b}'
    print(maior_sequencia(string_binaria))
