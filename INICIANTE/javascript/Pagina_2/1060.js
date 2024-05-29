// beecrowd | 1060
// Números Positivos
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

// Entrada
// Seis valores, negativos e/ou positivos.

// Saída
// Imprima uma mensagem dizendo quantos valores positivos foram lidos.

// Exemplo de Entrada	Exemplo de Saída
// 7                   4 valores positivos
// -5
// 6
// -3.4
// 4.6
// 12

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

numeros = lines.map(Number)
positivos = 0
for (let n of numeros) {
    if (n > 0) {
        positivos += 1
    }
}
console.log(`${positivos} valores positivos`)