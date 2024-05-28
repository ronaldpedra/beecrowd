// beecrowd | 1043
// Triângulo
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


// Perimetro = XX.X


// Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


// Area = XX.X

// Entrada
// A entrada contém três valores reais.

// Saída
// O resultado deve ser apresentado com uma casa decimal.

// Exemplo de Entrada	Exemplo de Saída
// 6.0 4.0 2.0          Area = 10.0

// 6.0 4.0 2.1          Perimetro = 12.1

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var lista = lines[0].split(' ').map(Number)

// Processamento dos dados
function formaTriangulo(lista) {
    var a = lista[0]
    var b = lista[1]
    var c = lista[2]

    var teste1 = (Math.abs(b - c) < a) && (a < Math.abs(b + c))
    var teste2 = (Math.abs(a - c) < b) && (b < Math.abs(a + c))
    var teste3 = (Math.abs(a - b) < c) && (c < Math.abs(a + b))

    if (teste1 && teste2 && teste3){
        return `Perimetro = ${(a + b + c).toFixed(1)}`
    }
    return `Area = ${(((a + b) * c) / 2).toFixed(1)}`
}

// Retorno do pedido
console.log(formaTriangulo(lista))
