"""
beecrowd | 2486
C Mais ou Menos?
Por João Marcos Salvanini Bellini de Moraes, IFSULDEMINAS BR Brazil

Timelimit: 1
Ultimamente, diversas pessoas estão indo à Dra. Cláudia Café com Leite 
para saber se estão consumindo a quantidade recomendada diária de 
vitamina C. Isso tem a deixado exausta, e por isso ela lhe pediu para 
escrever um programa que, dado o consumo diário de alimentos ricos em 
vitamina C por uma pessoa, indique o quanto essa pessoa deve consumir a 
mais ou a menos para atingir o recomendado.

Para tal, você poderá utilizar a tabela a seguir:

Alimentos ricos em Vitamina C	Quantidade de Vitamina C
suco de laranja	                120 mg
morango fresco	                85 mg
mamao	                        85 mg
goiaba vermelha	                70 mg
manga	                        56 mg
laranja	                        50 mg
brocolis	                    34 mg

Considere que o consumo diário recomendado de vitamina C está entre 110 
mg e 130 mg, inclusive.

Entrada
Cada caso de teste é composto um inteiro T (1 ≤ T ≤ 7) indicando que a 
pessoa consome diariamente T alimentos entre os 7 alimentos da tabela. 
Em seguida, haverá T linhas com um inteiro N e um alimento (totalmente 
em caixa baixa e sem acentuações), indicando que a pessoa consome uma 
quantidade N daquele alimento. A entrada termina com T = 0.

Saída
Para cada caso de teste (T), se o consumo ultrapassou o limite 
recomendado, imprima "Menos X mg", em que X representa a quantidade a 
menos a ser consumida para atingir o limite recomendado; se o consumo 
não atingiu o recomendado, imprima "Mais X mg", em que X representa a 
quantidade a mais para atingir o recomendado; se o consumo está dentro 
do intervalo recomendado, imprima "X mg", em que X representa a 
quantidade consumida diariamente pela pessoa.

Exemplo de Entrada	Exemplo de Saída
2                   Menos 365 mg
2 suco de laranja   Mais 8 mg
3 mamao             Mais 4 mg
1                   120 mg
3 brocolis
2
1 manga
1 laranja
1
1 suco de laranja
0
"""
TABELA_ALIMENTOS = {
    'suco de laranja': 120, 
    'morango fresco': 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34
    }
MIN_RECOMENDADO_VIT_C, MAX_RECOMENDADO_VIT_C = 110, 130
# ----------------------------------------------------------------------

def imprimir_diagnostico(vit_c_consumida: int) -> None:
    """
    Compara o consumo com os limites recomendados e imprime a mensagem
    apropriada.
    """
    if vit_c_consumida < MIN_RECOMENDADO_VIT_C:
        print(f'Mais {MIN_RECOMENDADO_VIT_C - vit_c_consumida} mg')
    elif vit_c_consumida > MAX_RECOMENDADO_VIT_C:
        print(f'Menos {vit_c_consumida - MAX_RECOMENDADO_VIT_C} mg')
    else:
        print(f'{vit_c_consumida} mg')


while True:
    try:
        # Lê o número de alimentos
        t = int(input())

        # Condição de parada t = 0
        if not t:
            break
        
        vitamina_c_total = 0
        for _ in range(t):
            qtd_str, alimento = input().split(' ', maxsplit=1)
            vitamina_c_total += int(qtd_str) * TABELA_ALIMENTOS[alimento]
        
        imprimir_diagnostico(vitamina_c_total)
    
    except EOFError:
        break
