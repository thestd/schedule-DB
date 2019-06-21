#!/usr/bin/env python
from motor import MotorClient
from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.web import Application

from app.api.urls import urls


def make_app():
    db = MotorClient(options.db_uri)[options.db_name]
    return Application(handlers=urls,
                       db=db,
                       debug=True)


def main():
    app = make_app()
    app.listen(options.app_port)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
