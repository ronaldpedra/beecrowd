# beecrowd | 1094
# Experiências
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

# Entrada
# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

# Saída
# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

# Exemplo de Entrada	Exemplo de Saída
# 10                   Total: 92 cobaias
# 10 C                 Total de coelhos: 29
# 6 R                  Total de ratos: 40
# 15 S                 Total de sapos: 23
# 5 C                  Percentual de coelhos: 31.52 %
# 14 R                 Percentual de ratos: 43.48 %
# 9 C                  Percentual de sapos: 25.00 %
# 6 R
# 8 S
# 5 C
# 14 R

def experiencias(conjunto_de_valores: list):
    '''Retorna os tipos de números'''

    total_cobaias = 0
    coelhos = 0
    ratos = 0
    sapos = 0

    for valores in conjunto_de_valores:
        match valores[1]:
            case 'C':
                coelhos += int(valores[0])
            case 'R':
                ratos += int(valores[0])
            case 'S':
                sapos += int(valores[0])

        total_cobaias += int(valores[0])

    percentual_coelhos = coelhos / total_cobaias * 100
    percentual_ratos = ratos / total_cobaias * 100
    percentual_sapos = sapos / total_cobaias * 100

    return total_cobaias, coelhos, ratos, sapos, percentual_coelhos, percentual_ratos, percentual_sapos

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return entrada.split(' ')

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    conjunto_de_valores = []
    casos_teste = int(input())
    for _ in range(casos_teste):
        conjunto_de_valores.append(dados(input()))

    # Processamento dos dados
    total_cobaias, coelhos, ratos, sapos, percentual_coelhos, percentual_ratos, percentual_sapos = experiencias(conjunto_de_valores)

    # Retorno do pedido
    print(f'Total: {total_cobaias} cobaias\nTotal de coelhos: {coelhos}')
    print(f'Total de ratos: {ratos}\nTotal de sapos: {sapos}')
    print(f'Percentual de coelhos: {percentual_coelhos:.2F} %')
    print(f'Percentual de ratos: {percentual_ratos:.2F} %')
    print(f'Percentual de sapos: {percentual_sapos:.2F} %')


if __name__ == '__main__':
    main()
