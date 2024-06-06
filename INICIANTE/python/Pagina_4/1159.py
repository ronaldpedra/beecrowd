# beecrowd | 1159
# Soma de Pares Consecutivos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.

# Entrada
# O arquivo de entrada contém muitos valores inteiros. O último valor do arquivo é zero.

# Saída
# Imprima a saida conforme a explicação acima e o exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 4                     40
# 11                    80
# 0

# Funções Auxiliares
def soma_cinco_pares_consecutivos(caso: int):
    '''Calcula a soma dos cinco pares consecutivos'''
    if caso % 2 == 0:
        return caso * 5 + 20

    return (caso + 1) * 5 + 20

def dados(
        lista: bool = False,
        inteiro: bool = False,
        flutuante: bool = False,
        caracteres: bool = True
        ):
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
    while True:
        n = dados(inteiro=True)
        if n == 0:
            break
        casos_teste.append(n)

    # Processamento dos dados
    # Retorno do pedido
    for caso in casos_teste:
        print(soma_cinco_pares_consecutivos(caso))


if __name__ == '__main__':
    main()
