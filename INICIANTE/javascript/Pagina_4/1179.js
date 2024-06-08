// beecrowd | 1179
// Preenchimento de Vetor IV
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

// Entrada
// A entrada contém 15 números inteiros.

// Saída
// Imprima a saída conforme o exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
// 1                    par[0] = 4
// 3                    par[1] = -4
// 4                    par[2] = 2
// -4                   par[3] = 8
// 2                    par[4] = 2
// 3                    impar[0] = 1
// 8                    impar[1] = 3
// 2                    impar[2] = 3
// 5                    impar[3] = 5
// -7                   impar[4] = -7
// 54                   impar[0] = 789
// 76                   impar[1] = 23
// 789                  par[0] = 54
// 23                   par[1] = 76
// 98                   par[2] = 98

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
function imprime_vetor(vetor, par=true) {
    if (par) {
        for (let i = 0; i < vetor.length; i++) {
            console.log(`par[${i}] = ${vetor[i]}`)
        }
    } else {
        for (let j = 0; j < vetor.length; j++) {
            console.log(`impar[${j}] = ${vetor[j]}`)
        }
    }
}

let pares = []
let impares = []
for (let k = 0; k <= 14; k++) {
    let n = parseInt(lines.shift())
    if (n % 2 == 0) {
        pares.push(n)
    } else {
        impares.push(n)
    }
    if (pares.length == 5) {
        imprime_vetor(pares)
        pares = []
    }
    if (impares.length == 5) {
        imprime_vetor(impares, par=false)
        impares = []
    }
}
imprime_vetor(impares, par=false)
imprime_vetor(pares)
