// beecrowd | 1067
// Números Ímpares
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

// Entrada
// O arquivo de entrada contém 1 valor inteiro qualquer.

// Saída
// Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

// Exemplo de Entrada	Exemplo de Saída
// 8                   1
//                     3
//                     5
//                     7

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var numero = parseInt(lines)

for (let n = 1; n < numero + 1; n++) {
    if (n % 2 !== 0) {
        console.log(n)
    }
}
