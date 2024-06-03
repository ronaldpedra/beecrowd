// beecrowd | 1145
// Sequência Lógica 2
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.

// Entrada
// O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

// Saída
// Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

// Exemplo de Entrada	Exemplo de Saída
// 3 99                 1 2 3
//                      4 5 6
//                      7 8 9
//                      10 11 12
//                      ...
//                      97 98 99

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var xy = lines.shift().split(' ').map(Number)
var x = xy[0]
var y = xy[1]

var saida = ''
var j = 0
for (let i = 1; i <= y; i++) {
    if (j < x - 1) {
        saida += `${i} `
        j++
    } else {
        console.log(`${saida + i}`)
        saida = ''
        j = 0

    }
}
