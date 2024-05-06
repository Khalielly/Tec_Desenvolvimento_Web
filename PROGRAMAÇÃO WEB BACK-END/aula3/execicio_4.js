const idade = function (data) {

    const hoje = new Date();
    const [dia, mes, ano] = data.split("/")
    let idade = hoje.getFullYear() - parseInt(ano)

    if (hoje.getMonth() < (parseInt(mes) - 1)) {
        return idade - 1
    } else if (hoje.getMonth() === (parseInt(mes) - 1)) {
        if (hoje.getDate() < parseInt(dia)) {
            return idade - 1
        }
    }
    return idade
}

console.log(idade('14/08/2005'))