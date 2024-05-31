# beecrowd | 1072
# Intervalo 2
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

# Entrada
# A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
# Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

# Saída
# Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

# Exemplo de Entrada	Exemplo de Saída
# 4                   2 in
# 14                  2 out
# 123
# 10
# -25

def numeros_in_out(inteiros: list):
    '''Retorna os tipos de números'''
    dentro = 0
    fora = 0

    for valor in inteiros:

        if 10 <= valor <= 20:
            dentro += 1
        else:
            fora += 1

    return dentro, fora

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
    dentro, fora = numeros_in_out(inteiros)

    # Retorno do pedido
    print(dentro, 'in')
    print(fora, 'out')


if __name__ == '__main__':
    main()
