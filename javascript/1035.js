// beecrowd | 1035
// Teste de Seleção 1
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

// Entrada
// Quatro números inteiros A, B, C e D.

// Saída
// Mostre a respectiva mensagem após a validação dos valores.

// Exemplo de Entrada	Exemplo de Saída
// 5 6 7 8             Valores nao aceitos

// 2 3 2 6             Valores aceitos

let input = require("fs").readFileSync("./javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var dados = lines[0].split(' ')

// Processamento dos dados
function varificaValores(dados){
    var a = parseInt(dados[0])
    var b = parseInt(dados[1])
    var c = parseInt(dados[2])
    var d = parseInt(dados[3])

    if (b > c && d > a && (c + d) > (a + b) && c >= 0 <= d && a % 2 === 0){
        console.log(`Valores aceitos`)
    } else {
        console.log(`Valores nao aceitos`)
    }
}

// Retorno do pedido
varificaValores(dados)
