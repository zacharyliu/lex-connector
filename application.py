import tornado.web
import tornado.wsgi

from tornado.web import url
from server import PingHandler, WSHandler

application = tornado.wsgi.WSGIAdapter(tornado.web.Application([
    url(r"/ping", PingHandler),
    url(r"/(.*)", WSHandler),
]))
