# -*- coding: utf-8 -*-

"""和main相比,这个使用gevent"""

import gevent
from gevent.pywsgi import WSGIServer
from application import wsgi_application
from tornado.options import define, options
    
    
class WServerManager(gevent.Greenlet):
    
    def __init__(self, port, app=None):
        self.port = port
        self.app = app
        gevent.Greenlet.__init__(self)

    def _app(self, environ, start_response):
        start_response('200 OK', [('Content-Type','text/plain')])
        yield "{0}\n".format(socket.getaddrinfo('www.baidu.com', 80))

    def _run(self):
        print("WSGI Server Listen at port {0}".format(self.port))
        server = WSGIServer(('0.0.0.0', self.port), self.app or self._app)
        server.serve_forever()


if __name__ == "__main__":
    options.logging = "none"
    options.parse_command_line()
    ws = WServerManager(8001, wsgi_application)
    ws.start()
    gevent.wait()
    
