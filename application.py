import logging
import tornado.web
import tornado.wsgi

from tornado.web import url
from server import PingHandler, WSHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)7s %(message)s",
)
application = tornado.wsgi.WSGIAdapter(tornado.web.Application([
    url(r"/ping", PingHandler),
    url(r"/(.*)", WSHandler),
]))
