from tornado.options import options
from tornado.ioloop import IOLoop
from app import app


app.listen(options.app_port)
IOLoop.instance().start()
