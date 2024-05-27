// beecrowd | 1037
// Intervalo
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

// O símbolo ( representa "maior que". Por exemplo:
// [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
// (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

// Entrada
// O arquivo de entrada contém um número com ponto flutuante qualquer.

// Saída
// A saída deve ser uma mensagem conforme exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
// 25.01               Intervalo (25,50]

// 25.00               Intervalo [0,25]

// 100.00              Intervalo (75,100]

// -25.02              Fora de intervalo

let input = require("fs").readFileSync("./javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var valor = parseFloat(lines[0])

// Processamento dos dados
function intervalo(valor){

    if (0 <= valor && valor <= 25){
        return 'Intervalo [0,25]'
    }

    if (25 < valor && valor <= 50){
        return 'Intervalo (25,50]'
    }

    if (50 < valor && valor <= 75){
        return 'Intervalo (50,75]'
    }

    if (75 < valor && valor <= 100){
        return 'Intervalo (75,100]'
    }

    return 'Fora de intervalo'
}

// Retorno do pedido
console.log(intervalo(valor))
