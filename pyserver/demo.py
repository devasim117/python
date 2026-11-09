import logging
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("RawServer")

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logger.info(f"Received GET request for path: {self.path}")
        if(self.path== "/"):
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()

            response = {"message":"Server is running"}
            self.wfile.write(json.dumps(response).encode("utf-8"))

        if(self.path== "/status"):
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()

            response = {"message":"Status is up"}
            self.wfile.write(json.dumps(response).encode("utf-8"))


    def do_POST(self):
        if(self.path== "/data"):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                logger.info(f"Received POST data: {data}")
                self.send_response(200)
                self.send_header("Content-Type","application/json")
                self.end_headers()

                response = {"message":"Data received successfully"}
                self.wfile.write(json.dumps(response).encode("utf-8"))
            except json.JSONDecodeError:
                logger.error("Failed to decode JSON data")
                self.send_response(400)
                self.send_header("Content-Type","application/json")
                self.end_headers()

                response = {"error":"Invalid JSON data"}
                self.wfile.write(json.dumps(response).encode("utf-8"))

def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    logger.info(f"Server successfully running on http://localhost:{port}")

    try:
        httpd.serve_forever()
        
    except keyboardInterrupt:
        logger.info("Server is shutting down...")
        httpd.server_close()

if __name__ == "__main__":
    run_server(port=8000)