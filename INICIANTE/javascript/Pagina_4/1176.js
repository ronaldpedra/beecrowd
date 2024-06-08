// beecrowd | 1176
// Fibonacci em Vetor
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

// Entrada
// A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.

// Saída
// Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.

// Exemplo de Entrada	Exemplo de Saída
// 3                    Fib(0) = 0
// 0                    Fib(4) = 3
// 4                    Fib(2) = 1
// 2

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
function fibonacci(num) {
    if (num == 0) {
        return 0
    }
    if (num == 1) {
        return 1
    }
    fibonacci_cache = {}
    fibonacci_cache[0] = 0
    fibonacci_cache[1] = 1
    for (let i = 2; i <= num; i++) {
        fibonacci_cache[i] = fibonacci_cache[i - 1] + fibonacci_cache[i - 2]
    }
    return fibonacci_cache[num]
}

lines.shift()
for (var caso of lines) {
    caso = parseInt(caso)
    console.log(`Fib(${caso}) = ${fibonacci(caso)}`)
}
