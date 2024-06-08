// beecrowd | 1181
// Linha na Matriz
// Por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser considerados na operação.




// Entrada
// A primeira linha de entrada contem um número L (0 ≤ L ≤ 11) indicando a linha que será considerada para operação. A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz, sendo que a mesma é preenchida linha por linha, da linha 0 até a linha 11, sempre da esquerda para a direita.

// Saída
// Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

// Exemplo de Entrada	Exemplo de Saída
// 2                    12.6
// S
// 0.0
// -3.5
// 2.5
// 4.1
// ...

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
let linha = parseInt(lines.shift())
let operacao = lines.shift().replace('\r', '')
let soma = 0
for (let i = 0; i < 12; i++) {
    for (let j = 0; j < 12; j++) {
        let n = parseFloat(lines.shift())
        if (i == linha) {
            soma += n
        }
    }
}

if (operacao === 'S') {
    console.log(`${soma.toFixed(1)}`)
}
if (operacao === 'M') {
    console.log(`${(soma / 12).toFixed(1)}`)
}
