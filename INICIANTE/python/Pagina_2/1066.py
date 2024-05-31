# beecrowd | 1066
# Pares, Ímpares, Positivos e Negativos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

# Exemplo de Entrada	Exemplo de Saída
# -5                  3 valor(es) par(es)
# 0                   2 valor(es) impar(es)
# -3                  1 valor(es) positivo(s)
# -4                  3 valor(es) negativo(s)
# 12

def tipo_dos_numeros(valores: list):
    '''Retorna os tipos de números'''
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    for valor in valores:
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1

    return pares, impares, positivos, negativos

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    valores = []
    for _ in range(5):
        valores.append(dados(input()))

    # Processamento dos dados
    pares, impares, positivos, negativos = tipo_dos_numeros(valores)

    # Retorno do pedido
    print(f'{pares} valor(es) par(es)\n{impares} valor(es) impar(es)')
    print(f'{positivos} valor(es) positivo(s)\n{negativos} valor(es) negativo(s)')

if __name__ == '__main__':
    main()
