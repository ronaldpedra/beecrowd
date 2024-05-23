// beecrowd | 1013
// O Maior
// Adaptado por Neilor Tonin, beecrowd  Brasil

// Timelimit: 1
// Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

// MaiorAB = (a + b + abs(a - b)) / 2

// Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

// Entrada
// O arquivo de entrada contém três valores inteiros.

// Saída
// Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

// Exemplos de Entrada	Exemplos de Saída
// 7 14 106             106 eh o maior

// 217 14 6             217 eh o maior

let input = require("fs").readFileSync("./javascript/stdin", "utf8");
let lines = input.split("\n");

function maiorAB(a, b){
    return (a + b + Math.abs(a - b)) / 2
}

var valores = lines[0].split(' ')
var maior = maiorAB(maiorAB(parseInt(valores[0]), parseInt(valores[1])), parseInt(valores[2]))

console.log(`${maior} eh o maior`)
