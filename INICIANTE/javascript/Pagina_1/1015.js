// beecrowd | 1015
// Distância Entre Dois Pontos
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

// Distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

// Entrada
// O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

// Saída
// Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

// Exemplo de Entrada	Exemplo de Saída
// 1.0 7.0              4.4721
// 5.0 9.0

// -2.5 0.4             16.1484
// 12.1 7.3

// 2.5 -0.4             16.4575
// -12.2 7.0

let input = require("fs").readFileSync("./javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var p1 = lines.shift().split(' ')
var p2 = lines.shift().split(' ')
var x1 = parseFloat(p1[0])
var y1 = parseFloat(p1[1])
var x2 = parseFloat(p2[0])
var y2 = parseFloat(p2[1])

// Processamento dos dados
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

// Retorno do pedido
console.log(distancia.toFixed(4))
