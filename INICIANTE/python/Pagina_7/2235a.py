"""
Fiz uma consulta ao Gemini para otimizar o código que escrevi 
originalmente. A seguir o resultado:

Sim, existe uma pequena otimização que podemos fazer.
Seu código já é muito rápido, então a otimização aqui é mais sobre 
reduzir o número de comparações e, para alguns, deixar o código um pouco
mais "Pythonic" (usando recursos da linguagem de forma elegante).A ideia
é ordenar os três números primeiro. Se chamarmos os números ordenados de
x, y e z (onde x menor igual y menor igual z), as verificações se tornam
mais simples:
    
    Verificar igualdade: 
        Só precisamos checar se x == y ou se y == z. Isso cobre todos os
        casos em que pelo menos dois números são iguais. 
    
    Verificar soma:
        Com os números ordenados, a única possibilidade de a soma de 
        dois ser igual a um terceiro é se x + y = z. As outras 
        combinações (x + z = y ou y + z = x) são impossíveis, pois os 
        números são positivos. 

O código otimizado ficaria assim:
"""

# Lê os valores e já os coloca em lista ordenada
numeros = sorted(list(map(int, input().split())))

# Acessa os valores ordenados. Opcional, apenas para clareza
a, b, c = numeros[0], numeros[1], numeros[2]

# Verifica as condições de forma mais concisa
if (a == b) or (b == c) or (a + b == c):
    print('S')
else:
    print('N')
