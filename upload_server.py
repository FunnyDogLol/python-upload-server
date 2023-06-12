from http.server import HTTPServer, SimpleHTTPRequestHandler

class UploadHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        # Specify the directory where uploaded files will be saved
        upload_dir = 'uploads'
        
        # Retrieve the file data from the request
        file_data = self.rfile.read(int(self.headers['Content-Length']))
        
        # Extract the filename from the request headers
        print(self.headers)
        file_name = self.headers['filename']
        
        # Save the uploaded file
        with open(f"{upload_dir}/{file_name}", 'wb') as f:
            f.write(file_data)
        
        # Send a response indicating success
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
