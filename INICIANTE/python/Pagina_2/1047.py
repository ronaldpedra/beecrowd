# beecrowd | 1047
# Tempo de Jogo com Minutos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

# Exemplo de Entrada	Exemplo de Saída
# 7 8 9 10            O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

# 7 7 7 7             O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)

# 7 10 8 9            O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)

# Função que apresenta a duração do jogo
def duracao_do_jogo(lista: list):
    '''Função que retorna a duração do jogo'''

    ini = lista[0] * 60 + lista[1] # Início do jogo
    fim = lista[2] * 60 + lista[3]

    if ini < fim:
        return divmod(fim - ini, 60)
    else:
        return divmod((fim + (24 * 60)) - ini, 60)

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    lista = dados(input())

    # Processamento dos dados
    hora, minuto = duracao_do_jogo(lista)
    # Retorno do pedido
    print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')


if __name__ == '__main__':
    main()
