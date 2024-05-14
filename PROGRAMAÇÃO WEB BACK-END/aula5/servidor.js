const http = require('http');

const port = 3000;
const host = 'localhost';
const resposta = `Minha Pagina`;

const resquestListener = function (req, res) {
    const { method, url } = req;

    if (url == '/teste') {
        res.end("Isso é um teste");
    } else if (url == '/professorteste') {
        res.end('Este é um prof');
    } else if (url == '/alunoresposta') {
        res.end('Isto é um aluno');
    }

    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(resposta);
}

const server = http.createServer();
server.on('request', resquestListener);

server.listen(port, host, () => {
    console.log(`Servidor rodando em http://${host}:${port}/`);

});