# beecrowd | 1049
# Animal
# Por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

# vertebrado      ave         carnivoro   aguia
#                             onivoro     pomba
#                 mamifero    onivoro     homem
#                             herbivoro   vaca

# invertebrado    inseto      hematofago  pulga
#                             herbivoro   lagarta
#                 anelideo    hematofago  sanguessuga
#                             onivoro     minhoca

# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

# Saída
# Imprima o nome do animal correspondente à entrada fornecida.

# Exemplos de Entrada	Exemplos de Saída
# vertebrado          homem
# mamifero
# onivoro

# vertebrado          aguia
# ave
# carnivoro

# invertebrado        minhoca
# anelideo
# onivoro

# Função que retorna o animal procurado
def animal_procurado(caracteristicas: list):
    '''Função que retorna animal'''

    match caracteristicas[0]:
        case 'vertebrado':
            match caracteristicas[1]:
                case 'ave':
                    match caracteristicas[2]:
                        case 'carnivoro':
                            animal = 'aguia'
                        case 'onivoro':
                            animal = 'pomba'
                case 'mamifero':
                    match caracteristicas[2]:
                        case 'onivoro':
                            animal = 'homem'
                        case 'herbivoro':
                            animal = 'vaca'
        case 'invertebrado':
            match caracteristicas[1]:
                case 'inseto':
                    match caracteristicas[2]:
                        case 'hematofago':
                            animal = 'pulga'
                        case 'herbivoro':
                            animal = 'lagarta'
                case 'anelideo':
                    match caracteristicas[2]:
                        case 'hematofago':
                            animal = 'sanguessuga'
                        case 'onivoro':
                            animal = 'minhoca'

    return animal

# Programa principal
def main():
    '''Função Principal'''

    # Coleta os dados
    caracteristicas = [input(), input(), input()]

    # Processamento dos dados
    animal = animal_procurado(caracteristicas)

    # Retorno do pedido
    print(f'{animal}')


if __name__ == '__main__':
    main()
