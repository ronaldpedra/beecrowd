"""
beecrowd | 2544
Kage Bunshin no Jutsu
Por Ricardo Oliveira, UFPR BR Brazil

Timelimit: 1
O Kage Bunshin no Jutsu (ou a "técnica dos clones de sombra", para os 
lusofalantes) é uma técnica milenar bastante utilizada em batalhas 
ninja.

Quando utilizada, a técnica cria uma cópia idêntica de seu usuário. 
Desta forma, se um dado ninja usa a técnica, passam a existir dois 
destes ninjas (o original e a cópia).

A técnica sempre é executada por todos os ninjas existentes no momento. 
Desta forma, se a técnica for utilizada novamente, passam a existir 
quatro ninjas idênticos ao original (os dois anteriores e mais duas 
cópias), e assim por diante.

Há N cópias de um dado ninja (incluindo o original). Sua tarefa é 
determinar quantas vezes a técnica foi utilizada.

Entrada
A entrada contém vários casos de teste. Cada caso contém uma linha com o 
número N (1 ≤ N ≤ 106). É garantido que o valor de N é tal que é 
possível obter exatamente N cópias de um ninja utilizando a técnica 
(incluindo o original).

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima uma linha contendo o número de vezes 
que a técnica foi utilizada.

Exemplo de Entrada	Exemplo de Saída
1                   0
2                   1
4                   2
"""
while True:
    try:
        ninjas = int(input())
        ninja = 1
        copias = 0
        while ninja * 2 <= ninjas:
            ninja *= 2
            copias += 1
        print(copias)

    except EOFError:
        break
