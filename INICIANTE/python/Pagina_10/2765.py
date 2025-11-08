"""
beecrowd | 2765
Entrada e Saída com Virgula
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor gostaria de fazer um programa com as seguintes 

características:

Leia uma frase que vai ter uma virgula no meio do texto;
Imprima a primeira parte da frase;
Imprima a segunda parte da frase.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste 
tem uma linha. A linha tem uma frase com no máximo 100 caracteres (pode 
ter espaço em branco) e uma virgula. Conforme mostrado no exemplo de 
entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de 
saída tem duas linhas conforme os passos 2 e 3. Conforme mostra o 
exemplo de saída a seguir.

Exemplos de Entrada	Exemplos de Saída
O URI, eh o melhor  O URI
                     eh o melhor

Bem vindo, ja vai!! Bem vindo
                     ja vai!!
"""
def main():
    """Função principal"""
    print(input().replace(',', '\n'))

if __name__ == '__main__':
    main()
