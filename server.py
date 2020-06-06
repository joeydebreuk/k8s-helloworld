import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 7000
server_address = ("", PORT)


class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header(
            "Access-Control-Allow-Headers",
            "Origin, X-Requested-With, Content-Type, Accept",
        )
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({"hello": "world!"}).encode())

    # POST echoes the message adding a JSON field
    def do_POST(self):
        self._set_headers()
        self.wfile.write(json.dumps({"hello": "world!"}).encode())


print("serving at port", PORT)
httpd = HTTPServer(server_address, RequestHandler)
httpd.serve_forever()
