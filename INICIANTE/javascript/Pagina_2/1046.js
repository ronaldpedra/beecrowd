// beecrowd | 1046
// Tempo de Jogo
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

// Entrada
// A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

// Saída
// Apresente a duração do jogo conforme exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
// 16 2                O JOGO DUROU 10 HORA(S)

// 0 0                 O JOGO DUROU 24 HORA(S)

// 2 16                O JOGO DUROU 14 HORA(S)

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var lista = lines[0].split(' ').map(Number)

// Processamento dos dados
function duracaoDoJogo(lista) {
    var ini = lista[0] // Início do jogo
    var fim = lista[1]

    if (ini < fim) {
        console.log(`O JOGO DUROU ${fim - ini} HORA(S)`)
    } else {
        console.log(`O JOGO DUROU ${fim + 24 - ini} HORA(S)`)
    }
}

// Retorno do pedido
duracaoDoJogo(lista)
