// beecrowd | 1075
// Resto 2
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

// Entrada
// A entrada contém um valor inteiro N (N < 10000).

// Saída
// Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

// Exemplo de Entrada	Exemplo de Saída
// 13                  2
//                     15
//                     28
//                     41
//                     ...

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var n = parseInt(lines[0])

console.log(`2`)

var numeros = n
var multiplo = 1

while (true) {
    numeros = n * multiplo + 2
    multiplo += 1
    if (numeros > 10000) {
        break
    }
    console.log(numeros)
}
