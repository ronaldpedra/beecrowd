// beecrowd | 1115
// Quadrante
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

// Entrada
// A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

// Saída
// Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

// Exemplo de Entrada	Exemplo de Saída
// 2 2                  primeiro
// 3 -2                 quarto
// -8 -1                terceiro
// -7 1                 segundo
// 0 2

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')

for (var ponto of lines) {

    ponto = ponto.split(' ').map(Number)
    var x = ponto[0]
    var y = ponto[1]
    
    if (x === 0 || y === 0) {
        break
    }

    if (x > 0) {
        if (y > 0) {
            console.log(`primeiro`)
        } else {
            console.log(`quarto`)
        }
    }

    if (x < 0) {
        if (y > 0) {
            console.log(`segundo`)
        } else {
            console.log(`terceiro`)
        }
    }
}
