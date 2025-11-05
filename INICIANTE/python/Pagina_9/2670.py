"""
beecrowd | 2670
Máquina de Café
Por Maratona de Programção da SBC, ACM ICPC 2017 BR Brazil

Timelimit: 1
O novo prédio da Sociedade Brasileira de Computação (SBC) possui 3 
andares. Em determinadas épocas do ano, os funcionários da SBC bebem 
muito café. Por conta disso, a presidência da SBC decidiu presentear os 
funcionários com uma nova máquina de expresso. Esta máquina deve ser 
instalada em um dos 3 andares, mas a instalação deve ser feita de forma 
que as pessoas não percam muito tempo subindo e descendo escadas.

Cada funcionário da SBC bebe 1 café expresso por dia. Ele precisa ir do 
andar onde trabalha até o andar onde está a máquina e voltar para seu 
posto de trabalho. Todo funcionário leva 1 minuto para subir ou descer 
um andar. Como a SBC se importa muito com a eficiência, ela quer 
posicionar a máquina de forma a minimizar o tempo total gasto subindo e 
descendo escadas.

Sua tarefa é ajudar a diretoria a posicionar a máquina de forma a 
minimizar o tempo total gasto pelos funcionários subindo e descendo 
escadas.

Entrada
A entrada consiste em 3 números, A1 , A2 , A3 (0 ≤ A1 , A2 , A3 ≤ 1000), 
um por linha, onde Ai representa o número de pessoas que trabalham no 
i-ésimo andar.

Saída
Seu programa deve imprimir uma única linha, contendo o número total de 
minutos a serem gastos com o melhor posicionamento possível da máquina.

Exemplos de Entrada	Exemplos de Saída
10                  80
20
30

10                  60
30
20

30                  100
10
20
"""
funcionarios_por_andar = []
for _ in range(3):
    funcionarios = int(input())
    funcionarios_por_andar.append(funcionarios)

casos = [(0, 2, 4), (2, 0, 2), (4, 2, 0)]

menor_tempo = 0
for i, caso in enumerate(casos):
    tempo = 0
    for j in range(3):
        tempo += funcionarios_por_andar[j] * caso[j]

    if i == 0:
        menor_tempo = tempo
    else:
        menor_tempo = min(menor_tempo, tempo)

print(menor_tempo)
