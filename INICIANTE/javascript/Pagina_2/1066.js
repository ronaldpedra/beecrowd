// beecrowd | 1066
// Pares, Ímpares, Positivos e Negativos
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

// Entrada
// O arquivo de entrada contém 5 valores inteiros quaisquer.

// Saída
// Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

// Exemplo de Entrada	Exemplo de Saída
// -5                  3 valor(es) par(es)
// 0                   2 valor(es) impar(es)
// -3                  1 valor(es) positivo(s)
// -4                  3 valor(es) negativo(s)
// 12

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var numeros = lines.map(Number)
var numerosUnicos = [...new Set(numeros)]

var pares = 0
var impares = 0
var positivos = 0
var negativos = 0

for (let n of numerosUnicos) {
    if (n % 2 === 0) {
        pares += 1
    } else {
        impares += 1
    }
    if (n > 0) {
        positivos += 1
    }
    if (n < 0) {
        negativos += 1
    }
}
console.log(`${pares} valor(es) par(es)\n${impares} valor(es) impar(es)`)
console.log(`${positivos} valor(es) positivo(s)\n${negativos} valor(es) negativo(s)`)
