#!/usr/bin/env python
from tornado.ioloop import IOLoop
from tornado.options import options

from app.settings.config import make_app


def start_loop():
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()


def main():
    app = make_app()
    app.listen(options.app_port)
    start_loop()


if __name__ == '__main__':
    main()
