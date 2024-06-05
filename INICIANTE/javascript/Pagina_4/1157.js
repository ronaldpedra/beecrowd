// beecrowd | 1157
// Divisores I
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Ler um número inteiro N e calcular todos os seus divisores.

// Entrada
// O arquivo de entrada contém um valor inteiro.

// Saída
// Escreva todos os divisores positivos de N, um valor por linha.

// Exemplo de Entrada	Exemplo de Saída
// 6                    1
//                      2
//                      3
//                      6

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Funções Auxiliares
function calculaDivisores(n) {
    var divisores = []
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
            divisores.push(i)
        }
    }

    return divisores

}

// Coleta dos dados
lines = lines.filter(item => item !== '')
lines = lines.map(Number)

// Processamento dos dados
var divisores = calculaDivisores(lines[0])

// Retorno do pedido
divisores.map(divisor => console.log(divisor))
