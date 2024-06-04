// beecrowd | 1153
// Fatorial Simples
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

// Entrada
// A entrada contém um valor inteiro N (0 < N < 13).

// Saída
// A saída contém um valor inteiro, correspondente ao fatorial de N.

// Exemplo de Entrada	Exemplo de Saída
// 4                    24

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Funções Auxiliares
function fatorial(n) {

    if (n <= 1) {
        return 1
    }

    return n * fatorial(n - 1)

}

// Coleta dos dados
// Processamento dos dados
// Retorno do pedido
console.log(fatorial(parseInt(lines[0])))
