// beecrowd | 1099
// Soma de Ímpares Consecutivos II
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

// Entrada
// A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

// Saída
// Imprima a soma de todos valores ímpares entre X e Y.

// Exemplo de Entrada	Exemplo de Saída
// 7                    0
// 4 5                  11
// 13 10                5
// 6 4                  0
// 3 3                  0
// 3 5                  0
// 3 4                  12
// 3 8

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var trash = lines.shift()
delete trash
lines = lines.filter(item => item !== '')

for (var caso of lines) {
    var soma = 0
    var lista = caso.split(' ').map(Number)
    lista.sort((a, b) => {return a - b})

    for (let i = lista[0] + 1; i < lista[1]; i++)
        if (i % 2 !== 0) {
            soma += i
        }
    console.log(soma)
}
