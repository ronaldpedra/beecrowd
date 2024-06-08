// beecrowd | 1172
// Substituição em Vetor I
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

// Entrada
// A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

// Saída
// Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.

// Exemplo de Entrada	Exemplo de Saída
// 0                    X[0] = 1
// -5                   X[1] = 1
// 63                   X[2] = 63
// 0                    X[3] = 1
// ...                  ...

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
for (let i = 0; i <= 9; i++) {
    let n = parseInt(lines.shift())
        if (n <= 0) {
            console.log(`X[${i}] = 1`)
        } else {
            console.log(`X[${i}] = ${n}`)
        }
}
        