// beecrowd | 1165
// Número Primo
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

// Entrada
// A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

// Saída
// Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

// Exemplo de Entrada	Exemplo de Saída
// 3                    8 nao eh primo
// 8                    51 nao eh primo
// 51                   7 eh primo
// 7

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
function ehPrimo(numero) {
    if (numero <= 1) {
        return false
    }
    if (numero <= 3) {
        return true
    }
    if (numero % 2 == 0 || numero % 3 == 0) {
        return false
    }
    let i = 5
    while (i * i <= numero) {
        if (numero % i == 0 || numero % (i + 2) == 0) {
            return false
        }
        i += 6
    }
    return true
}

for (let i = 1; i < lines.length; i++) {
    numero = parseInt(lines[i])
    if (ehPrimo(numero)) {
        console.log(`${numero} eh primo`)
    } else {
        console.log(`${numero} nao eh primo`)
    }
}
