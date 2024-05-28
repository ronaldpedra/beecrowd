// beecrowd | 1042
// Sort Simples
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

// Entrada
// A entrada contem três números inteiros.

// Saída
// Imprima a saída conforme foi especificado.

// Exemplo de Entrada	Exemplo de Saída
// 7 21 -14            -14
//                     7
//                     21

//                     7
//                     21
//                     -14

// -14 21 7            -14
//                     7
//                     21

//                     -14
//                     21
//                     7

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var lista = lines[0].split(' ').map(Number)

// Processamento dos dados
function imprimeListaOrdenada(lista){
    var listaOrdenada = lista.slice().sort(compararNumeros)
    for (let i = 0; i < listaOrdenada.length; i++){
        console.log(`${listaOrdenada[i]}`)
    }
    
}
function imprimeLista(lista){
    for (let j = 0; j < lista.length; j++){
        console.log(`${lista[j]}`)
    }
}

function compararNumeros(a, b) {
    return a - b;
}

// Retorno do pedido
imprimeListaOrdenada(lista)
console.log(``)
imprimeLista(lista)
