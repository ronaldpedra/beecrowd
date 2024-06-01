// beecrowd | 1113
// Crescente e Decrescente
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

// Entrada
// A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser encerrada ao ser fornecido valores iguais para X e Y.

// Saída
// Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário imprima a mensagem “Decrescente”.

// Exemplo de Entrada	Exemplo de Saída
// 5 4                  Decrescente
// 7 2                  Decrescente
// 3 8                  Crescente
// 2 2

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')

for (var caso of lines) {
    
    var lista = caso.split(' ').map(Number)
    
    if (lista[0] == lista[1]) {
        break
    } else if (lista[0] < lista[1]) {
        console.log(`Crescente`)
    } else {
        console.log(`Decrescente`)
    }
}
