# beecrowd | 1050
# DDD
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

# 61  Brasilia
# 71  Salvador
# 11  Sao Paulo
# 21  Rio de Janeiro
# 32  Juiz de Fora
# 19  Campinas
# 27  Vitoria
# 31  Belo Horizonte

# Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
# DDD nao cadastrado

# Entrada
# A entrada consiste de um único valor inteiro.

# Saída
# Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.

# Exemplo de Entrada	Exemplo de Saída
# 11                    Sao Paulo

# Função que retorna a cidade pelo ddd
def cidade_pelo_ddd(ddd: int):
    '''Função que retorna a cidade'''

    ddd_cidades = {
        61: 'Brasilia',
        71: 'Salvador',
        11: 'Sao Paulo',
        21: 'Rio de Janeiro',
        32: 'Juiz de Fora',
        19: 'Campinas',
        27: 'Vitoria',
        31: 'Belo Horizonte'}

    return ddd_cidades.get(ddd, 'DDD nao cadastrado')

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal


def main():
    '''Função Principal'''

    # Coleta os dados
    ddd = dados(input())

    # Processamento dos dados
    cidade = cidade_pelo_ddd(ddd)

    # Retorno do pedido
    print(cidade)


if __name__ == '__main__':
    main()
