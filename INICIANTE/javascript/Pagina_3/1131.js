// beecrowd | 1131
// Grenais
// Adaptado por Neilor Tonin, URI  Brasil

// Timelimit: 1
// A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

// - Quantos GRENAIS fizeram parte da estatística.
// - O número de vitórias do Inter.
// - O número de vitórias do Grêmio.
// - O número de Empates.
// - Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

// Entrada
// O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

// Saída
// Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

// Exemplo de Entrada	Exemplo de Saída
// 3 2                  Novo grenal (1-sim 2-nao)
// 1                    Novo grenal (1-sim 2-nao)
// 2 3                  3 grenais
// 1                    Inter:2
// 3 1                  Gremio:1
// 2                    Empates:0
//                      Inter venceu mais

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

let number;
let [x, y] = lines.shift().split(" ");
let X = parseInt(x);
let Y = parseInt(y);
let Inter = 0;
let Gremio = 0;
let empates = 0;
let cont = 0;
let team;

while (true) {
    if (X == Y) {
        empates++;
    }
    else if (Y > X) {
        Gremio++;
    }

    else if (X > Y) {
        Inter++;
    }
    cont++;
    console.log("Novo grenal (1-sim 2-nao)");
    number = lines.shift();
    if (number == 1) {
    }
    else {
        break;
    }
    [x, y] = lines.shift().split(" ");
    X = parseInt(x);
    Y = parseInt(y);
}

if (Inter > Gremio) {
    team = "Inter venceu mais";
}
else if (Inter < Gremio) {
    team = "Gremio venceu mais";
}
else {
    team = "Não houve vencedor"
}

console.log(`${cont} grenais\nInter:${Inter}\nGremio:${Gremio}\nEmpates:${empates}\n${team}`);