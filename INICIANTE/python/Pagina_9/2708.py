"""
beecrowd | 2708
Turistas no Parque Huacachina
Por André Marcos Silva BR Brazil

Timelimit: 1
A agência de turismo municipal da cidade de Ica, no Peru montou um posto 
de controle de jipes de aventura que sobem para as dunas do parque 
Hucachina. Como durante o dia, são vários os off-roads que sobem e 
descem do parque nacional, e nem sempre os turistas usam um mesmo 
transporte para a ida e volta, a prefeitura precisava ter um melhor 
controle e segurança sobre fluxo de visitantes no parque. Desenvolva um 
programa que receba como entrada se um jipe está entrando ou voltando do 
parque e a quantidade de turistas que este veículo está transportando. 
Ao final do turno, o programa deve indicar a quantidade de veículos e de 
turistas que ainda faltam regressar da aventura.

Entrada
O programa deve receber sucessivos pares de entrada. Cada par deve 
indicar o movimento do jipe e a quantidade de turistas que este está 
transportando. A primeira entrada deve ser "SALIDA" ou "VUELTA". 
"SALIDA" deve indicar que o jipe está saindo da central e entrando no 
parque; e "VUELTA" que o jipe está retornando do passeio. Imediatamente 
na sequência, o programa recebe um número inteiro T (onde, 0 <= T <=20) 
que indica a quantidade de turistas que estão sendo transportados pelo 
jipe. A string "ABEND" deve ser o indicador de fim de processamento.

Saída
Como objetivo o programa deve apresentar duas saídas, uma em cada linha: 
a quantidade de turistas e a quantidade de jipes que ainda faltam voltar 
do parque.

Exemplos de Entrada	Exemplos de Saída
SALIDA 10           12
SALIDA 12           2
SALIDA 10
VUELTA 20
ABEND

SALIDA 15           5
SALIDA 20           0
VUELTA 15
VUELTA 15
SALIDA 0
VUELTA 0
ABEND
"""
jipes_no_parque = 0
turistas_no_parque = 0
while True:
    entrada = input()
    if entrada == 'ABEND':
        print(f'{turistas_no_parque}\n{jipes_no_parque}')
        break

    movimento, turistas = entrada.split()
    turistas = int(turistas)
    if movimento == 'SALIDA':
        jipes_no_parque += 1
        turistas_no_parque += turistas
    else:
        jipes_no_parque -= 1
        turistas_no_parque -= turistas
