// beecrowd | 1049
// Animal
// Por Neilor Tonin, URI  Brasil

// Timelimit: 1
// Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

// vertebrado      ave         carnivoro   aguia
//                             onivoro     pomba
//                 mamifero    onivoro     homem
//                             herbivoro   vaca

// invertebrado    inseto      hematofago  pulga
//                             herbivoro   lagarta
//                 anelideo    hematofago  sanguessuga
//                             onivoro     minhoca

// Entrada
// A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

// Saída
// Imprima o nome do animal correspondente à entrada fornecida.

// Exemplos de Entrada	Exemplos de Saída
// vertebrado          homem
// mamifero
// onivoro

// vertebrado          aguia
// ave
// carnivoro

// invertebrado        minhoca
// anelideo
// onivoro

let input = require("fs").readFileSync("./INICIANTE/javascript/stdin", "utf8");
let lines = input.split("\n");

// Coleta dos dados
var caracteristicas = lines

// Processamento dos dados
function animalProcurado(caracteristicas) {
    var a = caracteristicas[0].replace('\r', '')
    var b = caracteristicas[1].replace('\r', '')
    var c = caracteristicas[2].replace('\r', '')

    if (a === "vertebrado") {
        if (b === 'ave'){
            if (c === 'carnivoro'){
                console.log('aguia')
            }
            if (c === 'onivoro'){
                console.log('pomba')
            }
        }
        if (b === 'mamifero'){
            if (c === 'onivoro'){
                console.log('homem')
            }
            if (c === 'herbivoro'){
                console.log('vaca')
            }
        }
    }
    if (a === 'invertebrado'){
        if (b === 'inseto'){
            if (c === 'hematofago'){
                console.log('pulga')
            }
            if (c === 'herbivoro'){
                console.log('lagarta')
            }
        }
        if (b === 'anelideo'){
            if (c === 'hematofago'){
                console.log('sanguessuga')
            }
            if (c === 'onivoro'){
                console.log('minhoca')
            }
        }
    }
}

// Retorno do pedido
animalProcurado(caracteristicas)
