"""
beecrowd | 2653
Dijkstra
Por Abner Samuel P. Palmeira, IFSULDEMINAS BR Brazil

Timelimit: 1
No jogo O Bruxo, Sigismund Dijkstra é o líder do Serviço Secreto 
Redaniano, por causa disso ele é uma das pessoas mais importantes do 
mundo.

Além disso Dijkstra possui um grande tesouro, o qual possui diversos 
tipos de jóias.

Dijkstra está muito curioso para saber quantos tipos de jóias diferentes 
seu tesouro possui.

Sabendo que você é o melhor programador do continente Dijkstra te 
contratou para verificar quantos tipos de jóias distintas ele tem em seu 
tesouro.

Entrada
A entrada consiste de várias linhas e cada uma contém uma string que 
descreve uma das jóias de Dijkstra. Essa string é composta apenas dos 
caracteres '(' e ')', a soma do tamanho de todas as string não excede 
10^6.

Saída
Imprima quantos tipos de jóias distintas Dijkstra tem.

Exemplo de Entrada	Exemplo de Saída
((                  3
))
((
))
(
"""
joias = set()

while True:
    try:
        joia = input()
        joias.add(joia)
    except EOFError:
        break
print(len(joias))
