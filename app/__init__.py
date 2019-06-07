from tornado.web import Application
from tornado.options import options
from options import load_conf
load_conf()

import motor.motor_tornado
from app.settings import settings


def prepare_db():
    client = motor.motor_tornado.MotorClient(options.db_uri)
    db = client[options.db_name]
    return db


def make_app():
    return Application(**settings)


app = make_app()
