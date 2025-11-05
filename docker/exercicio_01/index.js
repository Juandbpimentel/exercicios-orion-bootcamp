import http from "node:http";

const hostname = '0.0.0.0';

const port = 3000;

const server = http.createServer((req,res)=>{
    res.statusCode = 200;
    res.setHeader('Content-Type','application/json')
    res.end('{"Hello":"World","In":"Node"}')
});

server.listen(port,hostname,()=>{
    console.log(`Servidor rodando no caminho http://${hostname}:${port}/`)
})