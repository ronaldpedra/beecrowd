// beecrowd | 1020
// Idade em Dias
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

// Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

// Entrada
// O arquivo de entrada contém um valor inteiro.

// Saída
// Imprima a saída conforme exemplo fornecido.

// Exemplo de Entrada	Exemplo de Saída
// 400                 1 ano(s)
//                     1 mes(es)
//                     5 dia(s)

// 800                 2 ano(s)
//                     2 mes(es)
//                     10 dia(s)

// 30                  0 ano(s)
//                     1 mes(es)
//                     0 dia(s)

let input = require("fs").readFileSync("./javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var idade = parseInt(lines[0])

// Processamento dos dados
function anosMesesDias(idade){
    
    var ano = Math.floor(idade / 365)
    var meses = Math.floor((idade - (ano * 365)) / 30)
    var dias = idade - (ano * 365) - (meses * 30)
    
    console.log(`${ano} ano(s)\n${meses} mes(es)\n${dias} dia(s)`)
}

// Retorno do pedido
anosMesesDias(idade)

