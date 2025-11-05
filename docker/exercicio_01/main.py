from http.server import BaseHTTPRequestHandler, HTTPServer

class ServerRequestsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)

            self.send_header('Content-type','application/json')
            self.end_headers()

            message = '{"Hello":"World","In":"Python"}'

            self.wfile.write(bytes(message,'utf8'))

def run_server(server_class=HTTPServer, server_handler_class=ServerRequestsHandler, port=8000):
    server_adress = ('0.0.0.0',port)
    http_server = server_class(server_adress,server_handler_class)
    print(f"Servidor rodando no caminho http://{server_adress[0]}:{port}/")
    http_server.serve_forever()

if __name__ == '__main__':
    run_server()