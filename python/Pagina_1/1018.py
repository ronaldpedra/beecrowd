# beecrowd | 1018
# Cédulas
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

# Exemplo de Entrada	Exemplo de Saída
# 576                 576
#                     5 nota(s) de R$ 100,00
#                     1 nota(s) de R$ 50,00
#                     1 nota(s) de R$ 20,00
#                     0 nota(s) de R$ 10,00
#                     1 nota(s) de R$ 5,00
#                     0 nota(s) de R$ 2,00
#                     1 nota(s) de R$ 1,00

# 11257               11257
#                     112 nota(s) de R$ 100,00
#                     1 nota(s) de R$ 50,00
#                     0 nota(s) de R$ 20,00
#                     0 nota(s) de R$ 10,00
#                     1 nota(s) de R$ 5,00
#                     1 nota(s) de R$ 2,00
#                     0 nota(s) de R$ 1,00

# 503                 503
#                     5 nota(s) de R$ 100,00
#                     0 nota(s) de R$ 50,00
#                     0 nota(s) de R$ 20,00
#                     0 nota(s) de R$ 10,00
#                     0 nota(s) de R$ 5,00
#                     1 nota(s) de R$ 2,00
#                     1 nota(s) de R$ 1,00

# Função auxiliar para calcular o número de notas de cada tipo
def numero_de_notas(valor: int):
    '''Função que retorna o número de notas'''
    cem, um = divmod(valor, 100)
    cinquenta, um = divmod(um, 50)
    vinte, um = divmod(um, 20)
    dez, um = divmod(um, 10)
    cinco, um = divmod(um, 5)
    dois, um = divmod(um, 2)

    return cem, cinquenta, vinte, dez, cinco, dois, um

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    valor = dados(input())

    # Processamento dos dados
    cem, cinquenta, vinte, dez, cinco, dois, um = numero_de_notas(valor)

    # Retorno do pedido
    print(f'{valor}\n{cem} nota(s) de R$ 100,00\n{cinquenta} nota(s) de R$ 50,00\n{vinte} nota(s) de R$ 20,00\n{dez} nota(s) de R$ 10,00\n{cinco} nota(s) de R$ 5,00\n{dois} nota(s) de R$ 2,00\n{um} nota(s) de R$ 1,00')


if __name__ == '__main__':
    main()
