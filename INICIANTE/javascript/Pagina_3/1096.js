// beecrowd | 1096
// Sequencia IJ 2
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

// Entrada
// Não há nenhuma entrada neste problema.

// Saída
// Imprima a sequencia conforme exemplo abaixo

// Exemplo de Entrada	Exemplo de Saída
//                      I=1 J=7
//                      I=1 J=6
//                      I=1 J=5
//                      I=3 J=7
//                      I=3 J=6
//                      I=3 J=5
//                      ...
//                      I=9 J=7
//                      I=9 J=6
//                      I=9 J=5

for (let i = 1; i <= 9; i += 2) {
    for (let j = 7; j >= 5; j--) {
        console.log(`I=${i} J=${j}`)
    }
}
