"""
beecrowd | 2686
A Mudança Continua!!
Por Samuel Lucas Santos Gomes, IFSULDEMINAS BR Brazil

Timelimit: 1

Novamente Júlio pede sua ajuda, ele esqueceu de um pequeno detalhe. Como 
o seu o programa anterior só informava uma saudação, ele pediu que 
transformasse o grau do Sol/Lua em HH:MM:SS. Então caso aceite: dado um 
grau relativo a posição do Sol/Lua, refaça o sistema só que agora além 
da saudação de cada período do dia, informe exatamente as horas, os 
minutos e segundos.

Entrada
A entrada contem um pontos flutuantes M (0 ≥ M < 360) representando a 
posição, em graus,do Sol/Lua em relação a terra. Como eles andam em 
constante movimento seu programa receberá diversos casos a cada segundo
(EOF).

Saída
Imprima qual período do dia ele se encontra: "Boa Tarde!!", 
"Boa Noite!!", "Bom Dia!!" e "De Madrugada!!", e na linhas de baixo 
exiba as horas, minutos e segundos (HH:MM:SS).

Exemplo de Entrada
1.50
95.5
187.5
279.5

Exemplo de Saída
Bom Dia!!
06:06:00
Boa Tarde!!
12:22:00
Boa Noite!!
18:30:00
De Madrugada!!
00:38:00
"""
def que_horas_sao(graus):
    """Calcula as horas conforme a inclinação em graus"""
    horas, minutos = divmod(graus * 1440 / 360, 60)

    # Por convenção do problema 0º começa com 6 horas.
    horas = (horas + 6) % 24
    return (int(horas), int(minutos))

while True:
    try:
        posicao = float(input())
        hora, minuto = que_horas_sao(posicao)

        if 90 <= posicao < 180:
            print('Boa Tarde!!')
        elif 180 <= posicao < 270:
            print('Boa Noite!!')
        elif 270 <= posicao < 360:
            print('De Madrugada!!')
        else:
            print('Bom Dia!!')
        print(f'{hora:02d}:{minuto:02d}:00')

    except EOFError:
        break
