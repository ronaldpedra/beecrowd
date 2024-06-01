// beecrowd | 1114
// Senha Fixa
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

// Entrada
// A entrada é composta por vários casos de testes contendo valores inteiros.

// Saída
// Para cada valor lido mostre a mensagem correspondente à descrição do problema.

// Exemplo de Entrada	Exemplo de Saída
// 2200                 Senha Invalida
// 1020                 Senha Invalida
// 2022                 Senha Invalida
// 2002                 Acesso Permitido

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

lines = lines.filter(item => item !== '')

for (var senha of lines) {

    if (senha.replace('\r', '') === '2002') {
        console.log(`Acesso Permitido`)
        break
    } else {
        console.log(`Senha Invalida`)
    }
}
