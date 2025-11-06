"""
beecrowd | 2712
Rodízio Veicular
Por , Silva A M BR Brazil

Timelimit: 1
O rodízio municipal de veículos de São Paulo é uma restrição à 
circulação de veículos automotores na cidade. Implantado desde 1996 com 
o propósito de melhorar as condições ambientais reduzindo a carga de 
poluentes na atmosfera, se consolidou como um instrumento para reduzir 
congestionamentos nas principais vias da cidade, nos horários de maior 
movimento. Nas vias delimitadoras não é permitido o tráfego de caminhões 
e automóveis que estejam dentro da restrição. Há uma escala que 
determina em quais dias da semana quais veículos não podem circular. 
Essa escala é regida pelo último dígito da placa do veículo, sendo:

Segunda-feira, digito final da placa 1 e 2
Terça-feira, digito final da placa 3 e 4
Quarta-feira, digito final da placa 5 e 6
Quinta-feira, digito final da placa 7 e 8
Sexta-feira, digito final da placa 9 e 0
Os motoristas que são flagrados violando a restrição de circulação são 
autuados com multa e quatro pontos na carteira de habilitação.

Entrada
A primeira linha de entrada representa a quantidade de testes N 
(0 <= N < 1000) que deverão ser considerados. As demais entradas são 
cadeia de caracteres com tamanho máximo S (1 <= S <= 100) que 
representam cada placa que deverá ser analisada, de tal forma que, cada 
placa fique em uma única linha de entrada. O formato esperado para uma 
placa veicular válida em São Paulo é "AAA-9999", tal que A é um caracter 
válido em [A-Z], e 9 um dígito numérico válido em [0-9].

Saída
O conjunto de valores válidos como saída são: MONDAY, TUESDAY, 
WEDNESDAY, THURSDAY e FRIDAY, de acordo com a tabela de restrições 
predefinida, e FAILURE caso a placa não apresente o padrão definido.

Exemplos de Entrada	Exemplos de Saída
3                   TUESDAY
ABC-1234            FRIDAY
XYZ-1010            FAILURE
AAA3333

4
abc-1234            FAILURE
a-1010              FAILURE
ABCD-1234           FAILURE
AIQ-2001            MONDAY
"""
import re


DIAS_RODIZIO = [
    "FRIDAY", "MONDAY", "MONDAY", "TUESDAY", "TUESDAY", 
    "WEDNESDAY", "WEDNESDAY", "THURSDAY", "THURSDAY", "FRIDAY"
]

def rodizio(placa_rodizio: str) -> str:
    """Retorna o dia do rodízio da placa"""
    placa_final = int(placa_rodizio[-1:])
    return DIAS_RODIZIO[placa_final]


def validar_placa(placa_a_verificar: str) -> bool:
    """
    Verifica se uma string de placa segue o formato "AAA-9999".
    
    Onde:
    - A = Letra maiúscula (A-Z)
    - 9 = Dígito (0-9)
    """

    # --- Definição do Padrão (Pattern) ---
    # ^        -> Indica o início da string
    # [A-Z]{3} -> Corresponde a exatamente 3 letras maiúsculas
    # -        -> Corresponde ao hífen literal
    # [0-9]{4} -> Corresponde a exatamente 4 dígitos numéricos
    # $        -> Indica o fim da string
    #
    # O "r" antes da string (r"...") indica que é uma "raw string",
    # o que evita problemas com barras invertidas (embora não tenhamos
    # nenhuma aqui, é uma boa prática para regex).

    padrao = r'^[A-Z]{3}-[0-9]{4}$'

    return bool(re.fullmatch(padrao, placa_a_verificar))

casos_teste = int(input())
for _ in range(casos_teste):
    placa = input()
    if validar_placa(placa):
        print(rodizio(placa))
    else:
        print('FAILURE')
