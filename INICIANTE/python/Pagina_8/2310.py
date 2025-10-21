"""
beecrowd | 2310
Voleibol
Por Leonardo Fernandes, IFSC BR Brazil

Timelimit: 1
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe.
A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e 
ataques cada um de seus jogadores fez, bem como quantos desses saques, 
bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa 
deve mostrar qual o percentual de saques, bloqueios e ataques do time todo 
tiveram sucesso.

Entrada
A entrada é dada pelo número de jogadores N (1 ≤ N ≤ 100), seguido pelo 
nome de cada um dos jogadores. Abaixo do nome de cada jogador, seguem duas 
linhas com três inteiros cada. Na primeira linha S, B e A (0 ≤ S,B,A ≤ 10000) 
representam a quantidade de tentativas de saques, bloqueios e ataques e 
na segunda linha, S1, B1 e A1 (0 ≤ S1 ≤ S; 0 ≤ B1 ≤ B; 0 ≤ A1 ≤ A) com o 
número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

Saída
A saída deve conter o percentual total de saques, bloqueios e ataques do 
time todo que resultaram em pontos, conforme mostrado no exemplo.

Exemplo de Entrada	Exemplo de Saída
3                   Pontos de Saque: 19.05 %.
Renan               Pontos de Bloqueio: 63.33 %.
10 20 12            Pontos de Ataque: 75.00 %.
1 10 9
Jonas
8 7 1
2 7 0
Edson
3 3 3
1 2 3
"""
def resultado_em_pontos(total_tentado: list, total_acertos: list) -> None:
    """
    Esta função imprime o percentual total de saques, bloqueios e ataques
    do time todo que resultaram em pontos.
    """
    print(f'Pontos de Saque: {\
        ((total_acertos[0] / total_tentado[0]) * 100):.2f} %.')
    print(f'Pontos de Bloqueio: {\
        ((total_acertos[1] / total_tentado[1]) * 100):.2f} %.')
    print(f'Pontos de Ataque: {\
        ((total_acertos[2] / total_tentado[2]) * 100):.2f} %.')

numero_de_jogadores: int = int(input())

# Total de Tentativas e Acertos:
# [0] -> Saques, [1] -> Bloqueios e [2] -> Ataques
tentativas = [0, 0, 0]
acertos = [0, 0, 0]

for _ in range(numero_de_jogadores):

    nome = input()

    entrada_tentativa = list(map(int, input().split()))
    tentativas[0] += entrada_tentativa[0]
    tentativas[1] += entrada_tentativa[1]
    tentativas[2] += entrada_tentativa[2]

    entrada_acertos = list(map(int, input().split()))
    acertos[0] += entrada_acertos[0]
    acertos[1] += entrada_acertos[1]
    acertos[2] += entrada_acertos[2]

resultado_em_pontos(tentativas, acertos)
