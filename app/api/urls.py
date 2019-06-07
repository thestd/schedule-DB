from app.api.handlers import MainHandler

urls = [
    (r"/api/users/(.*)", MainHandler),
]
