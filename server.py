
import os 
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond to GET requests
        client = self.headers.get("client")

        print(f"Client is : {client}")
        print("Send Something Man : ", end = '')
        self.wfile.write(input().encode())
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        # Handle POST request and print the data received
        content_length = int(self.headers['Content-Length'])  # Get the size of the data
        post_data = self.rfile.read(content_length)  # Read the data sent in the POST request

        # Print the received data (for debugging)
        print("Received POST data:", post_data.decode('utf-8'))

        # Send a JSON response back to the client
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "status": "success",
            "received_data": post_data.decode('utf-8')
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))


# Set up the server to run on port 8000
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    PORT = int(os.getenv("PORT", 8000))

    run(port=PORT)

