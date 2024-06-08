// beecrowd | 1178
// Preenchimento de Vetor III
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.

// Entrada
// A entrada contem um valor de dupla precisão com 4 casas decimais.

// Saída
// Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição. Cada valor do vetor deve ser apresentado com 4 casas decimais.

// Exemplo de Entrada	Exemplo de Saída
// 200.0000             N[0] = 200.0000
//                      N[1] = 100.0000
//                      N[2] = 50.0000
//                      N[3] = 25.0000
//                      N[4] = 12.5000
//                      ...

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

function formatNumber(num) {
    var decimalValues = (num.toString().split('.')[1]);
    if (decimalValues[4] <= 5 && decimalValues[5] == 0) {
        return num.toString().split('.')[0] + '.' + decimalValues[0] + decimalValues[1] + decimalValues[2] + decimalValues[3];
    }
    return parseFloat(num).toFixed(4);
}

lines = lines.filter(item => item !== '')
var n = parseFloat(lines.shift()).toFixed(6)
for (var i = 0; i < 100; i++) {
    console.log(`N[${i}] = ${formatNumber(n)}`)
    n /= 2
    n = n.toFixed(6)
}
