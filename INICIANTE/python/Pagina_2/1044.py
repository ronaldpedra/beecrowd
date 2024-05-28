# beecrowd | 1044
# Múltiplos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

# Entrada
# A entrada contém valores inteiros.

# Saída
# A saída deve conter uma das mensagens conforme descrito acima.

# Exemplo de Entrada	Exemplo de Saída
# 6 24                  Sao Multiplos

# 6 25                  Nao sao Multiplos

# Função que verifica se os números são múltiplos
def multiplos(lista: list):
    '''Função que verifica se os números são múltiplos'''

    lista = sorted(lista)

    if lista[1] % lista[0] == 0:
        return 'Sao Multiplos'

    return 'Nao sao Multiplos'

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    lista = dados(input())

    # Processamento dos dados
    resultado = multiplos(lista)

    # Retorno do pedido
    print(resultado)


if __name__ == '__main__':
    main()
