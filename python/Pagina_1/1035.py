# beecrowd | 1035
# Teste de Seleção 1
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

# Entrada
# Quatro números inteiros A, B, C e D.

# Saída
# Mostre a respectiva mensagem após a validação dos valores.

# Exemplo de Entrada	Exemplo de Saída
# 5 6 7 8             Valores nao aceitos

# 2 3 2 6             Valores aceitos

# Função auxiliar verificar se os valores atendem ao pedido
def verifica_valores(valores: int):
    '''Função que retorna a mensagem apropriada à verificação'''
    a = valores[0]
    b = valores[1]
    c = valores[2]
    d = valores[3]

    if b > c and d > a and (c + d) > (a + b) and c >= 0 <= d and a % 2 == 0:
        return 'Valores aceitos'

    return 'Valores nao aceitos'

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(int, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    valores = dados(input())

    # Processamento dos dados
    mensagem = verifica_valores(valores)

    # Retorno do pedido
    print(mensagem)


if __name__ == '__main__':
    main()
