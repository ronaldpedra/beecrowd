// beecrowd | 1154
// Idades
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

// Entrada
// A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

// Saída
// A saída contém um valor correspondente à média de idade dos indivíduos.

// A média deve ser impressa com dois dígitos após o ponto decimal.

// Exemplo de Entrada	Exemplo de Saída
// 34                   39.25
// 56
// 44
// 23
// -2

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");



// Funções Auxiliares
function mediaIdade(soma, qtd) {

    return soma / qtd

}

// Coleta dos dados
lines = lines.filter(item => item !== '')
lines = lines.map(Number)

// Processamento dos dados
var contador = 0
var soma = 0
for (var idade of lines) {
    if (idade < 0) {
        break
    }
    contador += 1
    soma += idade
}
media = mediaIdade(soma, contador)

// Retorno do pedido
console.log(media.toFixed(2))
