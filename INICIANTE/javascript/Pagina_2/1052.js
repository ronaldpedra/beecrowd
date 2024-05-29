// beecrowd | 1052
// Mês
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

// Entrada
// A entrada contém um único valor inteiro.

// Saída
// Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

// Exemplo de Entrada	Exemplo de Saída
// 4                   April

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var nrMes = parseInt(lines[0])

// Processamento dos dados
function mesPorExtenso(nrMes) {
    const meses = ['January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December']

    return meses[nrMes - 1]
}

// Retorno do pedido
console.log(mesPorExtenso(nrMes))
