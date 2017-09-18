__author__ = 'Avinesh_Kumar'

import BaseHTTPServer
import time
import HttpServerImpl

hostname="127.0.0.1"
port=80

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    counter = 0
    
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        from urlparse import urlparse, parse_qs
        query_components = parse_qs(urlparse(self.path).query)
        res = HttpServerImpl.perform_command(query_components)
        print "response: ",res
        self.wfile.write(res)

if __name__ == '__main__':
    server = BaseHTTPServer.HTTPServer
    httpserver = server((hostname, port), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (hostname, port)
    try:
        httpserver.serve_forever()
    except KeyboardInterrupt:
        pass
    httpserver.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (hostname, port)
