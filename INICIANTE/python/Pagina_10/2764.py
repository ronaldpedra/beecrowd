"""
beecrowd | 2764
Entrada e Saída de Data
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor gostaria de fazer um programa com as seguintes 
características:

1. Leia uma data no formato DD/MM/AA;
2. Imprima a data no formato MM/DD/AA;
3. Imprima a data no formato AA/MM/DD;
4. Imprima a data no formato DD-MM-AA.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste 
tem uma linha. A linha tem o seguinte formato DD/MM/AA onde DD, MM, AA 
são números inteiros. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de 
saída tem três linhas conforme os procedimentos 2, 3 e 4. Conforme 
mostra o exemplo de saída a seguir.

Exemplos de Entrada	Exemplos de Saída
02/08/10            08/02/10
                    10/08/02
                    02-08-10

29/07/03            07/29/03
                    03/07/29
                    29-07-03
"""
def main():
    """Função principal"""
    dia, mes, ano = input().split('/')
    print(f'{mes}/{dia}/{ano}')
    print(f'{ano}/{mes}/{dia}')
    print(f'{dia}-{mes}-{ano}')


if __name__ == '__main__':
    main()
