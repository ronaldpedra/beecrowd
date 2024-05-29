# beecrowd | 1052
# Mês
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

# Entrada
# A entrada contém um único valor inteiro.

# Saída
# Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

# Exemplo de Entrada	Exemplo de Saída
# 4                     April

# Função que retorna o mês por extenso
def mes_por_extenso(nr_mes: int):
    '''Função que retorna o mês por extenso'''
    meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    return meses[nr_mes - 1]

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    nr_mes = dados(input())

    # Processamento dos dados
    mes = mes_por_extenso(nr_mes)

    # Retorno do pedido
    print(mes)

if __name__ == '__main__':
    main()
