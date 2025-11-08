""""
beecrowd | 2763
Entrada e Saída CPF
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor gostaria de fazer um programa com as seguintes 
características:

Leia os dados de um CPF no formato XXX.YYY.ZZZ-DD;
Imprima os quatro números, sendo um valor por linha.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste 
tem uma linha. A linha tem o seguinte formato XXX.YYY.ZZZ-DD, onde XXX, 
YYY, ZZZ, DD são números inteiros. Conforme mostrado no exemplo de 
entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de 
saída tem quatro linhas com um número inteiro em cada uma delas, 
conforme foi entrado. Conforme mostra o exemplo de saída a seguir.

Exemplos de Entrada	Exemplos de Saída
000.000.000-00      000
                    000
                    000
                    00

320.025.102-01      320
                    025
                    102
                    01
"""


def main():
    """Função principal"""
    print(input().replace('.', '\n').replace('-', '\n'))


if __name__ == '__main__':
    main()
