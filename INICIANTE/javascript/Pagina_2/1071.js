// beecrowd | 1071
// Soma de Impares Consecutivos I
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

// Entrada
// O arquivo de entrada contém dois valores inteiros.

// Saída
// O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

// Exemplo de Entrada	Exemplo de Saída
// 6                   5
// -5

// 15                  13
// 12

// 12                  0
// 12

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
var numeros = lines.map(Number).sort((a, b) => {return a - b})
//numeros = numeros.filter(item => item !== 0)
var soma = 0

for (let numero = numeros[0] + 1; numero < numeros[1]; numero++) {

    if (numero % 2 !== 0) {
        soma += numero
    }
}

console.log(soma)
