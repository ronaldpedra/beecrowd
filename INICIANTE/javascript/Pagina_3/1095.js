// beecrowd | 1095
// Sequencia IJ 1
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

// Entrada
// Não há nenhuma entrada neste problema.

// Saída
// Imprima a sequencia conforme exemplo abaixo

// Exemplo de Entrada	Exemplo de Saída
//                      I=1 J=60
//                      I=4 J=55
//                      I=7 J=50
//                      ...
//                      I=? J=0

var i = 1
var j = 60
while (j >= 0) {
    console.log(`I=${i} J=${j}`)
    i += 3
    j -= 5
}