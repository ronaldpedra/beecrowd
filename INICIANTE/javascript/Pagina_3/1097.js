// beecrowd | 1097
// Sequencia IJ 3
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

// Entrada
// Não há nenhuma entrada neste problema.

// Saída
// Imprima a sequencia conforme exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
//                      I=1 J=7
//                      I=1 J=6
//                      I=1 J=5
//                      I=3 J=9
//                      I=3 J=8
//                      I=3 J=7
//                      ...
//                      I=9 J=15
//                      I=9 J=14
//                      I=9 J=13

var i = 1
var j = 7

while (i <= 9) {
    for (let k = j; k >= j - 2; k--) {
        console.log(`I=${i} J=${k}`)
    }
    i += 2
    j += 2
}
