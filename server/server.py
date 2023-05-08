import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.166.218", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        

httpd = socketserver.TCPServer(("", PORT), MyHandler)

