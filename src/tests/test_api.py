import json

from tornado.testing import gen_test

from app.db.storage import ScheduleQuery
from tests.base import TornadoMotorAsyncTest


class TestScheduleQueryHandler(TornadoMotorAsyncTest):
    def setUp(self) -> None:
        super().setUp()
        self.query = ScheduleQuery(self.db)

    def test_get_without_user_id(self):
        response = self.fetch('/api/schedule-query/')
        self.assertEqual(response.code, 404)

    def test_get_with_bad_param(self):
        response = self.fetch('/api/schedule-query/ss')
        self.assertEqual(response.code, 404)

    def test_get_with_not_found_user_id(self):
        response = self.fetch('/api/schedule-query/1')
        self.assertEqual(response.code, 404)
        response = self.fetch('/api/schedule-query/2/')
        self.assertEqual(response.code, 404)

    @gen_test
    def test_get_with_valid_user_id(self):
        url = '/api/schedule-query/1/'
        yield self.query.save(1, 'ПІ-4', 'student')
        response = yield self.http_client.fetch(self.get_url(url))
        data = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(data['user_id'], 1)
        self.assertEqual(data['query'], 'ПІ-4')
        self.assertEqual(data['query_type'], 'student')

    def test_put_new_schedule_query(self):
        body = {'query': 'ПІ-4', 'query_type': 'student'}
        response = self.fetch('/api/schedule-query/2',
                              method="PUT",
                              body=json.dumps(body))
        self.assertEqual(response.code, 200)
        data = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(data['user_id'], 2)
        self.assertEqual(data['query'], 'ПІ-4')
        self.assertEqual(data['query_type'], 'student')

    @gen_test
    def test_put_update_schedule_query(self):
        url = '/api/schedule-query/1/'
        body = {'query': 'ПІ-4', 'query_type': 'student'}
        yield self.query.save(1, 'ІПЗ-2', 'student')
        response = yield self.http_client.fetch(self.get_url(url),
                                                method="PUT",
                                                body=json.dumps(body))
        data = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(data['user_id'], 1)
        self.assertEqual(data['query'], 'ПІ-4')
        self.assertEqual(data['query_type'], 'student')

    @gen_test
    def test_empty_schedule_data(self):
        url = '/api/schedule-query/2/'
        invalid_body = {'query': "", 'query_type': "d"}
        body = json.dumps(invalid_body)

        response = yield self.http_client.fetch(self.get_url(url),
                                                method="PUT",
                                                body=body,
                                                raise_error=False)
        data = json.loads(response.body)

        self.assertEqual(response.code, 400)
        self.assertEqual(data['detail'], "Query can't be empty")

    @gen_test
    def test_empty_body(self):
        url = '/api/schedule-query/2/'

        response = yield self.http_client.fetch(self.get_url(url),
                                                method="PUT",
                                                body="",
                                                raise_error=False)
        data = json.loads(response.body)
        self.assertEqual(response.code, 400)
        self.assertEqual(data['detail'], "Body can't be empty")
