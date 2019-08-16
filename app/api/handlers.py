from tornado.escape import json_decode, json_encode
from tornado.web import RequestHandler

from app.db.storage import ScheduleQuery


class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def send_response(self, body, code=200):
        self.write(json_encode(body))
        self.set_status(code)
        self.finish()

    def send_error_response(self, detail, code=400):
        self.send_response({'detail': detail}, code=code)


class ScheduleQueryHandler(BaseHandler):
    SUPPORTED_METHODS = ["GET", "PUT"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.schedule_query = ScheduleQuery(self.db)

    async def get(self, user_id):
        schedule_query = await self.schedule_query.find(user_id=user_id)
        if schedule_query:
            self.send_response({
                'user_id': schedule_query['user_id'],
                'query': schedule_query['query'],
                'query_type': schedule_query['query_type']
            })
        else:
            message = f'The schedule query with id={user_id} mot found'
            self.send_error_response(message, code=404)

    async def put(self, user_id):
        user_id = int(user_id)
        try:
            query, query_type = self.validated_data(body=self.request.body)
            await self.schedule_query.save(user_id, query, query_type)
            self.send_response({
                'user_id': user_id,
                'query': query,
                'query_type': query_type
            })
        except ValueError as e:
            self.send_error_response(str(e))

    @staticmethod
    def validated_data(body):
        if not body:
            raise ValueError("Body can't be empty")
        body_json = json_decode(body)
        query = body_json.get('query')
        query_type = body_json.get('query_type')
        if not query:
            raise ValueError("Query can't be empty")
        if not query_type:
            raise ValueError("Query type can't be empty")
        return query, query_type

    @property
    def db(self):
        return self.application.settings['db']
