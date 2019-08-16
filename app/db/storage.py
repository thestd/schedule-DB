from pymongo.results import UpdateResult


def collection(collection_name):
    def wrapper(decorated_class):
        class CollectionClass(decorated_class):
            def __init__(self, db, *args, **kwargs):
                decorated_class.__init__(db, *args, **kwargs)
                self.db = db
                self.collection = db[collection_name]

        return CollectionClass

    return wrapper


@collection('users_schedule_query')
class ScheduleQuery:
    async def find(self, user_id: int) -> dict:
        return await self.collection.find_one(
            {'user_id': int(user_id)},
            {'_id': False}
        )

    async def save(self, user_id: int, query: str,
                   query_type: str) -> UpdateResult:
        return await self.collection.update_one(
            {'user_id': int(user_id)},
            {'$set': {'query': query, 'query_type': query_type}},
            upsert=True
        )
