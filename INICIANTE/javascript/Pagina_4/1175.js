// beecrowd | 1175
// Troca em Vetor I
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

// Entrada
// A entrada contém 20 valores inteiros, positivos ou negativos.

// Saída
// Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

// Exemplo de Entrada	Exemplo de Saída
// 0                    N[0] = 230
// -5                   N[1] = 63
// ...                  ...
// 63                   N[18] = -5
// 230                  N[19] = 0

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
let n = Array(20).fill(0)
for (let i = 19; i >= 0; i--) {
    n[i] = parseInt(lines.shift())
}

for (let j = 0; j <= 19; j++) {
    console.log(`N[${j}] = ${n[j]}`)
}
