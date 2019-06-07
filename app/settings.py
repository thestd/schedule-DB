from tornado.options import options
import motor.motor_tornado
from app.api.urls import urls


def prepare_db():
    client = motor.motor_tornado.MotorClient(options.db_uri)
    database_client = client[options.db_name]
    return database_client


db = prepare_db()

settings = dict(
    handlers=urls,
    db=db,
    debug=True
)
