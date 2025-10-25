"""
beecrowd | 2493
Jogo do Operador
Por João Marcos Salvanini Bellini de Moraes, IFSULDEMINAS BR Brazil

Timelimit: 1
Samu Elmito adora criar jogos peculiares para desafiar seus amigos. 
Desta vez, ele inventou um jogo chamado "Jogo do Operador", em que ele 
cria expressões básicas e cada jogador deve escolher uma expressão e 
preencher a lacuna com o operador correto para validá-la. Os jogadores 
poderão escolher operadores de somente três tipos: adição, subtração e 
multiplicação. Porém, se o jogador achar que não há operador entre os 
três tipos que valide a expressão, poderá responder Impossível.

Sua tarefa é simples: dadas as expressões e as respostas dos jogadores, 
determinar os jogadores que não passarão para a outra fase do jogo.

Entrada
A entrada é composta por um inteiro T (2 ≤ T ≤ 50) que indica a 
quantidade de expressões e de jogadores. Cada caso de teste é composto 
por T expressões na forma "X Y=Z", indicando que X operador 
Y (0 ≤ X, Y ≤ 103) é igual a Z (-103 ≤ Z ≤ 106), seguido de T jogadores 
e suas respectivas respostas na forma "N E R", sendo N o nome do jogador 
(até 50 caracteres e sem espaços), E o índice da expressão escolhida 
(1 ≤ E ≤ T) e R a resposta (+, -, * ou I, indicando Impossível). A 
entrada termina com EOF (fim de arquivo).

Saída
Para cada caso de teste, se todos os jogadores passarem, imprima "You 
Shall All Pass!"; se nenhum jogador passar, imprima "None Shall Pass!"; 
caso contrário, imprima, em ordem lexicográfica e entre espaços, o nome 
dos jogadores que erraram a resposta e, desta forma, não passarão para a 
próxima fase do jogo.

Exemplo de Entrada	Exemplo de Saída
3                   Aline Samuel
8 4=5               None Shall Pass!
2 5=5
1 3=4
Samuel 2 +
Abner 3 +
Aline 1 *
2
1 2=-1
0 7=7
Luiz 2 -
Absolut 1 +
"""
def encontrar_respostas(testes: list) -> list:
    respostas = []
    for teste in testes:
        resultado = 'I'
        for operador in ['+', '-', '*']:
            caso_teste = teste[0].replace(' ', operador)
            if eval(caso_teste) == int(teste[1]):
                resultado = operador
                break
        respostas.append(resultado)
    return respostas

def jogo_do_operador(equacoes, participantes):
    respostas = encontrar_respostas(equacoes)
    erraram = []
    for participante in participantes:
        if participante[2] != respostas[int(participante[1]) - 1]:
            erraram.append(participante[0])
    if len(erraram) == 0:
        print('You Shall All Pass!')
    elif len(erraram) == len(participantes):
        print('None Shall Pass!')
    else:
        print(*sorted(erraram))


expressoes = []
jogadores = []
resultados_corretos = []
expressoes_jogadores = int(input())

for expressao in range(expressoes_jogadores):
    expressao = input().split('=')
    expressoes.append(expressao)
for jogador in range(expressoes_jogadores):
    jogador = input().split()
    jogadores.append(jogador)

jogo_do_operador(expressoes, jogadores)
