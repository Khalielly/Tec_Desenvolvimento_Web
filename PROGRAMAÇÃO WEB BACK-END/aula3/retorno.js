function test(lista) {
    let soma = 0;
    for (let i = 0; i < lista.length; i++) {
        soma += lista[i];
    }
    return soma;

    //-------------------------- resposta 2 utilizando parseInt ----------------------------------

    // for (elemento in lista) {
    //     soma += parseInt(lista[elemento]);
    // }

    // return soma;

}

let minhas_lista = test([5, 3]);
console.log(minhas_lista)
