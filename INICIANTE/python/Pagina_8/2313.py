"""
beecrowd | 2313
Qual Triângulo
Por Alexandre A. Melo, IFSC BR Brazil

Timelimit: 1
Dados três valores, verifique se os três podem formar um triângulo. Em
caso afirmativo, verifique se ele é escaleno, isóceles ou equilátero e 
se trata-se de um triângulo retângulo ou não.

Entrada
A entrada consiste em três números inteiros A,B e C (0 < A,B,C < 105).

Saída
A saída deve conter a string "Invalido" se os valores lidos não formarem
um triângulo. Se os valores formarem um triângulo a saída deve ser
"Valido-Equilatero", "Valido-Escaleno" ou "Valido-Isoceles" de acordo
com a característica do triângulo seguido de "Retangulo: S" se o
triângulo for retângulo ou "Retangulo: N" se não for, conforme os
exemplos.

Exemplos de Entrada	Exemplos de Saída
4 6 2               Invalido
4 3 3               Valido-Isoceles
                    Retangulo: N
3 4 5               Valido-Escaleno
                    Retangulo: S
"""
def forma_triangulo(lados: list) -> None:
    """
    Dados três valores, verifique se os três podem formar um triângulo.
    """
    a = lados[0]
    b = lados[1]
    c = lados[2]

    if (a + b)  <= c:
        print('Invalido')
        return

    linha1 = 'Valido-'
    if a == b and b == c:
        linha1 += 'Equilatero'
    if (a == b and b != c) or (a != b and b == c):
        linha1 += 'Isoceles'
    if b not in (a, c):
        linha1 += 'Escaleno'
    print(linha1)

    if c**2 == a**2 + b**2:
        print('Retangulo: S')
        return

    print('Retangulo: N')


tamanho_lados = sorted(list(map(int, input().split())))
forma_triangulo(tamanho_lados)
