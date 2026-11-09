import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configure logging so we can see server traffic
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger("RawServer")

# Define the server logic by subclassing the built-in handler
class SimpleExpressLikeHandler(BaseHTTPRequestHandler):
    
    # 1. HANDLE GET REQUESTS
    def do_GET(self):
        # Route: GET /
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            response = {"message": "Welcome to the raw Python server!"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
            
        # Route: GET /status
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            response = {"status": "healthy", "uptime": "good"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
            
        # 404 Not Found Route
        else:
            self.send_error_response(404, "Route not found")

    # 2. HANDLE POST REQUESTS
    def do_POST(self):
        # Route: POST /users
        if self.path == "/users":
            # Get the size of the incoming data
            content_length = int(self.headers.get("Content-Length", 0))
            # Read the raw string bytes from the request body
            raw_body = self.rfile.read(content_length)
            
            try:
                # Parse bytes into a Python dictionary (like express.json() middleware)
                data = json.loads(raw_body.decode("utf-8"))
                username = data.get("username", "Guest")
                
                self.send_response(201)  # 201 Created
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                
                response = {"message": f"User {username} created successfully!"}
                self.wfile.write(json.dumps(response).encode("utf-8"))
                
            except json.JSONDecodeError:
                self.send_error_response(400, "Invalid JSON payload")
        else:
            self.send_error_response(404, "Route not found")

    # Helper method to handle errors cleanly
    def send_error_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {"error": message}
        self.wfile.write(json.dumps(response).encode("utf-8"))

# =====================================================================
# SERVER INITIALISATION
# =====================================================================
def run_server(port=8080):
    server_address = ("", port)
    # HTTPServer takes the address binding and your custom routing handler class
    httpd = HTTPServer(server_address, SimpleExpressLikeHandler)
    logger.info(f"Server successfully running on http://localhost:{port}")
    try:
        httpd.serve_forever()  # Starts the infinite loop listening for requests
    except KeyboardInterrupt:
        logger.info("Server is shutting down gracefully...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
