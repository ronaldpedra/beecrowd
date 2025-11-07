"""
beecrowd | 2727
Código Secreto
Por Juliane Alves, UFRGS BR Brazil

Timelimit: 1
Joana gosta de brincar de fingir ser uma agente secreta com suas amigas 
Bruna, Jaqueline e Laura. Joana e Bruna criaram um código secreto para 
se comunicar sem que suas inimigas descubram seus planos.
O código secreto funciona da seguinte forma:

A letra 'a' é representada por um único ponto '.'
A letra 'b' é representada por dois pontos '..'
A letra 'c' é representada por três pontos '...'
As demais letras seguem a lógica anterior, porém cada conjunto de pontos 
está separado por um espaço e sempre com um conjunto a mais de pontos, 
como no exemplo abaixo:
. → a
.. → b
... → c
. . → d
.. .. → e
... ... → f
. . . → g
.. .. .. → h
... ... ... → i

O seu objetivo é criar um programa que decifre as mensagens secretas e 
ajudar Jaqueline e Laura descobrirem o que Joana e Bruna estão 
planejando.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada teste 
deverá conter um inteiro (N ≤ 50), que representa a quantidade de letras 
a serem decifradas e as N linhas seguintes contêm o código de cada 
letra.

Saída
Uma string representando a letra do alfabeto correspondente ao código de 
entrada. Cada string deve estar separada da outra por uma nova linha.

Exemplo de Entrada	Exemplo de Saída
2
... ... ... ... ...
... ... ...
3
... ... ... ... ...
... ... ... ...
.

o
i
o
l
a
"""
def decifrar_letra(cifra):
    """Decifra o código cifrado em uma letra do alfabeto"""

    # 1. Divide a cifra em segmentos de pontos
    # Ex: "... ... ..." -> ['...', '...', '...']
    # Ex: ".."          -> ['..']
    segmentos = cifra.split(' ')

    # 2. O número de espaços (S) é o (número de segmentos - 1)
    espacos = len(segmentos) - 1

    # 3. O número de pontos (P) é o comprimento do primeiro segmento
    #    (Já que todos os segmentos são iguais)
    pontos = len(segmentos[0])

    # 4. A fórmula é baseada no indice 0 da string de referência 
    # 'ALFABETO', por isso (pontos - 1)
    indice = (espacos * 3) + (pontos - 1)

    return ALFABETO[indice]

ALFABETO = 'abcdefghijklmnopqrstuvwxyz'

while True:
    try:
        qtd_letras = int(input())
        for _ in range(qtd_letras):
            letra_cifrada = input()
            print(decifrar_letra(letra_cifrada))
    except EOFError:
        break
