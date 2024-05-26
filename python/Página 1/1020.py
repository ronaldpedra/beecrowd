# beecrowd | 1020
# Idade em Dias
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.

# Exemplo de Entrada	Exemplo de Saída
# 400                 1 ano(s)
#                     1 mes(es)
#                     5 dia(s)

# 800                 2 ano(s)
#                     2 mes(es)
#                     10 dia(s)

# 30                  0 ano(s)
#                     1 mes(es)
#                     0 dia(s)

# Função auxiliar para calcular idade em anos, meses e dias
def anos_meses_dias(idade: int):
    '''Função que retorna o número de anos, meses e dias'''
    anos, dias = divmod(idade, 365)
    meses, dias = divmod(dias, 30)

    return anos, meses, dias

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return int(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    idade = dados(input())

    # Processamento dos dados
    anos, meses, dias = anos_meses_dias(idade)

    # Retorno do pedido
    print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')


if __name__ == '__main__':
    main()
