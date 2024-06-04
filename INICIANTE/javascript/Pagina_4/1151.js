// beecrowd | 1151
// Fibonacci Fácil
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

// Entrada
// O arquivo de entrada contém um valor inteiro N (0 < N < 46).

// Saída
// Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

// Exemplo de Entrada	Exemplo de Saída
// 5                    0 1 1 2 3

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Funções Auxiliares
function sequenciaFibonacci(n) {

    var sequencia = [0, 1]

    if (n < 3) {

        return sequencia.slice(0, n)

    }
    
    for (let i = 3; i <= n; i++) {

        sequencia.push(sequencia[i - 2] + sequencia[i - 3])
    }

    return sequencia

}

// Coleta os dados
let n = parseInt(lines[0])

// Processamento dos dados
var saida = ''
sequenciaFibonacci(n).forEach(item => saida += `${item} `)

// Retorno do pedido
console.log(saida.slice(0, -1))
