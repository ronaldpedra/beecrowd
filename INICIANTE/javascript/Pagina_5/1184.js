// beecrowd | 1184
// Abaixo da Diagonal Principal
// Por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal principal da matriz, conforme ilustrado abaixo (área verde).




// Entrada
// A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

// Saída
// Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

// Exemplo de Entrada	Exemplo de Saída
// S                    12.6
// 1.0
// 0.0
// -3.5
// 2.5
// 4.1
// ...

let input = require("fs").readFileSync("./INICIANTE/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
let operacao = lines.shift().replace('\r', '')
let soma = 0
let divisor = 0
for (let i = 0; i < 12; i++) {
    for (let j = 0; j < 12; j++) {
        let n = parseFloat(lines.shift())
        if (j < i) {
            soma += n
            divisor += 1
        }
    }
}

if (operacao === 'S') {
    console.log(`${soma.toFixed(1)}`)
}
if (operacao === 'M') {
    console.log(`${(soma / divisor).toFixed(1)}`)
}
