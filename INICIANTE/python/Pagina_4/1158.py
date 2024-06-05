# beecrowd | 1158
# Soma de Ímpares Consecutivos III
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
# para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
# para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

# Saída
# Imprima a soma dos consecutivos números ímpares a partir do valor X.

# Exemplo de Entrada	Exemplo de Saída
# 2                     21
# 4 3                   24
# 11 2

# Funções Auxiliares
def soma_impares_consecutivos(caso: list):
    '''Calcula a soma dos impares consecutivos'''

    soma = 0
    impares = 0
    passo = 0
    while True:
        if impares >= caso[1]:
            break
        teste = caso[0] + passo
        if (teste) % 2 != 0:
            soma += teste
            impares += 1
        passo += 1

    return soma

def dados(lista: bool = False, inteiro: bool = False , flutuante: bool = False, caracteres: bool = True):
    '''Retorna a variável do usuário'''
    entrada = str(input())
    if lista:
        if inteiro:
            return list(map(int, entrada.split(' ')))
        if flutuante:
            return list(map(float, entrada.split(' ')))
        if caracteres:
            return list(map(str, entrada.split(' ')))
    else:
        if inteiro:
            return int(entrada)
        if flutuante:
            return float(entrada)
    return entrada
    
    

# Programa principal
def main():
    '''Função Principal'''

    # Coleta dos dados
    casos_teste = []
    n = dados(inteiro=True)
    for _ in range(n):
        casos_teste.append(dados(lista=True, inteiro=True))

    # Processamento dos dados
    # Retorno do pedido
    for caso in casos_teste:
        print(soma_impares_consecutivos(caso))


if __name__ == '__main__':
    main()
