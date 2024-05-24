# beecrowd | 1015
# Distância Entre Dois Pontos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

# Distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# 1.0 7.0              4.4721
# 5.0 9.0

# -2.5 0.4             16.1484
# 12.1 7.3

# 2.5 -0.4             16.4575
# -12.2 7.0

# Função auxiliar para calcular a distância entre dois pontos
def distancia_entre_dois_pontos(x1: float, y1: float, x2: float, y2: float):
    '''Função que retorna o valor da distância entre dois pontos'''
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    entrada = list(map(float, entrada.split(' ')))
    return entrada[0], entrada[1]

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    x1, y1 = dados(input())
    x2, y2 = dados(input())

    # Processamento dos dados
    distancia = distancia_entre_dois_pontos(x1, y1, x2, y2)

    # Retorno do pedido
    print(f'{distancia:.4f}')


if __name__ == '__main__':
    main()
