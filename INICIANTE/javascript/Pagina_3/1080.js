// beecrowd | 1080
// Maior e Posição
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

// Entrada
// O arquivo de entrada contém 100 números inteiros, positivos e distintos.

// Saída
// Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
// 2                    34565
// 113                  4
// 45
// 34565
// 6
// ...
// 8
 
let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '').map(Number)

var maior = -1
var posicao = 0
for (var [i, numero] of lines.entries()) {
    if (numero > maior) {
        maior = numero
        posicao = i + 1
    }
}
console.log(`${maior}\n${posicao}`)
