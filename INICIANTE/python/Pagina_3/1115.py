# beecrowd | 1115
# Quadrante
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

# Saída
# Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

# Exemplo de Entrada	Exemplo de Saída
# 2 2                   primeiro
# 3 -2                  quarto
# -8 -1                 terceiro
# -7 1                  segundo
# 0 2

# Funções Auxiliares
def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    # Retorno do pedido
    while True:

        ponto = dados(input())
        x = ponto[0]
        y = ponto[1]

        if x == 0 or y == 0:
            break

        if x > 0:
            if y > 0:
                print('primeiro')
            else:
                print('quarto')

        if x < 0:
            if y > 0:
                print('segundo')
            else:
                print('terceiro')


if __name__ == '__main__':
    main()
