// beecrowd | 1019
// Conversão de Tempo
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

// Entrada
// O arquivo de entrada contém um valor inteiro N.

// Saída
// Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

// Exemplo de Entrada	Exemplo de Saída
// 556                 0:9:16

// 1                   0:0:1

// 140153              38:55:53

let input = require("fs").readFileSync("./javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var tempo = parseInt(lines[0])

// Processamento dos dados
function horaMinutoSegundo(tempo){
    
    var hora = Math.floor(tempo / 3600)
    var minuto = Math.floor((tempo - (hora * 3600)) / 60)
    var segundo = tempo - (hora * 3600) - (minuto * 60)
    
    console.log(`${hora}:${minuto}:${segundo}`)
}

// Retorno do pedido
horaMinutoSegundo(tempo)
