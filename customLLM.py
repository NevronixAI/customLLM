from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Expected API key
EXPECTED_API_KEY = "NevronixAI"

class CustomLLMHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # --- 1️⃣ Print all headers ---
        print("=== Incoming Headers ===")
        for header, value in self.headers.items():
            print(f"{header}: {value}")
        print("========================\n")

        # --- 2️⃣ Check API Key from Authorization header ---
        auth_header = self.headers.get('Authorization', '')
        api_key = ''
        if auth_header.startswith("Bearer "):
            api_key = auth_header.split(" ", 1)[1]

        if api_key != EXPECTED_API_KEY:
            self.send_response(401)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid API Key"}).encode())
            print("Rejected request: invalid API key\n")
            return

        # --- 3️⃣ Read request body ---
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        # --- 4️⃣ Parse JSON and print all received parameters ---
        try:
            data = json.loads(body)
            print("=== Received JSON payload ===")
            print(json.dumps(data, indent=4))
            print("=============================\n")
            
            # Extract question separately if needed
            question = data.get('question', '')
            print(f"Received question: {question}\n")
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
            return

        # --- 5️⃣ Respond ---
        response_text = "It works"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"response": response_text}).encode())
        print(f"Responded with: {response_text}\n")


def run(server_class=HTTPServer, handler_class=CustomLLMHandler, port=5005):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Mock CustomLLM server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
