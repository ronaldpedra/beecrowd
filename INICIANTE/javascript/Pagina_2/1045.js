// beecrowd | 1045
// Tipos de Triângulos
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

// se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
// se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
// se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
// se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
// se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
// se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
// Entrada
// A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

// Saída
// Imprima todas as classificações do triângulo especificado na entrada.

// Exemplos de Entrada	Exemplos de Saída
// 7.0 5.0 7.0         TRIANGULO ACUTANGULO
//                     TRIANGULO ISOSCELES

// 6.0 6.0 10.0        TRIANGULO OBTUSANGULO
//                     TRIANGULO ISOSCELES

// 6.0 6.0 6.0         TRIANGULO ACUTANGULO
//                     TRIANGULO EQUILATERO

// 5.0 7.0 2.0         NAO FORMA TRIANGULO

// 6.0 8.0 10.0        TRIANGULO RETANGULO

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var lista = lines[0].split(' ').map(Number)

// Processamento dos dados
function tiposDeTriangulos(lista) {
    var listaOrdenada = lista.slice().sort(compararNumeros)
    var a = listaOrdenada[2]
    var b = listaOrdenada[1]
    var c = listaOrdenada[0]

    if (a >= b + c) {
        console.log('NAO FORMA TRIANGULO')
    } else {
        if (a ** 2 == b ** 2 + c ** 2) {
            console.log('TRIANGULO RETANGULO')
        }
        if (a ** 2 > b ** 2 + c ** 2){
            console.log('TRIANGULO OBTUSANGULO')
        }
        if (a ** 2 < b ** 2 + c ** 2) {
            console.log('TRIANGULO ACUTANGULO')
        }
        if (a === b && b === c) {
            console.log('TRIANGULO EQUILATERO')
        }
        if ((a === b && b != c) || (a === c && c != b) || (b === c && c != a)) {
            console.log('TRIANGULO ISOSCELES')
        }
    }
}
function compararNumeros(a, b) {
    return a - b;
}

// Retorno do pedido
tiposDeTriangulos(lista)
