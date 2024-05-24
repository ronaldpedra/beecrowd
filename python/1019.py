# beecrowd | 1019
# Conversão de Tempo
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

# Exemplo de Entrada	Exemplo de Saída
# 556                 0:9:16

# 1                   0:0:1

# 140153              38:55:53

# Função auxiliar para calcular as horas, minutos e segundos
def hora_minuto_segundo(tempo: int):
    '''Função que retorna o número de horas, minutos e segundos'''
    hora, segundo = divmod(tempo, 3600)
    minuto, segundo = divmod(segundo, 60)

    return hora, minuto, segundo

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    tempo = dados(input())

    # Processamento dos dados
    hora, minuto, segundo = hora_minuto_segundo(tempo)

    # Retorno do pedido
    print(f'{hora}:{minuto}:{segundo}')


if __name__ == '__main__':
    main()
