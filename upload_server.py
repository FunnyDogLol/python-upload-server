from http.server import HTTPServer, SimpleHTTPRequestHandler

class UploadHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        upload_dir = 'uploads'
        
        file_data = self.rfile.read(int(self.headers['Content-Length']))
        print(self.headers)
        file_name = self.headers['filename']
        
        with open(f"{upload_dir}/{file_name}", 'wb') as f:
            f.write(file_data)
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded successfully')

# Specify the server address and port
server_address = ('', 81)

# Create the server instance using the custom handler
httpd = HTTPServer(server_address, UploadHandler)

# Start the server
print("░▒▓█ ɆVłⱠ ₴ɆⱤV █▓▒░")
print('Server running on port 81...')
httpd.serve_forever()
