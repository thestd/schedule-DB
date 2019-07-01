import os

from motor import MotorClient
from tornado.options import define, options
from tornado.web import Application

from app.api.urls import urls


def load_conf():
    define("debug", default=os.getenv("DEBUG", True))
    define("db_name", default=os.getenv("DB_NAME", "pnu_schedule"))
    define("db_user", default=os.getenv("DB_USER", "user"))
    define("db_password", default=os.getenv("DB_PASSWORD", "password"))
    define("db_host", default=os.getenv("DB_HOST", "localhost"))
    define("db_port", default=os.getenv("DB_PORT", 27017))

    define("app_port", default=os.getenv("APP_PORT", 8888))
    define("secret", default=os.getenv("SECRET", "ABCDEFG!@#$%#"))
    define("auth_token", default=os.getenv("AUTH_KEY", "123456"))

    define("db_uri", default=os.getenv("DB_URI", ("mongodb://{}:{}@{}:{}/".
                                                  format(options.db_user,
                                                         options.db_password,
                                                         options.db_host,
                                                         options.db_port))))


def make_app():
    db = MotorClient(options.db_uri)[options.db_name]
    return Application(handlers=urls, db=db, debug=options.debug)
