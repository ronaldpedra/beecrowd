"""
beecrowd | 2334
Patinhos
Por Hiago Oliveira de Jesus, UEA BR Brazil

Timelimit: 1
Cinco patinhos foram passear. Além das montanhas. Para brincar. A mamãe 
gritou: quá, quá, quá, quá. Mas só quatro patinhos voltaram de lá. 
Quatro patinhos foram passear. Além das montanhas. Para brincar. A mamãe 
gritou: quá, quá, quá, quá. Mas só três patinhos voltaram de lá. Três 
patinhos foram passear. Além das montanhas. Para brincar. A mamãe 
gritou: quá, quá, quá, quá. Mas só dois patinhos voltaram de lá. Dois 
patinhos foram passear. Além das montanhas. Para brincar. A mamãe 
gritou: quá, quá, quá, quá. Mas só um patinho voltou de lá. Um patinho 
foi passear. Além das montanhas. Para brincar. A mamãe gritou: quá, quá, 
quá, quá. Mas nenhum patinho voltou de lá.

A mamãe patinha ficou tão triste naquele dia que resolveu pedir sua 
ajuda para procurar além das montanhas, na beira do mar, quantos 
patinhos não voltaram de lá.

Entrada
Haverá vários casos de testes, a primeira linha de cada caso de teste 
contém um inteiro (0 ≤ P ≤ 10**19) representando a quantidade total de 
patos, a entrada termina com P = -1.

Saída
O arquivo de saída deve conter a quantidade de patinhos que retornaram.

Exemplo de Entrada	    Exemplo de Saída
0                       0
1                       0
10000000000000000000    9999999999999999999
-1
"""
quantidade_patinhos = []

while True:
    total_patos = int(input())
    if total_patos < 0:
        break
    quantidade_patinhos.append((total_patos - 1) if total_patos != 0 else 0)

print(*quantidade_patinhos, sep='\n')
