# beecrowd | 1074
# Par ou Ímpar
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.

# Entrada
# A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste. Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

# Saída
# Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.

# Exemplo de Entrada	Exemplo de Saída
# 4                   ODD NEGATIVE
# -5                  NULL
# 0                   ODD POSITIVE
# 3                   EVEN NEGATIVE
# -4

def par_ou_impar(inteiros: list):
    '''Retorna os tipos de números'''

    for valor in inteiros:
        
        if valor == 0:
            print('NULL')
            continue
        if valor % 2 == 0:
            print('EVEN ', end='')
        else:
            print('ODD ', end='')
        if valor > 0:
            print('POSITIVE')
        else:
            print('NEGATIVE')

    return None

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    inteiros = []
    casos_teste = int(input())
    for _ in range(casos_teste):
        inteiros.append(dados(input()))

    # Processamento dos dados
    # Retorno do pedido
    par_ou_impar(inteiros)


if __name__ == '__main__':
    main()
