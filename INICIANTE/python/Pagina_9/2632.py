"""
beecrowd | 2632
Magic and Sword
Por Edson Alves da Costa Júnior, UNB BR Brazil

Timelimit: 1
No tower defense Magic and Sword, o jogador pode lançar magias de área 
para derrotar as unidades inimigas. As magias são elementais: fogo, água, 
ar e terra, e a região afetada é determinada por um círculo cujo raio 
depende do nível da magia.

A tabela abaixo lista cada magia, o dano e o respectivo raio por nível:



As unidades inimigas são delimitadas por um retângulo de largura w e 
altura h, com canto inferior esquerdo posicionado no ponto (x0, y0). O 
inimigo sofrerá dano caso seu retângulo delimitador tenha qualquer 
intercessão com a área deﬁnida pelo círculo da magia.

Dada a posição e o retângulo delimitador da unidade inimiga, o centro da 
explosão e o identiﬁcador e o nível da magia, determine o dano sofrido 
pela unidade. Caso a unidade esteja fora do alcance da magia, o dano 
sofrido é igual a zero.

Entrada
A entrada consiste em T (1 ≤ T ≤ 1000) casos de teste, onde o valor de T 
é informado na primeira linha da entrada. Cada caso de teste é composto 
por duas linhas. A primeira contém quatro número inteiros que 
representam as dimensões w e h (1 ≤ w, h ≤ 1000) do retângulo e as 
coordenadas x0 e y0 (0 ≤ x0, y0 ≤ 1000) do canto inferior esquerdo. A 
segunda linha do caso de teste contém uma string com o identiﬁcador da 
magia (ﬁre para fogo, water para água, earth para terra e air para ar), 
o nível N desta magia (1 ≤ N ≤ 3) e as coordenadas cx e cy 
(0 ≤ cx, cy ≤ 1000) do centro da área da explosão.

Saída
Para cada caso de teste, a saída deve ser o valor do dano recebido pela 
unidade, seguido de uma quebra de linha.

Exemplo de Entrada	Exemplo de Saída
4                   0
10 10 50 50         200
fire 1 85 55        300
10 10 50 50         100
fire 2 85 55
10 10 50 100
water 3 100 100
10 10 50 100
air 3 100 100
"""
def clamp(n, min_val, max_val):
    """
    Limita o número 'n' entre um específico 'min_val' e máximo 'max_val'.
    """
    return max(min(n, max_val), min_val)

def intersecao(x_min, y_min, x_max, y_max, cx, cy, r):
    """Verifica a interseção de duas áreas"""
    px = clamp(cx, x_min, x_max)
    py = clamp(cy, y_min, y_max)
    distancia = ((cx - px) ** 2) + ((cy - py) ** 2)
    return distancia <= (r ** 2)

tabela_magias = {
    'fire': {
        'dano': 200,
        '1': 20,
        '2': 30,
        '3': 50
    },
    'water': {
        'dano': 300,
        '1': 10,
        '2': 25,
        '3': 40
    },
    'earth': {
        'dano': 400,
        '1': 25,
        '2': 55,
        '3': 70
    },
    'air': {
        'dano': 100,
        '1': 18,
        '2': 38,
        '3': 60
    },
}
casos_teste = int(input())
for _ in range(casos_teste):
    # ini - inimigo, w - width, h - heigth, (x, y) - posição inicial
    ini_w, ini_h, min_x, min_y = map(int, input().split())
    max_x = min_x + ini_w
    max_y = min_y + ini_h

    # (cx, cy) - coordenadas do centro da explosão
    magia, nivel, centro_x, centro_y = input().split()

    # Conversão de tipos
    centro_x = int(centro_x)
    centro_y = int(centro_y)

    # Busca dados de magia
    info_magia = tabela_magias[magia]
    raio = info_magia[nivel]
    dano = info_magia['dano']

    if intersecao(min_x, min_y, max_x, max_y, centro_x, centro_y, raio):
        print(dano)
    else:
        print(0)
