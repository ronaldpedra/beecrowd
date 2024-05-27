# beecrowd | 1040
# Média 3
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

# No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

# Entrada
# A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

# Saída
# Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".

# Exemplo de Entrada	Exemplo de Saída
# 2.0 4.0 7.5 8.0     Media: 5.4
# 6.4                 Aluno em exame.
#                     Nota do exame: 6.4
#                     Aluno aprovado.
#                     Media final: 5.9

# 2.0 6.5 4.0 9.0     Media: 4.8
#                     Aluno reprovado.

# 9.0 4.0 8.5 9.0     Media: 7.3
#                     Aluno aprovado.

# Função auxiliar para calcular o resultado do aluno
def resultado_do_aluno(notas: list):
    '''Função que retorna o resultado do aluno'''

    return (notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3]) / 10

def exame_do_aluno(resultado: float, exame: float):
    '''Função que retorna o resultado do exame'''
    return (resultado + exame) / 2

def dados(entrada: str):
    '''Retorna as variáveis do usuário'''
    return list(map(float, entrada.split(' ')))

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    notas = dados(input())

    # Processamento dos dados
    resultado = resultado_do_aluno(notas)

    # Retorno do pedido
    if resultado > 6.9:
        print(f'Media: {resultado:.1f}\nAluno aprovado.')

    if resultado < 5.0:
        print(f'Media: {resultado:.1f}\nAluno reprovado.')

    if 5.0 <= resultado <= 6.9:
        print(f'Media: {resultado:.1f}\nAluno em exame.')
        exame = dados(input())[0]
        print(f'Nota do exame: {exame:.1f}')
        final = exame_do_aluno(resultado, exame)
        if final >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print(f'Media final: {final:.1f}')


if __name__ == '__main__':
    main()
