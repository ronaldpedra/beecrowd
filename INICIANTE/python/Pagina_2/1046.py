# beecrowd | 1046
# Tempo de Jogo
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

# Entrada
# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

# Saída
# Apresente a duração do jogo conforme exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 16 2                O JOGO DUROU 10 HORA(S)

# 0 0                 O JOGO DUROU 24 HORA(S)

# 2 16                O JOGO DUROU 14 HORA(S)

# Função que apresenta a duração do jogo
def duracao_do_jogo(lista: list):
    '''Função que retorna a duração do jogo'''

    ini = lista[0] # Início do jogo
    fim = lista[1]
    
    if ini < fim:
        return fim - ini
    else:
        return fim + 24 - ini

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    lista = dados(input())

    # Processamento dos dados
    duracao = duracao_do_jogo(lista)
    # Retorno do pedido
    print(f'O JOGO DUROU {duracao} HORA(S)')


if __name__ == '__main__':
    main()
