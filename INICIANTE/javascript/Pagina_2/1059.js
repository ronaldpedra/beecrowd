// beecrowd | 1059
// Números Pares
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um programa que mostre os números pares entre 1 e 100, inclusive.

// Entrada
// Neste problema extremamente simples de repetição não há entrada.

// Saída
// Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

// Exemplo de Entrada	Exemplo de Saída
//                     2
//                     4
//                     6
//                     ...
//                     100

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

for (let i = 2; i <= 100; i += 2) {
    console.log(i)
}
    