# beecrowd | 1114
# Senha Fixa
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

# Entrada
# A entrada é composta por vários casos de testes contendo valores inteiros.

# Saída
# Para cada valor lido mostre a mensagem correspondente à descrição do problema.

# Exemplo de Entrada	Exemplo de Saída
# 2200                  Senha Invalida
# 1020                  Senha Invalida
# 2022                  Senha Invalida
# 2002                  Acesso Permitido

# Funções Auxiliares
# None

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    # Retorno do pedido
    while True:
        senha = input()
        match senha:
            case '2002':
                print('Acesso Permitido')
                break
            case _:
                print('Senha Invalida')


if __name__ == '__main__':
    main()
