"""
beecrowd | 2761
Entrada e Saída de Vários Tipos
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor gostaria de fazer um programa com as seguintes 
características:

1. Crie uma variável inteira;
2. Crie uma variável real de simples precisão;
3. Crie uma variável que armazene um carácter;
4. Crie uma variável que armazene uma frase de no máximo 50 caracteres;
5. Leia todas as variáveis na ordem da forma criada;
8. Imprima todas as variáveis como foram lidas;
9. Imprima as variáveis, separando-as por uma tabulação (8 espaços), na 
ordem que foram lidas;
10. Imprima as variáveis com exatos 10 espaços.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste 
tem uma linha. A linha tem uma variável A que armazena um número inteiro, 
uma variável B que armazena um número real, uma variável C com um 
carácter e uma variável D que armazena uma frase de no máximo 50 
caracteres. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de 
saída tem três linhas da forma descrita nos itens 6, 7 e 8. Conforme 
mostra o exemplo de saída a seguir. Imprima os valores de ponto 
flutuante com 6 casas decimais após a vírgula.

Exemplos de Entrada	        Exemplos de Saída
12 3.141560 a Uri online    123.141560aUri online
                            12 3.141560 a Uri online
                            12 3.141560 a Uri online

791 123.141568 | aaa        791123.141571|aaa
                            791 123.141571 | aaa
                            791123.141571 | aaa

791123.141571|aaa
791123.141571|aaa

791	123.141571	|	aaa
791     123.141571      |       aaa

       791123.141571         |       aaa
       791123.141571         |       aaa   


"""
import struct


def f32(x: float) -> float:
    """Converte para precisão simples (float32)"""
    return struct.unpack('f', struct.pack('f', x))[0]

def main():
    """Função principal"""
    inteiro, virgula, caractere, texto = input().split(maxsplit=3)
    virgula = f'{f32(float(virgula)):.6f}'

    print(f'{inteiro}{virgula}{caractere}{texto}')
    print(f'{inteiro}\t{virgula}\t{caractere}\t{texto}')
    print(f'{inteiro:>10}{virgula:>10}{caractere:>10}{texto:>10}')


if __name__ == '__main__':
    main()