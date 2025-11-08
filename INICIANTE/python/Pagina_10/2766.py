"""
beecrowd | 2766
Entrada e Saída Lendo e Pulando Nomes
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor gostaria de fazer um programa com as seguintes 
características:

Leia 10 nomes, sem espaço em branco;
Imprima o terceiro nome da lista;
Imprima o sétimo nome da lista;
Imprima o nono nome da lista.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste 
tem dez linhas. Em cada linha tem um nome de no máximo 30 caracteres e 
sem espaço em branco. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de 
saída tem três linhas conforme os procedimentos 2, 3 e 4. Conforme 
mostra o exemplo de saída a seguir.

Exemplos de Entrada	Exemplos de Saída
USP                 UFCG
UFPE                ITA
UFCG                URI
UFRN
UFRJ
IME
ITA
UNIOESTE
URI
UFG

UnB                 UNIFEI
UFMG                UFRGS
UNIFEI              UFU
UECE
UNICAMP
INATEL
UFRGS
UNIFESO
UFU
PUC
"""
def main():
    """Função principal"""
    nomes = [input() for _ in range(10)]
    print(nomes[2])
    print(nomes[6])
    print(nomes[8])


if __name__ == '__main__':
    main()
