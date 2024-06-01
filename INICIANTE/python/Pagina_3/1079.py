# beecrowd | 1079
# Médias Ponderadas
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

# Entrada
# O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

# Saída
# Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 3                     5.7
# 6.5 4.3 6.2           6.3
# 5.1 4.2 8.1           9.3
# 8.0 9.0 10.0

def media_ponderada(conjunto_de_valores: list):
    '''Retorna os tipos de números'''

    for valores in conjunto_de_valores:

        print(f'{(((valores[0] * 2) + (valores[1] * 3) + (valores[2] * 5)) / 10):.1f}')

    return None

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(float, entrada.split()))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    conjunto_de_valores = []
    casos_teste = int(input())
    for _ in range(casos_teste):
        conjunto_de_valores.append(dados(input()))

    # Processamento dos dados
    # Retorno do pedido
    media_ponderada(conjunto_de_valores)


if __name__ == '__main__':
    main()
