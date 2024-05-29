# beecrowd | 1051
# Imposto de Renda
# Por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

# Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

# Renda                         Imposto de Renda
# de 0.00 a R$ 2000.00          Isento
# de R$ 2000.01 a R$ 3000.00    8%
# de R$ 3000.01 a R$ 4500.00    18%
# acima de 4500.00              28%

# Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".

# Exemplos de Entrada	Exemplos de Saída
# 3002.00             R$ 80.36

# 1701.12             Isento

# 4520.00             R$ 355.60

# Função que calcula o imposto de reda da pessoa
def imposto_de_renda(salario: float):
    '''Função que retorna o valor do imposto de renda'''
    tabela_imposto = [0, 2000, 3000, 4500]
    percentual = [0, 8, 18, 28]
    imposto = 0
    base_calculo = 0

    for i in range(len(tabela_imposto)):
        if i == len(tabela_imposto) - 1:
            base_calculo = salario - tabela_imposto[i]
            imposto += base_calculo * percentual[i] / 100

            return imposto
        else:
            if tabela_imposto[i] < salario <= tabela_imposto[i + 1]:
                base_calculo = salario - tabela_imposto[i]
                imposto += base_calculo * percentual[i] / 100

                return imposto
            else:
                base_calculo = tabela_imposto[i + 1] - tabela_imposto[i]
                imposto += base_calculo * percentual[i] / 100        
    
    return None

def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return float(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    salario = dados(input())

    # Processamento dos dados
    imposto = imposto_de_renda(salario)

    # Retorno do pedido
    if imposto == 0:
        print('Isento')
    else:
        print(f'R$ {imposto:.2f}')

if __name__ == '__main__':
    main()
