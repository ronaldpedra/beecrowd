// beecrowd | 1044
// Múltiplos
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

// Entrada
// A entrada contém valores inteiros.

// Saída
// A saída deve conter uma das mensagens conforme descrito acima.

// Exemplo de Entrada	Exemplo de Saída
// 6 24                Sao Multiplos

// 6 25                Nao sao Multiplos

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var lista = lines[0].split(' ').map(Number)

// Processamento dos dados
function multiplos(lista) {
    var listaOrdenada = lista.slice().sort(compararNumeros)

    if(listaOrdenada[1] % listaOrdenada[0] === 0) {
        return `Sao Multiplos`
    }
    return `Nao sao Multiplos`
}
function compararNumeros(a, b) {
    return a - b;
}

// Retorno do pedido
console.log(multiplos(lista))
