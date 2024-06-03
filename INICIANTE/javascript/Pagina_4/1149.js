// beecrowd | 1149
// Somando Inteiros Consecutivos
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

// Entrada
// A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

// Saída
// A saída contém apenas um valor inteiro.

// Exemplo de Entrada	Exemplo de Saída
// 3 2                  7

// 3 -1 0 -2 2          7

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

let numeros = lines[0].split(' ').map(Number)
let inicio
let fim
let soma = 0
for (const [index, elemento] of numeros.entries()) {
    if (index == 0) {
        inicio = elemento
    } else if (elemento > 0) {
        fim = inicio + elemento
    }
}
for (i = inicio; i < fim; i++) {
    soma += i
}
console.log(soma)
