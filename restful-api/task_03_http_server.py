#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

"""This module sets up a simple HTTP server and request handler"""


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler class"""
    def do_GET(self):
        """handle get request"""
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"OK"}
            self.wfile.write(json.dumps(status).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """set up and start the server"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
