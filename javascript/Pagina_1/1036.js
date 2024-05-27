// beecrowd | 1036
// Fórmula de Bhaskara
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

// Entrada
// Leia três valores de ponto flutuante (double) A, B e C.

// Saída
// Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

// Exemplos de Entrada	Exemplos de Saída
// 10.0 20.1 5.1       R1 = -0.29788
//                     R2 = -1.71212

// 0.0 20.0 5.0        Impossivel calcular

// 10.3 203.0 5.0      R1 = -0.02466
//                     R2 = -19.68408

// 10.0 3.0 5.0        Impossivel calcular

let input = require("fs").readFileSync("./javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var dados = lines[0].split(' ')

// Processamento dos dados
function bhaskara(dados){
    var a = parseFloat(dados[0])
    var b = parseFloat(dados[1])
    var c = parseFloat(dados[2])

    if (a === 0 || (b ** 2 - 4 * a * c) < 0){
        console.log(`Impossivel calcular`)
    } else {
        var x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        var x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        console.log(`R1 = ${x1.toFixed(5)}\nR2 = ${x2.toFixed(5)}`)
    }
}

// Retorno do pedido
bhaskara(dados)
