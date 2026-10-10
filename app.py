from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 200 OK Response Header
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        
        # Binary stream payload
        message = "Hello World: Production Microservice Active via Jenkins CI/CD on AWS EC2!\n"
        self.wfile.write(message.encode("utf-8"))

    def log_message(self, format, *args):
        # Explicit STDERR logging with timestamping
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

if __name__ == "__main__":
    host, port = "0.0.0.0", 8000
    print(f"[BOOT] Initializing production web service on {host}:{port}...", flush=True)
    server = HTTPServer((host, port), HelloHandler)
    server.serve_forever()