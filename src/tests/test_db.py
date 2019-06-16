from tornado.testing import gen_test

from app.db.storage import ScheduleQuery
from tests.base import TornadoMotorAsyncTest


class ScheduleQueryDatabaseTest(TornadoMotorAsyncTest):
    def setUp(self) -> None:
        super().setUp()
        self.query = ScheduleQuery(self.db)

    @gen_test
    def test_object_insert(self):
        yield self.db.test.insert_one({'name': 'vasya',
                                       'surname': 'pupkin'})
        user = yield self.db.test.find_one({'name': 'vasya'})
        self.assertEqual(user['name'], 'vasya')
        self.assertEqual(user['surname'], 'pupkin')

    @gen_test
    def test_schedule_query_teacher_insert(self):
        yield self.query.save(1, 'Іщеряков Сергій Михайлович', 'teacher')
        model = yield self.query.find(user_id=1)
        self.assertEqual(model['user_id'], 1)
        self.assertEqual(model['query'], 'Іщеряков Сергій Михайлович')
        self.assertEqual(model['query_type'], 'teacher')

    @gen_test
    def test_schedule_query_not_found(self):
        model = yield self.query.find(user_id=1)
        self.assertIsNone(model)

    @gen_test
    def test_schedule_query_student_insert(self):
        yield self.query.save(1, 'ІПЗ-1', 'student')
        model = yield self.query.find(user_id=1)
        self.assertEqual(model['user_id'], 1)
        self.assertEqual(model['query'], 'ІПЗ-1')
        self.assertEqual(model['query_type'], 'student')

    @gen_test
    def test_schedule_query_update(self):
        yield self.query.save(2, 'ІПЗ-1', 'student')
        yield self.query.save(2, 'Іщеряков Сергій Михайлович', 'teacher')
        model = yield self.query.find(user_id=2)
        self.assertEqual(model['user_id'], 2)
        self.assertEqual(model['query'], 'Іщеряков Сергій Михайлович')
        self.assertEqual(model['query_type'], 'teacher')
