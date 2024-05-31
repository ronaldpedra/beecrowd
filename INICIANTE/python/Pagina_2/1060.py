# beecrowd | 1060
# Números Positivos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

# Entrada
# Seis valores, negativos e/ou positivos.

# Saída
# Imprima uma mensagem dizendo quantos valores positivos foram lidos.

# Exemplo de Entrada	Exemplo de Saída
# 7                     4 valores positivos
# -5
# 6
# -3.4
# 4.6
# 12

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return float(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    positivos = 0
    for _ in range(6):
        valor = dados(input())
        if valor > 0:
            positivos += 1

    # Retorno do pedido
    print(f'{positivos} valores positivos')

if __name__ == '__main__':
    main()
