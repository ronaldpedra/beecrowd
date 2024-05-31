// beecrowd | 1065
// Pares entre Cinco Números
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

// Entrada
// O arquivo de entrada contém 5 valores inteiros quaisquer.

// Saída
// Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

// Exemplo de Entrada	Exemplo de Saída
// 7                    3 valores pares
// -5
// 6
// -4
// 12

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var numeros = lines.map(Number)
var numerosUnicos = [...new Set(numeros)]

var pares = 0

for (let n of numerosUnicos) {
    if (n % 2 === 0) {
        pares += 1
    }
}
console.log(`${pares} valores pares`)
