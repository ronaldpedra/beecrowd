# beecrowd | 1013
# O Maior
# Adaptado por Neilor Tonin, beecrowd  Brasil

# Timelimit: 1
# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

# MaiorAB = (a + b + abs(a - b)) / 2

# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

# Exemplos de Entrada	Exemplos de Saída
# 7 14 106              106 eh o maior

# 217 14 6              217 eh o maior

# Função auxiliar para apresentar o maior valor
def maior_ab(a: int, b: int):
    '''Função que retorna o numero de maior'''
    return int((a + b + abs(a - b)) / 2)

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    entrada = list(map(int, entrada.split(' ')))
    return entrada[0], entrada[1], entrada[2]


# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    entrada = input()
    a, b, c = dados(entrada)

    # Processamento dos dados
    maior = maior_ab(a, b)
    maior = maior_ab(maior, c)

    # Retorno do pedido
    print(f'{maior} eh o maior')
    

if __name__ == '__main__':
    main()
