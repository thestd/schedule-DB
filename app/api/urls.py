from app.api.handlers import ScheduleQueryHandler

urls = [
    (r"/api/schedule-query/(?P<user_id>\d+)/?", ScheduleQueryHandler),
]
