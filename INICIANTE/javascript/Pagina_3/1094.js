// beecrowd | 1094
// Experiências
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

// Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

// Entrada
// A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

// Saída
// Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

// Exemplo de Entrada	Exemplo de Saída
// 10                   Total: 92 cobaias
// 10 C                 Total de coelhos: 29
// 6 R                  Total de ratos: 40
// 15 S                 Total de sapos: 23
// 5 C                  Percentual de coelhos: 31.52 %
// 14 R                 Percentual de ratos: 43.48 %
// 9 C                  Percentual de sapos: 25.00 %
// 6 R
// 8 S
// 5 C
// 14 R

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

var trash = lines.shift()
delete trash
lines = lines.filter(item => item !== '')

var total = 0
var coelhos = 0
var ratos = 0
var sapos = 0

for (var casos of lines) {
    // casosTeste.push(casos.split(' '))
    var caso = casos.split(' ')
    var animal = caso[1].replace('\r', '')
    switch (animal) {
        case "C":
            coelhos += parseInt(caso[0])
            break
        case 'R':
            ratos += parseInt(caso[0])
            break
        case 'S':
            sapos += parseInt(caso[0])
            break
    }
    total += parseInt(caso[0])
}

var percentualCoelhos = coelhos / total * 100
var percentualRatos = ratos / total * 100
var percentualSapos = sapos / total * 100

console.log(`Total: ${total} cobaias`)
console.log(`Total de coelhos: ${coelhos}`)
console.log(`Total de ratos: ${ratos}`)
console.log(`Total de sapos: ${sapos}`)
console.log(`Percentual de coelhos: ${percentualCoelhos.toFixed(2)} %`)
console.log(`Percentual de ratos: ${percentualRatos.toFixed(2)} %`)
console.log(`Percentual de sapos: ${percentualSapos.toFixed(2)} %`)
