# beecrowd | 1048
# Aumento de Salário
# Por Neilor Tonin, URI BR Brasil

# Timelimit: 1
# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


# Salário	Percentual de Reajuste
# 0 - 400.00
# 400.01 - 800.00
# 800.01 - 1200.00
# 1200.01 - 2000.00
# Acima de 2000.00

# 15%
# 12%
# 10%
# 7%
# 4%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 400.00              Novo salario: 460.00
#                     Reajuste ganho: 60.00
#                     Em percentual: 15 %

# 800.01              Novo salario: 880.01
#                     Reajuste ganho: 80.00
#                     Em percentual: 10 %

# 2000.00             Novo salario: 2140.00
#                     Reajuste ganho: 140.00
#                     Em percentual: 7 %

# Função que calcula o novo salário do funcionário
def novo_salario(salario: float):
    '''Função que retorna o novo salário do funcionário'''
    match salario:
        case salario if 0 <= salario <= 400.00:
            percentual = 15
        case salario if 400.01 <= salario <= 800.00:
            percentual = 12
        case salario if 800.01 <= salario <= 1200.00:
            percentual = 10
        case salario if 1200.01 <= salario <= 2000.00:
            percentual = 7
        case salario if salario >= 2000.01:
            percentual = 4

    reajuste = salario * (percentual / 100)
    salario_reajustado = salario + reajuste

    return salario_reajustado, reajuste, percentual

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return float(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    salario = dados(input())

    # Processamento dos dados
    salario_reajustado, reajuste, percentual = novo_salario(salario)

    # Retorno do pedido
    print(f'Novo salario: {salario_reajustado:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {percentual} %')


if __name__ == '__main__':
    main()
