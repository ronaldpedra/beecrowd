"""
beecrowd | 2721
Indecisão das Renas
Por Francisco Elio Parente Arcos Filho, UEA BR Brazil

Timelimit: 1
Esse ano as Renas do papai Noel decidiram que Rudolph não seria mais 
aquele que sempre ficaria à frente. Elas escolheriam de forma justa 
entre elas quem iria encabeçar o trenó. E nada é mais justo que o acaso.

Então optaram pela seguinte forma para escolher: Cada Rena faria a 
quantidade que quisesse de bolas de neve, sem as outras verem. Depois, 
todas as bolas de neve de todas as Renas seriam reunidas em uma única e 
grande pilha. Por último, as bolas de neve seriam tiradas dessa pilha, 
uma a uma, e distribuídas entre elas sempre seguindo a ordem: Dasher, 
Dancer, Prancer, Vixen, Comet, Cupid, Donner, Blitzen e Rudolph. Até que 
se acabassem as bolas de neve. A rena que ficasse com a última bola de 
neve seria declarada vencedora e ficaria na posicão principal do trenó 
este ano.

Dado o número de bolas de neve feitas por cada Rena, determine qual Rena 
ganhou o sorteio.

Entrada
A entrada é composta por uma única linha contendo 9 números inteiros Ai 
(1 ≤ Ai ≤ 104).

Saída
A saída é composta por uma única linha contendo o nome da Rena 
vencedora.

Exemplos de Entrada	Exemplos de Saída
1 2 3 4 5 6 7 8 9   Rudolph
9 9 9 9 9 9 9 9 7   Donner
1 2 1 2 1 2 1 2 1   Vixen
"""
renas = [
    'Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 
    'Cupid', 'Donner', 'Blitzen', 'Rudolph'
    ]
total_bolas = sum(map(int, input().split()))
print(renas[(total_bolas % 9) - 1])
