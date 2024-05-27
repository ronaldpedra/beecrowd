// beecrowd | 1038
// Lanche
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.



// Entrada
// O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

// Saída
// O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

// Exemplo de Entrada	Exemplo de Saída
// 3 2                 Total: R$ 10.00

// 4 3                 Total: R$ 6.00

// 2 3                 Total: R$ 13.50

let input = require("fs").readFileSync("./javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var valor = lines[0].split(' ')

// Processamento dos dados
function contaAPagar(valor){

    precos = [4.0, 4.5, 5.0, 2.0, 1.5]

    return precos[(valor[0] - 1)] * valor[1]
}

// Retorno do pedido
console.log(`Total: R$ ${contaAPagar(valor).toFixed(2)}`)
