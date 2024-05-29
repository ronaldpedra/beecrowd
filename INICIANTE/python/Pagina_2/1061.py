# Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

# Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

# Entrada
# Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

# Saída
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:

# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)

# Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

# Exemplo de Entrada	Exemplo de Saída
# Dia 5               3 dia(s)
# 08 : 12 : 23        22 hora(s)
# Dia 9               1 minuto(s)
# 06 : 13 : 23        0 segundo(s)

# Mês de Abril vai do Dia 1 ao Dia 30

# Função que calcula a duração do evento
def duracao_do_evento(lista: list):
    '''Função que retorna o cálculo da duração do evento'''

    ini = lista[0][0] * 24 * 3600 + lista[1][0] * 3600 + lista[1][1] * 60 + lista[1][2] # Início do evento em segundos
    fim = lista[2][0] * 24 * 3600 + lista[3][0] * 3600 + lista[3][1] * 60 + lista[3][2] # Fim do evento em segundos

    duracao = fim - ini

    dias, segundos = divmod(duracao, 24 * 3600)
    horas, segundos = divmod(segundos, 3600)
    minutos, segundos = divmod(segundos, 60)

    return dias, horas, minutos, segundos


def dados(lista_de_dados: list, entrada: str):
    '''Retorna as variáveis do usuário'''
    if "Dia " in entrada:
        lista_de_dados.append([int(entrada.split(' ')[1])])
    else:
        lista_de_dados.append(list(map(int, entrada.split(' : '))))

    return None

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    lista_de_dados = []
    for _ in range(4):
        dados(lista_de_dados, input())

    # Processamento dos dados
    dias, horas, minutos, segundos = duracao_do_evento(lista_de_dados)

    # Retorno do pedido
    print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')


if __name__ == '__main__':
    main()

