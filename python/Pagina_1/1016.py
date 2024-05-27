# beecrowd | 1016
# Distância
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

# Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.

# Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.

# Entrada
# O arquivo de entrada contém um número inteiro.

# Saída
# Imprima o tempo necessário seguido da mensagem "minutos".

# Exemplo de Entrada	Exemplo de Saída
# 30                    60 minutos

# 110                   220 minutos

# 7                     14 minutos

# Função auxiliar para calcular o tempo que leva para o carro Y se distanciar km do carro X
def tempo_necessario(km: int):
    '''Função que retorna o tempo para atingir a distância'''
    return km * 2

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    distancia = dados(input())

    # Processamento dos dados
    tempo = tempo_necessario(distancia)

    # Retorno do pedido
    print(f'{tempo} minutos')


if __name__ == '__main__':
    main()
