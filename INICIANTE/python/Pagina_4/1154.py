# beecrowd | 1154
# Idades
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

# Entrada
# A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

# Saída
# A saída contém um valor correspondente à média de idade dos indivíduos.

# A média deve ser impressa com dois dígitos após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# 34                    39.25
# 56
# 44
# 23
# -2

# Funções Auxiliares
def media(idades: list):
    '''Calcula a média das idades de uma lista'''

    return sum(idades) / len(idades)

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta dos dados
    idades = []
    while True:
        idade = dados(input())
        if idade < 0:
            break
        idades.append(idade)

    # Processamento dos dados
    # Retorno do pedido
    print(f'{media(idades):.2f}')


if __name__ == '__main__':
    main()
