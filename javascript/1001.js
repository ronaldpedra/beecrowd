// beecrowd | 1001
// Extremamente Básico
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

// Entrada
// A entrada contém 2 valores inteiros.

// Saída
// Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade, conforme o exemplo abaixo.

// Exemplos de Entrada	Exemplos de Saída
// 10                   X = 19
// 9

// -10                  X = -6
// 4

// 15                   X = 8
// -7

// O arquivo stdin armazena as variáveis dos Exemplos de Entrada do beecrowd. Na linha de comando abaixo, o javascript lê o arquivo e realiza a operação
let input = require("fs").readFileSync("./javascript/stdin", "utf8");
// Pega cada linha do arquivo lido anteriormente e armazena como um elemento de uma lista. lines = ['10\r', '9']
let lines = input.split("\n");

// O comando armazena o valor do primeiro elemento na variável A. O comando shift remove o elemento da lista. lines = ['9']
var A = parseInt(lines.shift());
var B = parseInt(lines.shift());

console.log(`X = ${A + B}`);
