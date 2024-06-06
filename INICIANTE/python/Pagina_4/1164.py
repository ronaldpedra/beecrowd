# beecrowd | 1164
# Número Perfeito
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.

# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 20), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito.

# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh perfeito” ou “X nao eh perfeito”, de acordo com a especificação fornecida.

# Exemplo de Entrada	Exemplo de Saída
# 3                     6 eh perfeito
# 6                     5 nao eh perfeito
# 5                     28 eh perfeito
# 28

# Funções Auxiliares
def numero_perfeito(n: int):
    '''Calcula os divisores de um número'''
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    if n == soma_divisores:
        return f'{n} eh perfeito'
    return f'{n} nao eh perfeito'

def dados(
        lista: bool = False,
        inteiro: bool = False,
        flutuante: bool = False,
        caracteres: bool = True
        ):
    '''Retorna a variável do usuário'''
    entrada = str(input())
    if lista:
        if inteiro:
            return list(map(int, entrada.split(' ')))
        if flutuante:
            return list(map(float, entrada.split(' ')))
        if caracteres:
            return list(map(str, entrada.split(' ')))
    else:
        if inteiro:
            return int(entrada)
        if flutuante:
            return float(entrada)
    return entrada

# Programa principal
def main():
    '''Função Principal'''

    # Coleta dos dados
    # Processamento dos dados
    # Retorno do pedido
    n = dados(inteiro=True)
    for _ in range(n):
        print(numero_perfeito(dados(inteiro=True)))


if __name__ == '__main__':
    main()
