# beecrowd | 1134
# Tipo de Combustível
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

# Entrada
# A entrada contém apenas valores inteiros e positivos.

# Saída
# Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.

# Exemplo de Entrada	Exemplo de Saída
# 8                     MUITO OBRIGADO
# 1                     Alcool: 1
# 7                     Gasolina: 2
# 2                     Diesel: 0
# 2
# 4

# Funções Auxiliares
def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    alcool = 0
    gasolina = 0
    diesel = 0
    while True:
        entrada = dados(input())
        if entrada == 4:
            break
        if entrada == 1:
            alcool += 1
        if entrada == 2:
            gasolina += 1
        if entrada == 3:
            diesel += 1

    # Retorno do pedido
    print('MUITO OBRIGADO')
    print(f'Alcool: {alcool}')
    print(f'Gasolina: {gasolina}')
    print(f'Diesel: {diesel}')

if __name__ == '__main__':
    main()
