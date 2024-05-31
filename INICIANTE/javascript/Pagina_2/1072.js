// beecrowd | 1072
// Intervalo 2
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
// Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

// Entrada
// A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
// Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

// Saída
// Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

// Exemplo de Entrada	Exemplo de Saída
// 4                   2 in
// 14                  2 out
// 123
// 10
// -25

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");


lines = lines.filter(item => item !== '')
var numeros = lines.map(Number)

var dentro = 0
var fora = 0

for (let i = 1; i < numeros.length; i++) {
    if (numeros[i] >= 10 && numeros[i] <= 20) {
        dentro += 1
    } else {
        fora += 1
    }
}

console.log(dentro, 'in')
console.log(fora, 'out')
