# beecrowd | 1117
# Validação de Nota
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

# Entrada
# A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

# Saída
# Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
# Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# -3.5                  nota invalida
# 3.5                   nota invalida
# 11.0                  media = 6.75
# 10.0

# Funções Auxiliares
def dados(entrada: str):
    '''Retorna a variável do usuário'''
    return float(entrada)

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    # Processamento dos dados
    # Retorno do pedido
    notas = []

    while True:

        if len(notas) == 2:
            break

        nota = dados(input())
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print('nota invalida')

    print(f'media = {((notas[0] + notas[1]) / 2):.2f}')


if __name__ == '__main__':
    main()
