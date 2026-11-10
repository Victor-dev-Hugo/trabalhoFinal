import json
import os
import socket
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.getenv("APP_PORT", "8000"))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        corpo = json.dumps({
            "servico": "api-simples",
            "mensagem": "Olá do segundo container!",
            "hostname": socket.gethostname(),
            "horario": datetime.now().isoformat(timespec="seconds"),
            "caminho": self.path,
        }, ensure_ascii=False).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)


if __name__ == "__main__":
    print(f"API rodando na porta {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
