// beecrowd | 1117
// Validação de Nota
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

// Entrada
// A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

// Saída
// Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
// Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.

// Exemplo de Entrada	Exemplo de Saída
// -3.5                 nota invalida
// 3.5                  nota invalida
// 11.0                 media = 6.75
// 10.0

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '').map(Number)

var notas = []

for (var nota of lines) {
    
    if (notas.length === 2) {
        break
    }

    if (nota >= 0 && nota <= 10) {
        notas.push(nota)
    } else {
        console.log(`nota invalida`)
    }
}

console.log(`media = ${((notas[0] + notas[1]) / 2).toFixed(2)}`)
