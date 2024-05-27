// beecrowd | 1041
// Coordenadas de um Ponto
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).



// Se o ponto estiver na origem, escreva a mensagem “Origem”.

// Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

// Entrada
// A entrada contem as coordenadas de um ponto.

// Saída
// A saída deve apresentar o quadrante em que o ponto se encontra.

// Exemplo de Entrada	Exemplo de Saída
// 4.5 -2.2            Q4

// 0.1 0.1             Q1

// 0.0 0.0             Origem

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var ponto = lines[0].split(' ').map(parseFloat)

// Processamento dos dados
function quadranteDoPonto(x, y){
    if (x === 0 && y === 0){
        return 'Origem'
    }
    if (x === 0 && y != 0){
        return 'Eixo Y'
    }
    if (x != 0 && y === 0){
        return 'Eixo X'
    }
    if (x > 0){
        if (y > 0){
            return 'Q1'
        } else {
            return 'Q4'
        }
    }
    if (x < 0){
        if (y > 0){
            return 'Q2'
        } else {
            return 'Q3'
        }
    }
    return None
}

// Retorno do pedido
var quadrante = quadranteDoPonto(ponto[0], ponto[1])

console.log(quadrante)
