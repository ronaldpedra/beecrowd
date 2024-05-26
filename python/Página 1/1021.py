# beecrowd | 1021
# Notas e Moedas
# Por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.

# Exemplo de Entrada	Exemplo de Saída
# 576.73              NOTAS:
#                     5 nota(s) de R$ 100.00
#                     1 nota(s) de R$ 50.00
#                     1 nota(s) de R$ 20.00
#                     0 nota(s) de R$ 10.00
#                     1 nota(s) de R$ 5.00
#                     0 nota(s) de R$ 2.00
#                     MOEDAS:
#                     1 moeda(s) de R$ 1.00
#                     1 moeda(s) de R$ 0.50
#                     0 moeda(s) de R$ 0.25
#                     2 moeda(s) de R$ 0.10
#                     0 moeda(s) de R$ 0.05
#                     3 moeda(s) de R$ 0.01

# 4.00                NOTAS:
#                     0 nota(s) de R$ 100.00
#                     0 nota(s) de R$ 50.00
#                     0 nota(s) de R$ 20.00
#                     0 nota(s) de R$ 10.00
#                     0 nota(s) de R$ 5.00
#                     2 nota(s) de R$ 2.00
#                     MOEDAS:
#                     0 moeda(s) de R$ 1.00
#                     0 moeda(s) de R$ 0.50
#                     0 moeda(s) de R$ 0.25
#                     0 moeda(s) de R$ 0.10
#                     0 moeda(s) de R$ 0.05
#                     0 moeda(s) de R$ 0.01

# 91.01               NOTAS:
#                     0 nota(s) de R$ 100.00
#                     1 nota(s) de R$ 50.00
#                     2 nota(s) de R$ 20.00
#                     0 nota(s) de R$ 10.00
#                     0 nota(s) de R$ 5.00
#                     0 nota(s) de R$ 2.00
#                     MOEDAS:
#                     1 moeda(s) de R$ 1.00
#                     0 moeda(s) de R$ 0.50
#                     0 moeda(s) de R$ 0.25
#                     0 moeda(s) de R$ 0.10
#                     0 moeda(s) de R$ 0.05
#                     1 moeda(s) de R$ 0.01

# Função auxiliar para calcular o número de notas e moedas de cada tipo
def numero_de_notas_moedas(valor: int):
    '''Função que retorna o número de notas e moedas'''

    notas, moedas = divmod(valor, 1)
    notas = int(notas)
    moedas = int(moedas * 100)

    cem, um = divmod(notas, 100)
    cinquenta, um = divmod(um, 50)
    vinte, um = divmod(um, 20)
    dez, um = divmod(um, 10)
    cinco, um = divmod(um, 5)
    dois, um = divmod(um, 2)

    cinquenta_centavos, um_centavo = divmod(moedas, 50)
    vintecinco_centavos, um_centavo = divmod(um_centavo, 25)
    dez_centavos, um_centavo = divmod(um_centavo, 10)
    cinco_contavos, um_centavo = divmod(um_centavo, 5)

    return int(cem), int(cinquenta), int(vinte), int(dez), int(cinco), int(dois), int(um), int(cinquenta_centavos), int(vintecinco_centavos), int(dez_centavos), int(cinco_contavos), int(um_centavo)

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return float(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    valor = dados(input())

    # Processamento dos dados
    cem, cinquenta, vinte, dez, cinco, dois, um, cinquenta_centavos, vintecinco_centavos, dez_centavos, cinco_contavos, um_centavo = numero_de_notas_moedas(valor)

    # Retorno do pedido
    print('NOTAS:')
    print(f'{cem} nota(s) de R$ 100.00\n{cinquenta} nota(s) de R$ 50.00\n{vinte} nota(s) de R$ 20.00\n{dez} nota(s) de R$ 10.00\n{cinco} nota(s) de R$ 5.00\n{dois} nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(f'{um} moeda(s) de R$ 1.00\n{cinquenta_centavos} moeda(s) de R$ 0.50\n{vintecinco_centavos} moeda(s) de R$ 0.25\n{dez_centavos} moeda(s) de R$ 0.10\n{cinco_contavos} moeda(s) de R$ 0.05\n{um_centavo} moeda(s) de R$ 0.01')


if __name__ == '__main__':
    main()
