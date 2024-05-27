# beecrowd | 1042
# Sort Simples
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

# Entrada
# A entrada contem três números inteiros.

# Saída
# Imprima a saída conforme foi especificado.

# Exemplo de Entrada	Exemplo de Saída
# 7 21 -14            -14
#                     7
#                     21

#                     7
#                     21
#                     -14

# -14 21 7            -14
#                     7
#                     21

#                     -14
#                     21
#                     7

# Função que imprime a lista ordenada crescente
def imprime_ordenada(lista: list):
    '''Função que imprime uma lista ordenada crescente'''

    for elemento in sorted(lista):
        print(elemento)

    return None

def imprime_lista_original(lista: list):
    '''Função que imprime uma lista'''

    for elemento in lista:
        print(elemento)

    return None

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    lista = dados(input())

    # Processamento dos dados
    # direto no retorno do pedido

    # Retorno do pedido
    imprime_ordenada(lista)
    print()
    imprime_lista_original(lista)


if __name__ == '__main__':
    main()
