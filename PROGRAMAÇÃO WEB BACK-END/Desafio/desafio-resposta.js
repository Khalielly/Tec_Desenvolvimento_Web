var readingSync = require('readline-sync')

console.log("Bem-vindo ao Programa de Cálculo de Consumo de Combustível e Comparação de Preços!");
console.log("Por favor, insira os seguintes dados:");

let kmPercorrido = readingSync.question('- Quilômetros percorridos:');
let litrosCombust = readingSync.question('- Litros de combustível gastos:');
let precoAlcool = readingSync.question('- Preço do litro do álcool:');
let precoGasosa = readingSync.question('- Preço do litro da gasolina:');

kmPercorrido = parseFloat(kmPercorrido);
litrosCombust = parseFloat(litrosCombust);
precoAlcool = parseFloat(precoAlcool);
precoGasolina = parseFloat(precoGasosa);

let consumoMedio = kmPercorrido/litrosCombust;
let relacaoDePreco = precoAlcool/precoGasosa;
let vantagemCombust;

if (relacaoDePreco <= 0.7){
    vantagemCombust = "Álcool";
} else {
    vantagemCombust = "Gasolina";
}

console.log(`O consumo médio do seu veículo é de ${consumoMedio.toFixed(2)} km/l.`);
console.log(`A relação entre o preço do litro do álcool e da gasolina é de ${relacaoDePreco.toFixed(2)}`);
console.log(`Considerando a relação de preços, é mais vantajoso abastecer com  ${vantagemCombust}`);
