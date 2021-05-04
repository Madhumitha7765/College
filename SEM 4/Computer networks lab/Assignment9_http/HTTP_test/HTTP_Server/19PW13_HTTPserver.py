import time
from http.server import *
# http.server -- has BaseHTTPRequestHandler,HTTPServer
import os


#function that gives the rootdirectory to search for the html docs
def getRootDirectory():
    rootDir='C:/Users/Madhu/Desktop/PSG/madhu/SEM 4/Computer networks lab/19PW13_HTTP/19PW13/HTTP_Server/'
    return rootDir


#custom HTTPRequest Handler class
class http_RequestHandler(BaseHTTPRequestHandler):

    #function to handle get command,returns headers and content of the file
    def do_GET(self):
        # splitting data from file name
        x = self.path.split(',')
        if_modified=x[1]
        try:

            # gets last modified time from below command and compare with the given string

            fileStatsObj = os.stat(getRootDirectory() + self.path)
            modificationTime = time.ctime(fileStatsObj[os.stat.ST_MTIME])

            if(str(if_modified) == str(modificationTime)):
                # opens root directory and opens file
                file = open(getRootDirectory() + self.path)

                self.send_response(200)     #OK response sent to client
                self.send_header('Content-type', 'text-html')       #sends header to client
                self.end_headers()

                #reads html file an writes to the o/p stream
                html = file.read()
                self.wfile.write(bytes(html, "utf-8"))
                file.close()

                return
            else:
                self.send_response(304)  # OK response sent to client
                self.send_header('Content-type', 'text-html')  # sends header to client
                self.end_headers()

        except:
            self.send_error(404, 'file not found')

    # HEAD - returns headers without content of the file
    def do_HEAD(self):
        try:
            #opens root directory and opens file
            file = open(getRootDirectory() + self.path)
            self.send_response(200)     #OK response sent to client
            self.send_header('Content-type', 'text-html')       #sends header to client
            self.end_headers()
            return
        except:
            self.send_error(404, 'file not found')

    # PUT - creates file with entered data,is made idempotent
    def do_PUT(self):

        # splitting data from file name
        x = self.path.split(',')

        try:
            # if file exist,new file is not created
            if os.path.exists(getRootDirectory() + x[1]):
                self.send_response(200)
                self.send_header('Content-type', 'text-html')  # sends header to client
                self.end_headers()
                # say client that file already exists
                #self.send("File already exists !")

            else:
                # opening file in write mode
                file = open(getRootDirectory() + x[1], "w")
                self.send_response(201)  # Created response sent to client

                self.send_header('Content-type', 'text-html')  # sends header to client
                self.end_headers()

                # writing in the file
                file.write(x[0])
                file.close()
                return

        except:
            self.send_error(404, 'file not found')

    # POST - appends given data into specified file,its non idempotent
    def do_POST(self):
        x = self.path.split(',')
        try:
            file = open(getRootDirectory() + x[1], "a")
            self.send_response(201)  # OK response sent to client

            self.send_header('Content-type', 'text-html')  # sends header to client
            self.end_headers()
            file.write(x[0])
            file.close()
            return
        except:
            self.send_error(404, 'file not found')

    # DELETE - deletes given file
    def do_DELETE(self):
        if os.path.exists(getRootDirectory()+self.path):
            os.remove(getRootDirectory()+self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text-html')  # sends header to client
            self.end_headers()

        else:
            self.send_error(404,'file not found')
        return


#function that creates and runs a http server
def serverRun():
    print('http server is starting...')
    server_address = ('127.0.0.1', 9000)
    # HTTPServer -- tcp connection
    # http_RequestHandler -- method to do after connection is done
    httpServer = HTTPServer(server_address,http_RequestHandler)
    print('http server is running...')
    httpServer.serve_forever()

if __name__=='__main__':
    serverRun()