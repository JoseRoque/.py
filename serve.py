from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # response status code
        self.send_response(200)

        # add headers to response
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # write message
        self.wfile.write(bytes("hello, world", "utf8"))
        return

# configure server
port = 8080
server_address = ("localhost", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

# run server
httpd.serve_forever()
