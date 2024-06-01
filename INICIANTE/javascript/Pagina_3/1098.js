// beecrowd | 1098
// Sequencia IJ 4
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

// Entrada
// Não há nenhuma entrada neste problema.

// Saída
// Imprima a sequencia conforme exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
//                      I=0 J=1
//                      I=0 J=2
//                      I=0 J=3
//                      I=0.2 J=1.2
//                      I=0.2 J=2.2
//                      I=0.2 J=3.2
//                      .....
//                      I=2 J=?
//                      I=2 J=?
//                      I=2 J=?

for (let i = 0.0; i <= 2.0; i += 0.2) {
    for (let j = 1; j <= 3; j++) {
        console.log(`I=${i.toFixed(1).replace('.0', '')} J=${(i + j).toFixed(1).replace('.0', '')}`)
    }
}
