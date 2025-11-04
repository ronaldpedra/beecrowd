"""
beecrowd | 2626
Turma do JB6
Por Matheus Pimenta, UNB BR Brazil

Timelimit: 1
Dodô, Leo e Pepper passam várias madrugadas conversando, em algum lugar 
do Condomínio Jardim Botânico IV. Diversos assuntos astrais ganham pauta 
nestas conversas homéricas. Nas últimas sessões, Dodô tem falado do jogo 
de RPG que ele e Leo estão inventando, Leo (para “variar”, mas com razão) 
tem falado do gênero musical heavy metal e Pepper ficou fascinado com a 
história da mitologia grega contada por Leo.

Os garotos resolveram adotar uma estratégia para dividir as sessões 
igualmente entre os assuntos, de modo que eles possam especular cada um 
ao máximo e chegarem a conclusões astronômicas. Eles irão jogar “pedra, 
papel e tesoura” para decidir o assunto da sessão de hoje, e então irão 
alternar os assuntos nas próximas sessões. Dadas as jogadas de Dodô, Leo 
e Pepper, nesta ordem, você deve determinar o assunto da sessão de hoje.

Entrada
A entrada é composta por vários casos de teste e termina com fim de 
arquivo. Cada caso de teste é composto por uma única linha, que contém 
as jogadas de cada um dos garotos, como mostrado nos exemplos.

Saída
Para cada caso de teste, imprima uma única linha com a mensagem "Os 
atributos dos monstros vao ser inteligencia, sabedoria..." para indicar 
que Dodô é o vencedor, a mensagem "Iron Maiden's gonna get you, no 
matter how far!" para indicar que Leo é o vencedor, a mensagem "Urano 
perdeu algo muito precioso..." para indicar que Pepper é o vencedor, ou 
a mensagem "Putz vei, o Leo ta demorando muito pra jogar..." se houver 
empate.

Exemplo de Entrada	Exemplo de Saída
papel pedra pedra   Os atributos dos monstros vao ser inteligencia, sabedoria...
papel tesoura papel Iron Maiden's gonna get you, no matter how far!
pedra pedra papel   Urano perdeu algo muito precioso...
papel papel pedra   Putz vei, o Leo ta demorando muito pra jogar...
"""
def vence(jogador1, jogador2):
    """Verifica se jogador1 vence jogador2."""
    return (jogador1 + jogador2) in JOGADAS_VENCEDORAS

JOGADAS_VENCEDORAS = {'pedratesoura', 'papelpedra', 'tesourapapel'}
while True:
    try:
        dodo, leo, pepper = input().split()

        if vence(dodo, leo) and vence(dodo, pepper):
            print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif vence(leo, dodo) and vence(leo, pepper):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif vence(pepper, dodo) and vence(pepper, leo):
            print("Urano perdeu algo muito precioso...")
        else:
            print('Putz vei, o Leo ta demorando muito pra jogar...')

    except EOFError:
        break
