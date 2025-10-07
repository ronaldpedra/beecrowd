#beecrowd | 2203
#Tempestade de Corvos
#Por Ícaro Dantas, UFCG BR Brazil

#Timelimit: 1
#Fiddlesticks é um campeão do jogo League of Legends e tem como sua habilidade ultimate a "Tempestade de Corvos", 
# ela funciona da seguinte maneira:
#
#Primeiro Fiddlesticks escolhe um local estratégico e prontamente ele se prepara para ressurgir em uma direção até 
# uma certa distância, então ele se enraiza e canaliza a ultimate por exatamente 1.5 segundos, após esse tempo ele 
# ressurge imediatamente no local alvo com uma revoada de corvos voando ao seu redor e causando muito dano.
#
#Fiddlesticks quer sua ajuda para saber se de uma certa posição é possível atingir um invasor com sua habilidade 
# ultimate.
#
#Obs: Considere que Fiddlesticks sempre luta exatamente na direção do invasor e o invasor sempre tenta fugir na 
# direção contrária a Fiddlesticks, em velocidade constante.
#
#Entrada
#A entrada é composta de várias linhas, cada linha contém os seguintes valores inteiros: Xf, Yf, Xi, Yi, Vi, R1 e 
# R2(0 ≤ Xf, Yf, Xi, Yi, Vi, R1 e R2 ≤ 100), representando respectivamente as coordenadas de Fiddlesticks, as 
# coordenadas iniciais do invasor, a velocidade do invasor, o raio de conjuração da ultimate e o raio de voo dos corvos. 
# Considere a unidade de medida como sendo o metro.
#
#Saída
#Na saída você deve imprimir para cada linha o caractere 'Y' caso seja possível atingir o invasor ou 'N' caso contrário, 
# ambos seguidos de uma quebra de linha.
#
#Exemplo de Entrada Exemplo de Saída
#4 6 22 6 0 16 2    Y
#4 6 22 6 1 16 2    N

# Depois de tempos buscando essa solução!

def resultado(entradas):
    for entrada in entradas:
        dados = list(map(int, entrada.split()))
        xf = dados[0]
        yf = dados[1]
        xi = dados[2]
        yi = dados[3]
        vi = dados[4]
        r1 = dados[5]
        r2 = dados[6]

        # Não importa para qual sentido da reta os jogadores se movimentem, pois o alcance de ataque do fiddlesticks é sempre o mesmo R1 + R2.
        # Portanto, d é o alcance do ataque. se o inimigo deslocar uma distância menor que d ele será atingido.
        d = r1 + r2

        # Neste ponto calculamos a distancia entre o inimigo e fiddlesticks mais o deslocamento de fuga ocorrido em 1.5s (tempo de conjuração da ultimate) 
        # na velocidade informada.
        # 1. A expressão: (((xi - xf) ** 2 + (yi - yf) ** 2) ** 0.5) é a fórmula que calcula a distância entre dois pontos; e
        # 2. O cálculo da distância deslocada se dá por s = v * t (v = s/t)
        dfi = (((xi - xf) ** 2 + (yi - yf) ** 2) ** 0.5) + 1.5 * vi

        if d >= dfi:
            print('Y')
        else:
            print('N')

entradas = []

while True:
    # Armazena a entrada em uma lista de entradas.
    try:
        entrada = input()
        entradas.append(entrada)
    except EOFError:
         break

resultado(entradas)
