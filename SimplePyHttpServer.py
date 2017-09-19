__author__ = 'Avinesh_Kumar'

'''
MIT License

Copyright (c) 2017 Avinesh Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
import BaseHTTPServer
import time
import HttpServerImpl
import json
from urlparse import urlparse, parse_qs

hostname="127.0.0.1"
port=80


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    keep_values = {}

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # print self.path
        # print urlparse(self.path).query
        query_components = parse_qs(urlparse(self.path).query)
        # print query_components
        res = HttpServerImpl.process_get(query_components)
        # print "response: ",res
        self.wfile.write(res)
        
    # support JSON post data only.
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        # print "post body: ",post_body
        self.send_response(200)
        self.end_headers()
        data = json.loads(post_body)
        res = HttpServerImpl.process_post(data)
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
