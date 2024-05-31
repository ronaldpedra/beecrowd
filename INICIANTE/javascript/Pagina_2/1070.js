// beecrowd | 1070
// Seis Números Ímpares
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

// Entrada
// A entrada será um valor inteiro positivo.

// Saída
// A saída será uma sequência de seis números ímpares.

// Exemplo de Entrada	Exemplo de Saída
// 8                   9
//                     11
//                     13
//                     15
//                     17
//                     19

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var numero = parseInt(lines)
var contagem = 1

while (true) {
    if (numero % 2 !== 0) {
        console.log(numero)
        if (contagem === 6) {
            break
        } else {
            contagem += 1
        }
    }
    numero += 1
}
