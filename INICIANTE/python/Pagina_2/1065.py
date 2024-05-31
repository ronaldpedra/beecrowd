# beecrowd | 1065
# Pares entre Cinco Números
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

# Exemplo de Entrada	Exemplo de Saída
# 7                     3 valores pares
# -5
# 6
# -4
# 12

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    pares = 0
    for _ in range(5):
        valor = dados(input())
        if valor % 2 == 0:
            pares += 1

    # Retorno do pedido
    print(f'{pares} valores pares')

if __name__ == '__main__':
    main()
