"""
beecrowd | 2724
Ajude Patatatitu
Por Felipe C. Ochial, URI BR Brazil

Timelimit: 1
Juvenal comportou-se muito bem este ano, já que gosta muito de química e 
queria muito ganhar um kit Alquimia. Entretanto, Juvenal pediu para 
incluir alguns elementos perigosos em seu kit. Seu Noel não podendo 
negar o pedido ( afinal, como dizer não para a criança mais bem 
comportada do planeta?) pediu para o pobre elfo Patatatitu garantir que 
o presente fosse seguro.

Patatatitu sabe muito sobre química, e conhece todos os compostos 
perigosos que podem ser feitos com os elementos disponíveis no kit de 
Juvenal. Assim, decidiu enviar um cd junto com o presente, contendo um 
programa que afira a segurança dos experimentos de Juvenal. Todos 
concordam que a criança mais bem-comportada do planeta nunca faria uma 
experiência sem antes checar sua segurança conforme as instruções. 
Porém Patatatitu não sabe programar e está atrás de ajuda. Você poderia 
ajudá-lo?

Para facilitar, Patatatitu explica que um composto perigoso é formado a 
partir da mistura de elementos na ordem de sua fórmula atômica e 
respeitando as devidas proporções. Neste kit de química é possível 
apenas adicionar um elemento por vez, em diferentes quantidades. Assim 
para formar trifluoreto de cloro (ClF3), um composto muito perigoso, 
deve-se adicionar um átomo cloro (Cl) e três de flúor (F3), 
independentemente do que for adicionado antes ou depois. ClF4 não é um 
composto perigoso, pois está fora de proporção. De forma similar caso 
Mg2F seja um composto perigoso, Mg2Fe será seguro, visto que flúor (F) 
é um elemento distinto de ferro (Fe).

Entrada
A entrada consiste de um inteiro N (0 < N < 10) que indica o número de 
casos de teste. Cada caso de teste consiste em um inteiro T (0 < T < 51) 
que indica o número de compostos perigosos possíveis, caso os elementos 
sejam incluídos na ordem e proporções mostradas. Seguem T linhas, cada 
uma contendo uma string de até 50 caracteres representando uma formula 
que gera um composto perigoso caso os elementos sejam misturados na 
ordem e proporções que são apresentados. Após isso, é dado um inteiro U 
(0 < U < 51) que indica a quantia de experiencias que Juvenal irá 
realizar. Seguem U linhas cada uma contendo uma string de até 50 
caracteres representando os elementos que Juvenal utilizara na ordem e 
proporções em que serão adicionados.

Saída
A saída consiste de U linhas por caso de teste, as quais devem informar 
se Juvenal deve prosseguir ou abortar o  U-ésimo  experimento do caso 
teste. Caso deva abortar imprima "Abortar", caso seja seguro imprima 
"Prossiga".Deixe uma linha em branco entre cada caso de teste.

Exemplo de Entrada
3
3
KH2O
C3H5N3O9
ClF3
5
WOsFNeSeBrSnAsNOH4C12CuKZrBr
C8H10N4O2C2H7NO3SC6H5NO2
C3H5N3O9ClF3KH20
C3H5N3O9
4P12Si7CNF12BLiClF312ON12H
2
H20NaCl
C6H12F2
4
H20Na
C6H12F
H20NaCl
C6H12F2
3
KBrAsC
Mg2F
CsH
6
KBrAsCl
Mg2Fe
CsHe
Mg2F
Cl2NaOPMg2F
KBrAsC

Exemplo de Saída
Prossiga
Prossiga
Abortar
Abortar
Prossiga

Prossiga
Prossiga
Abortar
Abortar

Prossiga
Prossiga
Prossiga
Abortar
Abortar
Abortar
"""
def verificar_experiencia_perigosa(caso, referencia):
    """Verifica se um composto perigoso está presente no caso"""
    nocivo_presente = False
    for nocivo in referencia:
        if nocivo in caso:
            try:
                ultimo_char_nocivo = nocivo[-1]
                proximo_char_nocivo = caso[caso.index(nocivo) + len(nocivo)]
                if ultimo_char_nocivo.isdigit() and proximo_char_nocivo.isalpha():
                    nocivo_presente = True
                if ultimo_char_nocivo.isalpha() and proximo_char_nocivo.isupper():
                    nocivo_presente = True
            except IndexError:
                nocivo_presente = True
    return nocivo_presente

resultado_final = []
casos_teste = int(input())
for _ in range(casos_teste):
    resultado_caso = []

    nr_compostos_perigosos = int(input())
    compostos_perigosos = []
    for _ in range(nr_compostos_perigosos):
        composto_perigoso = input()
        compostos_perigosos.append(composto_perigoso)

    qtd_experiencias = int(input())
    for _ in range(qtd_experiencias):
        experiencia = input()
        if verificar_experiencia_perigosa(experiencia, compostos_perigosos):
            resultado_caso.append('Abortar')
        else:
            resultado_caso.append('Prossiga')

    resultado_final.append(resultado_caso)
for i, caso in enumerate(resultado_final):
    for resultado in caso:
        print(resultado)
    if i < len(resultado_final) - 1:
        print()
