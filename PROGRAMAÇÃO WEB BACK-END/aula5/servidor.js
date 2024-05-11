const http = require('http');

const port = 3000;
const host = "localhost";
const botao = 'console.log("to no front")';
const resposta = `
<head>
    <title>Exemplo Client-Side</title>
</head>
<body>
    <button id="meuBotao">Clique aqui</button>
    <script>${botao}</script>
</body>
</html>`

const resquestListener = function (req, res) {
    
    console.log("Chegou uma requisicao");
    res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'});
    res.end(resposta);
}

const server = http.createServer(resquestListener);

server.listen(port, host, () =>{
    console.log(`Servidor rodando em http://${host}:${port}/`);

});