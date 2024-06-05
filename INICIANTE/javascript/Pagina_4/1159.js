// beecrowd | 1159
// Soma de Pares Consecutivos
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.

// Entrada
// O arquivo de entrada contém muitos valores inteiros. O último valor do arquivo é zero.

// Saída
// Imprima a saida conforme a explicação acima e o exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
// 4                    40
// 11                   80
// 0

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Funções Auxiliares
function somaCincoParesConsecutivos(caso) {
    if (caso % 2 == 0) {
        return caso * 5 + 20
    }    
    return (caso + 1) * 5 + 20
}

// Coleta dos dados
lines = lines.filter(item => item !== '')
lines = lines.map(Number)

// Processamento dos dados
// Retorno do pedido
for (caso of lines) {
    if (caso === 0) {
        break
    }
    console.log(somaCincoParesConsecutivos(caso))
}
