// beecrowd | 1074
// Par ou Ímpar
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.

// Entrada
// A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste. Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

// Saída
// Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.

// Exemplo de Entrada	Exemplo de Saída
// 4                   ODD NEGATIVE
// -5                  NULL
// 0                   ODD POSITIVE
// 3                   EVEN NEGATIVE
// -4

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");


lines = lines.filter(item => item !== '')
var numeros = lines.map(Number)

for (let i = 1; i < numeros.length; i++) {

    var resposta = ''

    if (numeros[i] === 0) {
        console.log(`NULL`)
        continue
    }
    if (numeros[i] % 2 === 0) {
        resposta += 'EVEN '
    } else {
        resposta += 'ODD '
    }
    if (numeros[i] > 0) {
        resposta += 'POSITIVE'
    } else {
        resposta += 'NEGATIVE'
    }
    console.log(resposta)
}
