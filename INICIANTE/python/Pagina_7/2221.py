#beecrowd | 2221
#Batalha de Pomekons
#Por Gabriel Duarte, UNIFESO BR Brazil

#Timelimit: 1
#Depois de capturar muitos Pomekons, Dabriel e Guarte resolveram batalhar. A forma de duelo é simples, cada treinador coloca um Pomekon na batalha e 
# vence quem tem o Pomekon com maior valor de golpe, que é definido da seguinte maneira:

# ValorGolpe = (Ataque + Defesa) / 2 + Bonus

#O Bônus será dado ao Pomekon do treinador que estiver em um level de valor par.

#Neste problema será dado a você o valor do bônus aplicado, os valores de ataque e defesa do Pomekon de Dabriel e Guarte e seus respectivos níveis, 
# cabe a você informar o ganhador da batalha.

#Entrada
#A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T indicando o número de instâncias. Cada instância 
# começa com um inteiro B (0 ≤ B ≤ 100), que indica o valor do bônus aplicado. Nas duas linhas seguintes terão três inteiros Ai, Di e Li 
# (1 ≤ Ai, Di ≤ 100, 1 ≤ Li ≤ 50), representado o valor de ataque do Pomekon, o valor de defesa e o level do treinador. A primeira linha representa 
# o Pomekon de Dabriel e a segunda o de Guarte.

#Saída
#Para instância na entrada você deverá imprimir o nome do treinador que irá vencer a batalha, em caso de empate imprima: "Empate", sem aspas.

#Exemplo de Entrada Exemplo de Saída
#3                  Guarte
#5                  Empate
#12 23 15           Dabriel
#42 12 20
#2
#52 1 11
#1 52 1
#3
#95 12 22
#5 51 21

def calcula_ataque(bonus, ataque, defesa, level):
    valor_ataque_pokemon = (ataque + defesa) / 2
    if level % 2 == 0:
        return valor_ataque_pokemon + bonus
    return valor_ataque_pokemon

t = int(input())
instancias = []
for _ in range(t):
    instancia = []
    instancia.append(int(input())) # Bonus
    instancia.append(list(map(int, input().split()))) # Ataque Pokemon Dabriel
    instancia.append(list(map(int, input().split()))) # Ataque Pokemon Guarte
    instancias.append(instancia)

for instancia in instancias:
    # apd - Ataque Pokemon Dabriel
    # apg - Ataque Pokemon Guarte
    apd = calcula_ataque(instancia[0], instancia[1][0], instancia[1][1], instancia[1][2])
    apg = calcula_ataque(instancia[0], instancia[2][0], instancia[2][1], instancia[2][2])
    
    if apd == apg:
        print('Empate')
    if apd > apg:
        print('Dabriel')
    if apd < apg:
        print('Guarte')
