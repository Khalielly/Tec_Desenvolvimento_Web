function test(lista) {
    let soma = 0;
    for (let i = 0; i < lista.length; i++) {
        soma += lista[i];
    }
    return soma;
}

let minhas_lista = test([0, 3, 5, 9, 5]);
console.log(minhas_lista)