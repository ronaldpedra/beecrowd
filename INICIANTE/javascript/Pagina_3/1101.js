// beecrowd | 1101
// Sequência de Números e Soma
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

// Entrada
// O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

// Saída
// Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
// 5 2                  2 3 4 5 Sum=14
// 6 3                  3 4 5 6 Sum=18
// 5 0

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
lines = lines.filter(item => item.indexOf('0') === -1)
lines = lines.filter(item => item.indexOf('-') === -1)

for (var caso of lines) {
    var soma = 0
    var saida = ''
    var lista = caso.split(' ').map(Number)
    lista.sort((a, b) => {return a - b})

    for (let i = lista[0]; i <= lista[1]; i++) {
        soma += i
        if (i === lista[1]) {
            saida += `${i} Sum=${soma}`
        } else {
            saida += `${i} `
        }
    }
    console.log(`${saida}`)
}
