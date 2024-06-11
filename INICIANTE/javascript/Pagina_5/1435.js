// beecrowd | 1435
// Matriz Quadrada I
// Adaptado por Josué P. de Castro  Brasil
// Timelimit: 2
// Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

// Entrada
// A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

// Saída
// Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

// Exemplo de Entrada	Exemplo de Saída
// 1
// 2
// 3
// 4
// 5
// 0

//   1
 
//   1   1
//   1   1
 
//   1   1   1
//   1   2   1
//   1   1   1
   
//   1   1   1   1
//   1   2   2   1
//   1   2   2   1
//   1   1   1   1
 
//   1   1   1   1   1
//   1   2   2   2   1
//   1   2   3   2   1
//   1   2   2   2   1
//   1   1   1   1   1

let input = require("fs").readFileSync("./INICIANTE/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')
lines = lines.filter(item => item !== '0')
lines = lines.map(Number)

let esquerda
let direita
let cima
let embaixo
let menor
let saida

for (caso of lines) {
    // Usando a lógica da menor distância da borda
    for (let i = 0; i < caso; i++) {
        saida = ''
        for (let j = 0; j < caso; j++) {
            // Calcula a distância da borda em cada direção
            esquerda = j
            direita = (caso - 1) - j
            cima = i
            embaixo = (caso - 1) - i

            // Verifica qual é a menor distância da borda e acrescenta 1 para atender ao pedido
            menor = [esquerda, direita, cima, embaixo].sort((a, b) => {return a - b})[0] + 1
            // Retorna o pedido com tamanho 3 para todas as saídas
            saida += menor.toString().padStart(3)
        }
        console.log(saida)
    }
    console.log()
}


// for caso in casos_teste:


//     for i in range(caso):
//         for j in range(caso):


//             esquerda = j
//             direita = (caso - 1) - j
//             cima = i
//             embaixo = (caso - 1) - i


//             menor = sorted([esquerda, direita, cima, embaixo])[0] + 1

//             # Retorna o pedido com tamanho 3 para todas as saídas
//             if j == 0:
//                 print(f'{menor:>3}', end='')
//             else:
//                 print(f'{menor:>4}', end='')
//         print()
//     print()
