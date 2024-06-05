// beecrowd | 1158
// Soma de Ímpares Consecutivos III
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
// para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
// para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

// Entrada
// A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

// Saída
// Imprima a soma dos consecutivos números ímpares a partir do valor X.

// Exemplo de Entrada	Exemplo de Saída
// 2                    21
// 4 3                  24
// 11 2

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Funções Auxiliares
function somaImparesConsecutivos(caso) {
    var soma = 0
    var impares = 0
    var passo = 0
    while (true) {
        if (impares >= caso[1]) {
            break
        }
        var teste = caso[0] + passo
        if (teste % 2 !== 0) {
            soma += teste
            impares++
        }
        passo++
    }
    return soma
}

// Coleta dos dados
lines = lines.filter(item => item !== '')
lines.shift()
lines = lines.map(item => item.split(' ').map(Number))

// Processamento dos dados
// Retorno do pedido
for (caso of lines) {
    console.log(somaImparesConsecutivos(caso))
}
