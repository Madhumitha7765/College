from http.server import *
import os

rD='C:/Users/Madhu/Desktop/PSG/madhu/SEM 4/Computer networks lab/Assignment9_http/CN_http/'

class http_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            file = open(rD + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            html = file.read()
            self.wfile.write(bytes(html, "utf-8"))
            file.close()
            return
        except:
            self.send_error(404, 'file not found')

    def do_PUT(self):
        x=self.path.split(',')
        try:
            file=open(rD +x[1],"w")
            self.send_response(201)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            file.write(x[0])
            file.close()
            return
        except:
            self.send_error(404, 'file not found')

    def do_POST(self):
        x = self.path.split(',')
        try:
            file = open(rD + x[1], "a")
            self.send_response(201)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            file.write(x[0])
            file.close()
            return
        except:
            self.send_error(404, 'file not found')

    def do_DELETE(self):
        if os.path.exists(rD+self.path):
            os.remove(rD+self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
        else:
            self.send_error(404,'file not found')
        return


if __name__=='__main__':
    server_address = ('127.0.0.1', 9000)
    httpServer = HTTPServer(server_address,http_RequestHandler)
    httpServer.serve_forever()