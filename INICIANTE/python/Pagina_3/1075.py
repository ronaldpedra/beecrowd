# beecrowd | 1075
# Resto 2
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

# Entrada
# A entrada contém um valor inteiro N (N < 10000).

# Saída
# Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

# Exemplo de Entrada	Exemplo de Saída
# 13                  2
#                     15
#                     28
#                     41
#                     ...

def resto_dois(n: int):
    '''Retorna os tipos de números'''

    print(2)

    numeros = n
    multiplo = 1

    while True:
        
        numeros = n * multiplo + 2
        multiplo += 1
        if numeros > 10000:
            break
        print(numeros)

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    n = dados(input())
    
    # Processamento dos dados
    # Retorno do pedido
    resto_dois(n)


if __name__ == '__main__':
    main()
