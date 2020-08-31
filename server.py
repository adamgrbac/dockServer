import http.server
import socketserver

PORT=8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="server", **kwargs)

with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print("Serving at port: ", PORT)
    httpd.serve_forever()