# beecrowd | 1011
# Esfera
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.

# Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.

# Saída
# A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, com um espaço antes e um espaço depois da igualdade. O valor deverá ser apresentado com 3 casas após o ponto.

# Exemplos de Entrada	Exemplos de Saída
# 3                     VOLUME = 113.097

# 15                    VOLUME = 14137.155

# 1523                  VOLUME = 14797486501.627

# Função auxiliar para calcular o volume da esfera
def volume_esfera(raio: float):
    '''Função que retorna o valor do volume da esfera'''
    return (4 / 3) * 3.14159 * (raio ** 3)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    raio = float(input())

    # Processamento dos dados
    volume = volume_esfera(raio)

    # Retorno do pedido
    print(f'VOLUME = {volume:.3f}')


if __name__ == '__main__':
    main()
