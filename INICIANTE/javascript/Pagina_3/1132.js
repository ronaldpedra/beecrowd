// beecrowd | 1132
// Múltiplos de 13
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

// Entrada
// O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

// Saída
// Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.

// Sample Input Sample Output
// 100          13954
// 200

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '').map(Number).sort((a, b) => {return a - b})

var soma = 0
for (let i = lines[0]; i <= lines[1]; i++) {
    if (i % 13 !== 0) {
        soma += i
    }
}
console.log(soma)