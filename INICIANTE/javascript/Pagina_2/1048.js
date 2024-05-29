// beecrowd | 1048
// Aumento de Salário
// Por Neilor Tonin, URI BR Brasil

// Timelimit: 1
// A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


// Salário	Percentual de Reajuste
// 0 - 400.00
// 400.01 - 800.00
// 800.01 - 1200.00
// 1200.01 - 2000.00
// Acima de 2000.00

// 15%
// 12%
// 10%
// 7%
// 4%

// Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

// Entrada
// A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

// Saída
// Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
// 400.00              Novo salario: 460.00
//                     Reajuste ganho: 60.00
//                     Em percentual: 15 %

// 800.01              Novo salario: 880.01
//                     Reajuste ganho: 80.00
//                     Em percentual: 10 %

// 2000.00             Novo salario: 2140.00
//                     Reajuste ganho: 140.00
//                     Em percentual: 7 %

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var salario = parseFloat(lines[0])

// Processamento dos dados
function novoSalario(salario) {
    
    switch (true) {
        case (0.00 <= salario) && (salario <= 400.00):
            var percentual = 15
            break
        case (400.01 <= salario) && (salario <= 800.00):
            var percentual = 12
            break
        case (800.01 <= salario) && (salario <= 1200.00):
            var percentual = 10
            break
        case (1200.01 <= salario) && (salario <= 2000.00):
            var percentual = 7
            break
        case (salario >= 2000.01):
            var percentual = 4
    }

    var reajuste = salario * (percentual / 100)
    var salarioReajustado = salario + reajuste

    return [salarioReajustado, reajuste, percentual]
}

// Retorno do pedido
let [salarioReajustado, reajuste, percentual] = novoSalario(salario)
console.log(`Novo salario: ${salarioReajustado.toFixed(2)}\nReajuste ganho: ${reajuste.toFixed(2)}\nEm percentual: ${percentual} %`)
