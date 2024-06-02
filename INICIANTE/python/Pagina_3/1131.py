# beecrowd | 1131
# Grenais
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

# - Quantos GRENAIS fizeram parte da estatística.
# - O número de vitórias do Inter.
# - O número de vitórias do Grêmio.
# - O número de Empates.
# - Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

# Entrada
# O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

# Saída
# Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 3 2                   Novo grenal (1-sim 2-nao)
# 1                     Novo grenal (1-sim 2-nao)
# 2 3                   3 grenais
# 1                     Inter:2
# 3 1                   Gremio:1
# 2                     Empates:0
#                       Inter venceu mais

# Funções Auxiliares
def resultado(resultados_dos_jogos: list):
    '''Retorna o processamento dos dados aprentados'''

    grenais = len(resultados_dos_jogos)
    inter = 0
    gremio = 0
    empates = 0
    conclusao = ''

    for jogo in resultados_dos_jogos:
        resultado_do_jogo = jogo[0] - jogo[1]
        if resultado_do_jogo == 0:
            empates += 1
        elif resultado_do_jogo > 0:
            inter += 1
        else:
            gremio += 1

    conclusao_dos_grenais = inter - gremio
    if conclusao_dos_grenais == 0:
        conclusao = 'Nao houve vencedor'
    elif conclusao_dos_grenais > 0:
        conclusao = 'Inter venceu mais'
    else:
        conclusao = 'Gremio venceu mais'

    return grenais, inter, gremio, empates, conclusao

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    resultados_dos_jogos = []

    while True:

        resultados_dos_jogos.append(dados(input()))
        print('Novo grenal (1-sim 2-nao)')
        novo_grenal = int(input())

        if novo_grenal == 1:
            continue

        break

    # Processamento dos dados
    grenais, inter, gremio, empates, conclusao = resultado(resultados_dos_jogos)

    # Retorno do pedido
    print(f'{grenais} grenais')
    print(f'Inter:{inter}')
    print(f'Gremio:{gremio}')
    print(f'Empates:{empates}')
    print(f'{conclusao}')


if __name__ == '__main__':
    main()
