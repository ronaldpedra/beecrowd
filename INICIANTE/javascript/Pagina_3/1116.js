// beecrowd | 1116
// Dividindo X por Y
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 2
// Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

// Entrada
// A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

// Saída
// Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

// Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

// Exemplo de Entrada	Exemplo de Saída
// 3                    -1.5
// 3 -2                 divisao impossivel
// -8 0                 0.0
// 0 8

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var trash = lines.shift()
delete trash
lines = lines.filter(item => item !== '')

for (var ponto of lines) {

    ponto = ponto.split(' ').map(Number)
    var x = ponto[0]
    var y = ponto[1]
    
    if (y === 0) {
        console.log(`divisao impossivel`)
    }
    else {
        console.log(`${(x / y).toFixed(1)}`)
    }
}
