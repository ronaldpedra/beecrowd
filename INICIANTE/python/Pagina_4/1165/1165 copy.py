# beecrowd | 1165
# Número Primo
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

# Exemplo de Entrada	Exemplo de Saída
# 3                     8 nao eh primo
# 8                     51 nao eh primo
# 51                    7 eh primo
# 7

#        1    2  3   4   5   6   7   8   9  10  soma algarismos
# 1           2  3       5       7              impar
# 2     11      13              17      19      par
# 3             23                      29      impar
# 4     31                      37              par
# 5     41      43              47              impar

'''
Que problema interessante!
Para identificar um número primo devemos dividi-lo
sucessivamente por números primos como: 2, 3, 5. . .
e verificar se a divisão é exata (em que o resto é zero)
ou não exata (onde o resto é diferente de zero).

Se o resto da divisão for zero o número não é primo.

Se nenhum resto for zero, o número é primo.

Veja mais sobre "Como reconhecer os números primos" em:
https://brasilescola.uol.com.br/matematica/como-reconhecer-os-numeros-primos.htm

1. Explicando o programa:
O programa inicia recebendo o número de casos teste a serem executados.
Dos casos teste inseridos, somente o maior executará a função carrega primos.
Esta função inicia com a lista de primos elementares.
A medida que o loop for é executado, a lista de primos elementares é acrescida dos
primos encontrados seguindo os critérios apresentados neste docstring.
Depois que a lista de primos elementares está pronta, e só fazer uma busca pelos
outros casos teste e retornar o pedido.

2. Explicando a lógica
Do estudo que fiz no site acima, concluí que todos os números primos acima de 10
possuem como último algarismo os números 1, 3, 7 e 9. Portanto, não faz sentido
testar os demais.

A seguir, para verificar se o número é primo, fazemos a sua divisão por todos os números
primos menores que ele. Caso nenhum resultado das divisões seja 0. O numero é primo.

Por fim, para maior eficiência do código, ao aplicar-se a etapa anterior, se o
quociente da divisão do caso teste pelo primo elementar da vez (no loop) for menor
que o primo divisor, o número é primo, tornando-se desnecessário testar os demais
primos da lista de primos elementares.
'''

# Funções Auxiliares
def carrega_primos(n, primos) -> list:
    '''Calcula todos os numeros primos do maior valor dos casos teste'''

    for i in range(primos[-1] + 2, n + 1, 2):
        ehprimo = True
        if str(i)[-1] == '5':
            continue
        for primo in primos:
            if i % primo == 0:
                ehprimo = False
                break
            if int(i / primo) < primo:
                break
        if ehprimo:
            primos.append(i)

    print(primos)

    return primos

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
    casos_teste = []
    n = dados(inteiro=True)
    for _ in range(n):
        casos_teste.append(dados(inteiro=True))
    maior = sorted(casos_teste)[-1]

    # Processamento dos dados
    primos_elementares = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    primos_elementares = carrega_primos(maior, primos_elementares)

    # Retorno do pedido
    for numero in casos_teste:
        if numero in primos_elementares:
            print(f'{numero} eh primo')
        else:
            print(f'{numero} nao eh primo')


if __name__ == '__main__':
    main()
