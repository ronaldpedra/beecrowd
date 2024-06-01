# beecrowd | 1098
# Sequencia IJ 4
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
#                       I=0 J=1
#                       I=0 J=2
#                       I=0 J=3
#                       I=0.2 J=1.2
#                       I=0.2 J=2.2
#                       I=0.2 J=3.2
#                       .....
#                       I=2 J=?
#                       I=2 J=?
#                       I=2 J=?

for i in range(0, 22, 2):
    for j in range(1, 4):
        print(f'I={str(i / 10).replace(".0", "")} J={str(j + (i / 10)).replace(".0", "")}')
