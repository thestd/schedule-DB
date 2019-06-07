from tornado.web import RequestHandler
import json
import bcrypt
from bson.json_util import dumps
from app.api.decorators import auth_required


class MainHandler(RequestHandler):

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    @auth_required
    async def get(self, user_id):
        db = self.settings['db']

        user = await db.users.find_one(dict(user_id=int(user_id)))
        if user is None:
            self.set_status(404)
            self.write("User does not exists. ")
        else:
            self.set_status(200)
            self.write(user.get('group'))

    @auth_required
    async def post(self, _):
        db = self.settings['db']

        user_id = self.json_args.get('user_id')
        group = self.json_args.get('group')
        query_type = self.json_args.get('query_type')

        check = await db.users.find_one(dict(user_id=user_id))
        if check is None:
            insert_check = await db.users.insert_one(dict(user_id=user_id,
                                                          group=group,
                                                          query_type=query_type))
            self.set_status(200)
            self.write("User {} was created.".format(insert_check.inserted_id))
        else:
            self.set_status(400)
            self.write("User already exists.")

