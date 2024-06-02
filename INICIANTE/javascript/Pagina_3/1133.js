// beecrowd | 1133
// Resto da Divisão
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

// Entrada
// O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

// Saída
// Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

// Sample Input	Sample Output
// 10              12
// 18              13
//                 17

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '').map(Number).sort((a, b) => {return a - b})

for (let i = lines[0] + 1; i < lines[1]; i++) {
    if (i % 5 == 2 || i % 5 == 3) {
        console.log(i)
    }
}
