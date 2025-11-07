"""
beecrowd | 2757
Entrada e Saída de Números Inteiros
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor gostaria que você fizesse um programa com as seguintes 
características:

Crie três variáveis para armazenar números inteiros;
Leia o primeiro número, que pode ser um valor na faixa de: -10000 ≤ A ≤ 
10000;
Leia o segundo número, que pode ser um valor na faixa de: 0 ≤ B ≤ 99;
Leia o terceiro número, que pode ser um valor na faixa de: 0 ≤ C ≤ 999;
Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em 
branco, o número armazenado na primeira variável, uma virgula, um espaço 
em branco, a letra B, um espaço em branco, o sinal de igual, um espaço 
em branco, o número armazenado na segunda variável, uma virgula, um 
espaço em branco, a letra C, um espaço em branco, o sinal de igual, um 
espaço em branco, o número armazenado na terceira variável. Não esqueça 
de pular linha;
Repita o procedimento 5, colocando o número em um espaçamento de 10 
dígitos e justificado a direita;
Repita o procedimento 5, colocando o número em um espaçamento de 10 
dígitos e preenchido com zeros;
Repita o procedimento 5, colocando o número em um espaçamento de 10 
dígitos e justificado a esquerda.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste 
tem três linhas. Na primeira linha tem um inteiro A (-10000 ≤ A ≤ 10000). 
Na segunda linha tem um inteiro B (0 ≤ B ≤ 99). Na terceira linha tem um 
inteiro C (0 ≤ C ≤ 999). Conforme mostrado no exemplo de entrada a 
seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de 
saída tem quatro linhas da forma descrita no item 5. Conforme mostra o 
exemplo de saída a seguir.

Exemplos de Entrada	Exemplos de Saída
1234                A = 1234, B = 12, C = 123
12                  A =       1234, B =         12, C =        123
123                 A = 0000001234, B = 0000000012, C = 0000000123
                    A = 1234      , B = 12        , C = 123

4567                A = 4567, B = 78, C = 789
78                  A =       4567, B =         78, C =        789
789                 A = 0000004567, B = 0000000078, C = 0000000789
                    A = 4567      , B = 78        , C = 789

-9991               A = -9991, B = 1, C = 1
01                  A =      -9991, B =          1, C =          1
001                 A = -000009991, B = 0000000001, C = 0000000001
                    A = -9991     , B = 1         , C = 1

"""
A = int(input())
B = int(input())
C = int(input())

print(f"A = {A}, B = {B}, C = {C}")
print(f"A = {A:>10}, B = {B:>10}, C = {C:>10}")
print(f"A = {A:010d}, B = {B:010d}, C = {C:010d}")
print(f"A = {A:<10}, B = {B:<10}, C = {C:<10}")
