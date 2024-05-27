# beecrowd | 1009
# Salário com Bônus
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

# Entrada
# O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

# Saída
# Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

# Exemplos de Entrada	Exemplos de Saída
# JOAO                  TOTAL = R$ 684.54
# 500.00
# 1230.30

# PEDRO                 TOTAL = R$ 700.00
# 700.00
# 0.00

# MANGOJATA             TOTAL = R$ 1884.58
# 1700.00
# 1230.50

# Função auxiliar para calcular o bonus do funcionário
def bonus(vendas_efetuadas:float):
    '''Função que retorna o bonus do funcionário'''
    return vendas_efetuadas * 0.15

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    nome_funcionario = input()
    del nome_funcionario
    salario = float(input())
    vendas_efetuadas = float(input())

    # Processamento dos dados
    total = bonus(vendas_efetuadas) + salario

    # Retorno do pedido
    print(f'TOTAL = R$ {total:.2f}')


if __name__ == '__main__':
    main()
