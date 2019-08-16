import uuid

from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.testing import AsyncHTTPTestCase

from app.main import make_app


class TornadoMotorAsyncTest(AsyncHTTPTestCase):
    def setUp(self) -> None:
        options.db_name = str(uuid.uuid4())
        super().setUp()

    def tearDown(self) -> None:
        self.db.client.drop_database(options.db_name)

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_app(self):
        app = make_app()
        self.db = app.settings['db']
        return app
