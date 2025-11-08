"""
beecrowd | 2758
Entrada e Saída de Números Reais
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor gostaria de fazer um programa com as seguintes características:

Crie duas variáveis para armazenar números reais de precisão simples;
Crie duas variáveis para armazenar números reais de precisão dupla;
Leia o primeiro número de precisão simples que sempre terá uma casa decimal;
Leia o segundo número de precisão simples que sempre terá duas casas decimais;
Leia o primeiro número de precisão dupla que sempre terá três casas decimais;
Leia o segundo número de precisão dupla que sempre terá quatro casas decimais;
Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, 
o número armazenado na primeira variável lida no passo 3, uma virgula, um 
espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço 
em branco, o número armazenado na segunda variável lida no passo 4. Não esqueça 
de pular linha;
Imprima a letra C, um espaço em branco, o sinal de igual, um espaço em branco, 
o número armazenado na primeira variável lida no passo 5, uma virgula, um 
espaço em branco, a letra D, um espaço em branco, o sinal de igual, um espaço 
em branco, o número armazenado na segunda variável lida no passo 6. Não esqueça 
de pular linha;
Repita o procedimento 7, imprimindo os números com uma casa decimal;
Repita o procedimento 8, imprimindo os números com uma casa decimal;
Repita o procedimento 7, imprimindo os números com duas casas decimais;
Repita o procedimento 8, imprimindo os números com duas casas decimais;
Repita o procedimento 7, imprimindo os números com três casas decimais;
Repita o procedimento 8, imprimindo os números com três casas decimais;
Repita o procedimento 7, imprimindo os números com três casas decimais e 
em forma de notação cientifica com o carácter E;
Repita o procedimento 8, imprimindo os números com três casas decimais e 
em forma de notação cientifica com o carácter E;
Repita o procedimento 7, imprimindo somente a parte inteira do número;
Repita o procedimento 8, imprimindo somente a parte inteira do número.
Entrada
A entrada consiste em vários arquivos de teste. Em cada arquivo de teste 
tem duas linhas. Na primeira linha tem dois números reais A e B 
(-1000.0 ≤ A, B ≤ 1000.0), separados por espaço em branco. Na segunda 
linha tem dois números reais C e D (-1000.0 ≤ C, D ≤ 1000.0), separados 
por espaço em branco. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de 
saída tem doze linhas da forma descrita no item 7 e 8. Conforme mostra o 
exemplo de saída a seguir.

Exemplos de Entrada	Exemplos de Saída
1.2 3.45            A = 1.200000, B = 3.450000
3.451 3.4516        C = 3.451000, D = 3.451600
                    A = 1.2, B = 3.5
                    C = 3.5, D = 3.5
                    A = 1.20, B = 3.45
                    C = 3.45, D = 3.45
                    A = 1.200, B = 3.450
                    C = 3.451, D = 3.452
                    A = 1.200E+00, B = 3.450E+00
                    C = 3.451E+00, D = 3.452E+00
                    A = 1, B = 3
                    C = 3, D = 3

2127.9 -821.45      A = 2127.899902, B = -821.450012
-1020.456 1352.4548 C = -1020.456000, D = 1352.454800
                    A = 2127.9, B = -821.5
                    C = -1020.5, D = 1352.5
                    A = 2127.90, B = -821.45
                    C = -1020.46, D = 1352.45
                    A = 2127.900, B = -821.450
                    C = -1020.456, D = 1352.455
                    A = 2.128E+03, B = -8.215E+02
                    C = -1.020E+03, D = 1.352E+03
                    A = 2128, B = -821
                    C = -1020, D = 1352
"""
import sys
import struct


def f32(x: float) -> float:
    """Converte para precisão simples (float32)"""
    return struct.unpack('f', struct.pack('f', x))[0]


while True:
    line1 = sys.stdin.readline()
    if not line1:
        break
    line2 = sys.stdin.readline()

    a, b = map(float, line1.split())
    c, d = map(float, line2.split())

    a = f32(a)
    b = f32(b)

    print(f'A = {a:.6f}, B = {b:.6f}')
    print(f'C = {c:.6f}, D = {d:.6f}')

    print(f'A = {a:.1f}, B = {b:.1f}')
    print(f'C = {c:.1f}, D = {d:.1f}')

    print(f'A = {a:.2f}, B = {b:.2f}')
    print(f'C = {c:.2f}, D = {d:.2f}')

    print(f'A = {a:.3f}, B = {b:.3f}')
    print(f'C = {c:.3f}, D = {d:.3f}')

    print(f'A = {a:.3E}, B = {b:.3E}')
    print(f'C = {c:.3E}, D = {d:.3E}')

    print(f'A = {a:.0f}, B = {b:.0f}')
    print(f'C = {c:.0f}, D = {d:.0f}')
